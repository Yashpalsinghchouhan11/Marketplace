// myscript.js
document.addEventListener("DOMContentLoaded", function () {
  const productForm = document.getElementById("product-form");
  
  productForm.addEventListener("submit", function (event) {
    event.preventDefault();
    // Get form data
    const formData = new FormData(productForm);

    // Add user email to form data
    console.log(formData)
    formData.append("Product_owner", "{{ request.user.email }}");

    // Fetch request
    fetch("/product/", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // Handle success response
        console.log("Success:", data);
        alert("Product registered successfully!");
        // Redirect or perform any other action as needed
      })
      .catch((error) => {
        // Handle error
        console.error("Error:", error);
        alert("Failed to register product!");
      });
  });
});

// Fetch data from the API
// fetch("http://localhost:8000/retrieve_product_info/") // Replace with your actual API endpoint
//   .then((response) => response.json())
//   .then((data) => {
//     // Process the data and display it
//     const productList = document.querySelector(".container");

//     data.forEach((product) => {
//       const productCard = document.createElement("div");

//       // Construct the full image URL
//       const baseUrl = "http://localhost:8000"; // Replace with your server's base URL
//       const imageUrl = `${baseUrl}${product.Product_image}`;

//       productCard.innerHTML = `
//       <div class="product-card">
//       <div class="img-container">
//         <div class="image-container">
//           <img src="${imageUrl}" style="height: 200px; width: auto;" alt="">
//         </div>
//         <h2 class="card-title">${product.Product_name}</h2>
//         <p>${product.Product_description}</p>
//         <p>Price: $${parseFloat(product.Product_price).toFixed(2)}</p>
//         <h4>Size: <span>S M L XL XXL</span></h4>
//         <div class="buttons-container">
//           <a href="" class="add-to-cart"><i class="fa-solid fa-cart-shopping"></i>Add To Cart</a>
//           <a href="" class="add-to-wishlist"><i class="fa-regular fa-heart"></i>Wishlist</a>
//         </div>
//       </div>
//     </div>
//                   `;

//       productList.appendChild(productCard);
//     });
//   })
//   .catch((error) => console.error("Error fetching data:", error));

