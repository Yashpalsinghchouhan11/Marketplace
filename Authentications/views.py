# views.py
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import SignUpForm,LoginForm,Changepassword
from django.contrib.auth import update_session_auth_hash
import random
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import string
from django.http import JsonResponse
from .models import Product,CustomUser,Cart,Wishlist
import json
from django.db.models import Q

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # email = request.POST['email']
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to database yet
            # Hash the password
            password = form.cleaned_data.get('password')  # Get the raw password
            user.set_password(password)
            form.save()
            messages.info(request, 'Your Acoount has been successfully created !')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                # Email and password authentication successful
                    # No OTP verification required, proceed with login
                    auth_login(request, user)
                    messages.success(request, 'Login successfully !')
                    # Redirect to a success page or home page
                    return redirect('home')
            else:
    # Invalid email or password
                messages.error(request, 'Invalid email or password.')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')

# @api_view(['POST'])
def verify_otp(request):
    if request.method == 'POST':
        # Parse JSON data from request body
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
        # Retrieve OTP value from parsed JSON data
        otp_value = body_data.get('otp')
        print(otp_value)  # Print the OTP value to the console for debugging
        store_otp = cache.get(otp_value)

        if store_otp == otp_value:
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')  # Add error message
        return redirect('verify_otp')
    return render(request, "otp.html")


def forget_password(request):
    if request.method == "post":
        email = request.POST.get('')
        


def generate_otp(digits=4):
    return ''.join(random.choices(string.digits, k=digits))

def send_otp_to_email(email, otp):
    subject = 'Your OTP for Signup'
    message = f'Your OTP for signup is: {otp}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def resend_otp(request):
    email = request.data.get('email')

    # Clear any existing OTP for the given email
    cache_key = {email}
    cache.delete(cache_key)

    # Generate a new OTP and store it in the cache
    otp = generate_otp(digits=6)   # Generate OTP
    cache.set(cache_key, otp, timeout=300)  # 5 minutes timeout

    # Send the new OTP to the user's email address
    send_otp_to_email(email, otp)
    
# @login_required(login_url='/login/')
# def forget_password(request):
#     user_email = request.user.email
#     print(user_email)    # Forget password logic goes here
#     # This view is accessed only if the user is logged in, so redirecting to login doesn't make sense
#     return render(request, 'ForgetPassword.html')


@login_required(login_url='/login/')
def product(request):
    if request.method == 'POST':
        # Ensure the user is authenticated
        if request.user.is_authenticated:
            # Verify if the user is a CustomUser instance
            if isinstance(request.user, get_user_model()):
                # Retrieve product data from the request
                product_name = request.POST.get('Product_name')
                product_category = request.POST.get('Product_category')
                product_price = request.POST.get('Product_price')
                product_quantity = request.POST.get('Product_quantity')
                product_description = request.POST.get('Product_description')

                # Handle file upload
                product_image = request.FILES.get('Product_image')

                # Create the product with the current user's instance
                Product.objects.create(
                    Product_owner=request.user,
                    Product_name=product_name,
                    Product_category=product_category,
                    Product_image=product_image,
                    Product_price=product_price,
                    Product_quantity=product_quantity,
                    Product_description=product_description
                )

                return JsonResponse({'message': 'Product registered successfully'}, status=201)
            else:
                return JsonResponse({'error': 'User is not a CustomUser instance'}, status=401)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    else:
        # If it's a GET request, render the product form
        context = {
            **total_cart_item(request)
        }
        return render(request, 'productform.html',context)


def retrieve_product_info(request):
    try:
        products = Product.objects.all()
        Cart_detail = Cart.objects.filter(User = request.user)
        # count = 0
        # for cart in Cart_detail:
        #     count += 1

    except Product.DoesNotExist:
        return Response({"error": "No products found."}, status=404)
    context = {
        'products': products,
        **total_cart_item(request)
    }
    return render(request, 'home.html', context)



def get_products(request):
    if request.method == 'GET' and 'category' in request.GET:
        category = request.GET['category']
        products = Product.objects.filter(Product_category=category)
        context = {
            'products': products, 
            'category': category,
            **total_cart_item(request)
        }
        return render(request, 'home.html',context)
    else:
        products = Product.objects.all()
        return render(request, 'home.html', {'products': products, 'category': 'All'})



@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = Changepassword(request.POST)
        if form.is_valid():
            user = request.user
            new_password = form.cleaned_data['password']
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Update the session to prevent the user from being logged out
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')  # Redirect to the same page after successful password change
    else:
        form = Changepassword()
    return render(request, 'changepassword.html', {'form': form})


def Profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            section = request.GET.get('section')
            Profile_data = CustomUser.objects.filter(email = user.email)
            SellingProductData = Product.objects.filter(Product_owner_id = user.email)
            context = {
                'section':section,
                'profile_data':Profile_data,
                'SellingProductData':SellingProductData,
                **total_cart_item(request)
                }
            return render(request, 'Profile.html',context)
        else:
            return redirect('login')
    else:
        return render(request, 'Profile.html')
    
@login_required(login_url='/login/')
def Add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if Cart.objects.filter(User=request.user, Product_id=product_id).exists():
            messages.info(request, 'Item already exists in your cart.')
            return redirect('home')
        else:
            user = request.user
            # product_id = request.POST.get('product_id')
            Product_info = Product.objects.get(id = product_id)
            Cart(User=user, Product = Product_info).save()
            messages.success(request, 'Item Added to cart')
    return redirect('home')

def total_cart_item(request):
    count = 0
    # if request.method == 'GET':
    Cart_detail = Cart.objects.filter(User = request.user)
    for cart in Cart_detail:
        count += 1
    return {'total_cart_item':count}

@login_required(login_url='/login/')
def Get_cart_detail(request):
    if request.method == 'GET':
        loggedin_user = request.user
        Cart_detail = Cart.objects.filter(User = loggedin_user)
        total_amount = 0
        count = 0
        for cart in Cart_detail:
            amount = cart.quantity * cart.Product.Product_price
            total_amount = total_amount + amount
            count += 1
        # context = {
        #     'total_cart_item' : count,
        #     'Total_amount' : total_amount,
        # }
        return render(request, 'Cart.html',{'carts':Cart_detail, 'total_cart_item' : count, 'Total_amount' : total_amount})
    

def remove_cart_item(request):
    if request.method == 'POST':
        Cart_id = request.POST.get('cart_id')
        Instance = Cart.objects.filter(id = Cart_id)
        Instance.delete()
        messages.info(request, 'Item Removed !')
        return redirect('Get_cart_detail')
    

def cart_quantity_plus(request):
    if request.method == 'GET':
        P_id = request.GET['prod_id']
        cart_quantity = Cart.objects.get(Q(User = request.user) & Q(Product = P_id))
        if (cart_quantity.quantity < 10):
            cart_quantity.quantity += 1
        else:
            messages.info(request, 'only 10 quantity is allow to each order!')
        cart_quantity.save()
        user = request.user
        carts = Cart.objects.filter(User=user)
        total_amount = 0
        # count = 0
        for cart in carts:
            amount = cart.quantity * cart.Product.Product_price
            total_amount = total_amount + amount
            # count += 1
        context = {
            # 'total_cart_items' : count,
            'Total_amount' : total_amount,
        }
        # data = {'quantity': cart.quantity}
        return JsonResponse(context)
    
def cart_quantity_minus(request):
    if request.method == 'GET':
        P_id = request.GET['prod_id']
        cart_quantity = Cart.objects.get(Q(User = request.user) & Q(Product = P_id))
        if (cart_quantity.quantity > 1):
            cart_quantity.quantity -= 1
        else:
            messages.info(request, 'Quantity should not have 0')
        cart_quantity.save()
        user = request.user
        carts = Cart.objects.filter(User=user)
        total_amount = 0
        # count = 0
        for cart in carts:
            amount = cart.quantity * cart.Product.Product_price
            total_amount = total_amount + amount
            # count += 1
        context = {
            # 'total_cart_items' : count,
            'Total_amount' : total_amount,
        }
        # data = {'quantity': cart.quantity}
        return JsonResponse(context)
    

def ProductDetail(request):
    if request.method == 'POST':
        Product_id = request.POST.get('product_id')
        Instance = Product.objects.filter(id=Product_id)
        context = {
            'product_info': Instance,
            **total_cart_item(request)
        }
        return render(request, "Productpage.html",context)
    else:
        return HttpResponse("Method not allowed")
    

@login_required(login_url='/login/')
def Add_to_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if Wishlist.objects.filter(User=request.user, Product_id=product_id).exists():
            messages.info(request, 'Item already exists in your wishlist.')
            return redirect('home')
        else:
            user = request.user
            # product_id = request.POST.get('product_id')
            Product_info = Product.objects.get(id = product_id)
            Wishlist(User=user, Product = Product_info).save()
            messages.success(request, 'Item Added to wishlist')
    return redirect('home')


@login_required(login_url='/login/')
def Get_wishlist_detail(request):
    if request.method == 'GET':
        loggedin_user = request.user
        Wishlist_detail = Wishlist.objects.filter(User = loggedin_user)
        # for wishlist in Wishlist_detail:
        #     amount = wishlist.Product.Product_price
        context = {
            'Wishlist':Wishlist_detail,
            **total_cart_item(request)
            }
        return render(request, 'wishlist.html',context)

def remove_wishlist_item(request):
    if request.method == 'POST':
        Wishlist_id = request.POST.get('wishlist_id')
        Instance = Wishlist.objects.filter(id = Wishlist_id)
        Instance.delete()
        messages.info(request, 'Item Removed !')
        return redirect('Get_wishlist_detail')

def MyOrders(request):
    context = {
        **total_cart_item(request),
        }
    return render(request, 'orders.html',context)
