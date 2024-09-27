# urls.py
from django.urls import path
from .views import signup,login,verify_otp,forget_password,product,retrieve_product_info,get_products,logout,change_password,total_cart_item,Profile,Add_to_cart,Get_cart_detail,remove_cart_item,cart_quantity_plus,cart_quantity_minus,ProductDetail,MyOrders,Add_to_wishlist,remove_wishlist_item,Get_wishlist_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('changepassword/', change_password, name='change_password'),
    path('verify_otp/', verify_otp, name='otp'),
    path('forget_password/', forget_password, name='forget_password'),
    path('product/', product, name='create-product'),
    path('get_products/product/', product, name=''), 
    path('', retrieve_product_info, name='home'),
    path('get_products/', get_products, name='get_products'), 
    path('profile/', Profile, name='Profile'),
    path('total_cart_item/', total_cart_item, name='total_cart_item'),
    path('profile/changepassword', change_password, name='change_password'),
    path('Get_cart_detail/', Get_cart_detail, name='Get_cart_detail'),
    path('Add_to_cart/', Add_to_cart, name='Add_to_cart'),
    path('remove_cart_item/', remove_cart_item, name='remove_cart_item'),
    path('cart_quantity_plus/', cart_quantity_plus, name='cart_quantity_plus'),
    path('cart_quantity_minus/', cart_quantity_minus, name='cart_quantity_minus'),
    path('ProductDetail/', ProductDetail, name='ProductDetail'),
    path('ProductDetail/profile/', Profile),
    path('ProductDetail/changepassword', change_password),
    path('MyOrders/', MyOrders, name='MyOrders'),
    path('get_products/profile/', Profile, name='Profile'),
    path('Add_to_wishlist/', Add_to_wishlist, name='Add_to_wishlist'),
    path('Get_wishlist_detail/', Get_wishlist_detail, name='Get_wishlist_detail'),
    path('remove_wishlist_item/', remove_wishlist_item, name='remove_from_wishlist'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)