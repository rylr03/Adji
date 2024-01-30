function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var eyeIcon = document.querySelector(".eye-icon i");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove("fa-eye");
        eyeIcon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove("fa-eye-slash");
        eyeIcon.classList.add("fa-eye");
    }
}

function checkPasswordVisibility() {
    var passwordInput = document.getElementById("cpassword");
    var eyeIcon = document.querySelector(".eye-icon1 i");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove("fa-eye");
        eyeIcon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove("fa-eye-slash");
        eyeIcon.classList.add("fa-eye");
    }
}

function validateForm() {
    var checkbox = document.getElementById("myCheckbox");

    if (!checkbox.checked) {
      alert("Please agree to the terms and conditions.");
      return false;
    }

    return true; // Form will be submitted if all validations pass.
  }


var cartItemCount = 0;
var cartItems = [];

function addToCart(productId) {
    var product = getProductDetails(productId);
    var existingItem = cartItems.find(item => item.id === product.id);

    if (existingItem) {
        existingItem.quantity++;
    } else {
        product.quantity = 1;
        cartItems.push(product);
    }

    cartItemCount++;
    updateCartButton();
    updateCartSidebar();
}

function getProductDetails(productId) {
    if (productId === 1) {
        return {
            id: 1,
            name: 'Plain T-shirt',
            price: 99.00,
            type: 'Women',
            image: "{% static '/images/Pink Women.jpg' %}"
        };
    } else if (productId === 2) {
        return {
            id: 2,
            name: 'Plain T-shirt',
            price: 99.00,
            type: 'Women',
            image: "{% static '/images/Red Women.jpg' %}"
        };
    } else if (productId === 3) {
        return {
            id: 3,
            name: 'Plain T-shirt',
            price: 99.00,
            type: 'Women',
            image: "{% static '/images/Red Women.jpg' %}"
        };
    } else if (productId === 4) {
        return {
            id: 4,
            name: 'Plain T-shirt',
            price: 99.00,
            type: 'Men',
            image: "{% static '/images/Blue Men.jpg' %}"
        };
    }else if (productId === 5) {
        return {
            id: 5,
            name: 'Plain T-shirt',
            price: 99.00,
            type: 'Power Bank',
            image: "{% static '/images/Gray Men.jpg' %}"
        };
    }else if (productId === 6) {
        return {
            id: 6,
            name: 'Plain T-shirt',
            price: 99.00,
            type: 'Men',
            image: "{% static '/images/Black Men.jpg' %}"
        };
    }else if (productId === 7) {
        return {
            id: 7,
            name: 'Plain T-shirt',
            price: 89.00,
            type: 'Kid',
            image: "{% static '/images/Green Kids Boy.jpg' %}"
        };
    }else if (productId === 8) {
        return {
            id: 8,
            name: 'Plain T-shirt',
            price: 89.00,
            type: 'Kid',
            image: "{% static '/images/Red Kids Boy.jpg' %}"
        };
    }else if (productId === 9) {
        return {
            id: 9,
            name: 'Plain T-shirt',
            price: 89.00,
            type: 'Kid',
            image: "{% static '/images/Red Kids Boy.jpg' %}"
        };
    }

}

function updateCartButton() {
    var cartButton = document.getElementById('cartButton');
    var cartCount = document.querySelector('.cart-count');
    cartButton.textContent = '';
    cartCount.textContent = '' + cartItemCount + '';
}

function updateCartSidebar() {
    var cartItemsContainer = document.getElementById('cartItems');
    var emptyCartMessage = document.getElementById('emptyCartMessage');

    cartItemsContainer.innerHTML = '';

    if (cartItems.length === 0) {
        emptyCartMessage.style.display = 'block';
    } else {
        emptyCartMessage.style.display = 'none';

        cartItems.forEach(function(item) {
            var cartItemElement = document.createElement('div');
            cartItemElement.className = 'cart-item';
            cartItemElement.innerHTML = `
                    <div class="cart-item-image">
                    <img src="${item.image}" alt="${item.name}">
                    </div>
                    <div class="cart-item-details">
                        <span>Name: ${item.name}<br>Price: ₱ ${(item.price * item.quantity).toFixed(2)}<br>Type: ${item.type}</span>
                    </div>
                    <div class="quantity-container">
                        <button class="quantity-btn" onclick="changeQuantity(${item.id}, 'decrease')">-</button>
                        <span>${item.quantity}</span>
                        <button class="quantity-btn" onclick="changeQuantity(${item.id}, 'increase')">+</button>
                    </div>
                    <div class="buttons-wrapper">
                        <button class="delete-btn" onclick="deleteCartItem(${item.id})">Delete</button>
                        <button class="buy-btn" onclick="buyCartItem(${item.id})">Buy</button>
                    </div>
                `;
                cartItemsContainer.appendChild(cartItemElement);
            });
        }

        openCartSidebar();
    }

    function changeQuantity(productId, action) {
        var item = cartItems.find(item => item.id === productId);

        if (item) {
            if (action === 'increase') {
                item.quantity++;
            } else if (action === 'decrease' && item.quantity > 1) {
                item.quantity--;
            }

            updateCartSidebar();
        }
    }
    

    function deleteCartItem(productId) {
        var itemIndex = cartItems.findIndex(item => item.id === productId);
        

        if (itemIndex !== -1) {
            cartItems.splice(itemIndex, 1);
            cartItemCount--;
            updateCartButton();
            updateCartSidebar();
        }
    }

    function openCartSidebar() {
        document.getElementById('cartSidebar').style.right = '0';
    }

    function closeCartSidebar() {
        document.getElementById('cartSidebar').style.right = '-500px';
    }

    function buyCartItem() {
        alert('Redirecting to checkout...');
    }

    function buyAll() {
        // Add logic to handle buying all items in the cart
        alert('Buying all items...');
    }

    function deleteAll() {
        cartItems = [];
        cartItemCount = 0;
        updateCartButton();
        updateCartSidebar();
    }


    document.addEventListener("DOMContentLoaded", function () {
        let currentSlide = 0;
        const slides = document.querySelectorAll(".slide");
        const dots = document.querySelectorAll(".dot");
        const totalSlides = slides.length;
    
        function nextSlide() {
          currentSlide = (currentSlide + 1) % totalSlides;
          updateSlider();
        }
    
        function updateSlider() {
          const newTransformValue = -currentSlide * 100 + "%";
          document.querySelector(".slider").style.transform = "translateX(" + newTransformValue + ")";
          updateDots();
        }
    
        function updateDots() {
          dots.forEach((dot, index) => {
            dot.classList.toggle("active", index === currentSlide);
          });
        }
    
        function goToSlide(index) {
          currentSlide = index;
          updateSlider();
        }
    
        // Automatically advance to the next slide every 3 seconds
        setInterval(nextSlide, 3000);
      });

function showPopup(img) {
    var popupContainer = document.getElementById("popupContainer");
    var popupImage = document.getElementById("popupImage");
        
    popupImage.src = img.src;
    popupContainer.style.display = "flex";
}
      
    function hidePopup() {
    var popupContainer = document.getElementById("popupContainer");
    popupContainer.style.display = "none";
}
function changeProfilePicture(event) {
    const input = event.target;
    const file = input.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('profile-picture').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

function removeProfilePicture() {
    document.getElementById('profile-picture').src = 'default-profile.jpg'; // Replace with the path to your default profile picture
}