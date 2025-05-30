const cart = [];
let currentItem = null;

// Modal instances
const quantityModal = new bootstrap.Modal(document.getElementById('quantityModal'));
const amountModal = new bootstrap.Modal(document.getElementById('amountModal'));

function showQuantityModal(item) {
    currentItem = item;
    document.getElementById('product-name').textContent = item.name;
    document.getElementById('product-price').textContent = item.price.toFixed(2);
    document.getElementById('quantity-input').value = 1;
    updateProductSubtotal();
    quantityModal.show();
}

function showAmountModal(item) {
    currentItem = item;
    document.getElementById('service-name').textContent = item.name;
    document.getElementById('service-base-price').textContent = item.price.toFixed(2);
    document.getElementById('amount-input').value = item.price.toFixed(2);
    amountModal.show();
}

function updateProductSubtotal() {
    const quantity = parseInt(document.getElementById('quantity-input').value) || 1;
    const price = currentItem.price;
    const subtotal = quantity * price;
    document.getElementById('product-subtotal').textContent = subtotal.toFixed(2);
}

function addProductToCart() {
    const quantity = parseInt(document.getElementById('quantity-input').value) || 1;
    const cartItem = {
        id: currentItem.id,
        name: currentItem.name,
        category: 'product',
        price: currentItem.price,
        quantity: quantity,
        total: currentItem.price * quantity
    };
    cart.push(cartItem);
    updateCart();
    quantityModal.hide();
}

function addServiceToCart() {
    const amount = parseFloat(document.getElementById('amount-input').value) || 0;
    const cartItem = {
        id: currentItem.id,
        name: currentItem.name,
        category: 'service',
        price: amount,
        quantity: 1,
        total: amount
    };
    cart.push(cartItem);
    updateCart();
    amountModal.hide();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const totalElement = document.getElementById('total');
    const cartCount = document.getElementById('cart-count');
    const emptyCart = document.getElementById('empty-cart');
    const cartFooter = document.getElementById('cart-footer');

    // Clear existing items
    cartItems.innerHTML = '';

    if (cart.length === 0) {
        emptyCart.classList.remove('d-none');
        cartItems.classList.add('d-none');
        cartFooter.classList.add('d-none');
        cartCount.textContent = '0';
        totalElement.textContent = '0.00';
        return;
    }

    emptyCart.classList.add('d-none');
    cartItems.classList.remove('d-none');
    cartFooter.classList.remove('d-none');

    let total = 0;
    let itemCount = 0;

    cart.forEach((item, index) => {
        total += item.total;
        itemCount += item.category === 'product' ? item.quantity : 1;

        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item mb-3 p-3 border rounded-3 bg-light';

        if (item.category === 'product') {
            cartItem.innerHTML = `
                        <div class="d-flex justify-content-between align-items-start">
                            <div class="flex-grow-1">
                                <h6 class="mb-1 text-dark fw-semibold">${item.name}</h6>
                                <small class="text-muted">Product • ${item.price} each</small>
                            </div>
                            <button class="btn btn-outline-danger btn-sm" onclick="removeFromCart(${index})" title="Remove item">
                                <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                                </svg>
                            </button>
                        </div>
                        <div class="d-flex justify-content-between align-items-center mt-2">
                            <div class="quantity-controls d-flex align-items-center">
                                <button class="btn btn-outline-secondary btn-sm" onclick="decreaseQuantity(${index})">
                                    <svg width="12" height="12" fill="currentColor" viewBox="0 0 16 16">
                                        <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8z"/>
                                    </svg>
                                </button>
                                <span class="mx-3 fw-semibold">${item.quantity}</span>
                                <button class="btn btn-outline-secondary btn-sm" onclick="increaseQuantity(${index})">
                                    <svg width="12" height="12" fill="currentColor" viewBox="0 0 16 16">
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                                    </svg>
                                </button>
                            </div>
                            <div class="text-end">
                                <div class="fw-bold text-success">${item.total.toFixed(2)}</div>
                            </div>
                        </div>
                    `;
        } else {
            cartItem.innerHTML = `
                        <div class="d-flex justify-content-between align-items-start">
                            <div class="flex-grow-1">
                                <h6 class="mb-1 text-dark fw-semibold">${item.name}</h6>
                                <small class="text-muted">Service</small>
                            </div>
                            <button class="btn btn-outline-danger btn-sm" onclick="removeFromCart(${index})" title="Remove item">
                                <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                                </svg>
                            </button>
                        </div>
                        <div class="d-flex justify-content-between align-items-center mt-2">
                            <div class="amount-controls d-flex align-items-center">
                                <label class="form-label mb-0 me-2 small text-muted">Amount:</label>
                                <input type="number" class="form-control form-control-sm" style="width: 100px;" 
                                       value="${item.total.toFixed(2)}" step="0.01" min="0"
                                       onchange="updateServiceAmount(${index}, this.value)">
                            </div>
                            <div class="text-end">
                                <div class="fw-bold text-success">${item.total.toFixed(2)}</div>
                            </div>
                        </div>
                    `;
        }

        cartItems.appendChild(cartItem);
    });

    cartCount.textContent = itemCount;
    totalElement.textContent = total.toFixed(2);
}

function increaseQuantity(index) {
    if (cart[index].category === 'product') {
        cart[index].quantity += 1;
        cart[index].total = cart[index].quantity * cart[index].price;
        updateCart();
    }
}

function decreaseQuantity(index) {
    if (cart[index].category === 'product' && cart[index].quantity > 1) {
        cart[index].quantity -= 1;
        cart[index].total = cart[index].quantity * cart[index].price;
        updateCart();
    }
}

function updateServiceAmount(index, newAmount) {
    const amount = parseFloat(newAmount) || 0;
    if (cart[index].category === 'service') {
        cart[index].total = amount;
        updateCart();
    }
}

function removeFromCart(index) {
    cart.splice(index, 1);
    updateCart();
}

function checkout() {
    if (cart.length === 0) {
        alert('Cart is empty!');
        return;
    }

    // Prepare data for backend - each cart item becomes an Order record
    const orderData = {
        orders: cart.map(item => ({
            item_id: item.id,
            quantity: item.category === 'product' ? item.quantity : null,
            amount: item.total
        }))
    };

    // Send to backend
    fetch('/checkout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(orderData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(`${data.orders_created} orders placed successfully!`);
                cart.length = 0; // Clear cart
                updateCart();
            } else {
                alert('Error placing order: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error placing order');
        });
}

function setupEventListeners() {
    // Product cards
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', () => {
            const item = {
                id: card.getAttribute('data-id'),
                name: card.getAttribute('data-name'),
                price: parseFloat(card.getAttribute('data-price')) || 0,
                category: 'product'
            };
            showQuantityModal(item);
        });
    });

    // Service cards
    document.querySelectorAll('.service-card').forEach(card => {
        card.addEventListener('click', () => {
            const item = {
                id: card.getAttribute('data-id'),
                name: card.getAttribute('data-name'),
                price: parseFloat(card.getAttribute('data-price')) || 0,
                category: 'service'
            };
            showAmountModal(item);
        });
    });

    // Update subtotal when quantity changes
    document.getElementById('quantity-input').addEventListener('input', updateProductSubtotal);
}

document.addEventListener('DOMContentLoaded', setupEventListeners);