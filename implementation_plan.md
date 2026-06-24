# E-Commerce Backend Completion Plan

This plan details the step-by-step strategy for resolving existing bugs and implementing the missing backend features required for a complete e-commerce application.

---

## Phase 1: Bug Fixes & Project Stabilization
First, we must resolve the compilation and logical bugs preventing the server from starting and working properly.

### Proposed Changes

#### [MODIFY] [models.py](file:///D:/E-commerce%20website%20backend%20development/cart/models.py)
* **Goal**: Fix the syntax error and incorrect scope configuration.
* **Details**: Wrap user, product, and quantity inside a proper `CartItem` model class and fix `models.Foreignkey` to `models.ForeignKey`.

#### [MODIFY] [serializers.py](file:///D:/E-commerce%20website%20backend%20development/products/serializers.py)
* **Goal**: Correct the validate method location and prevent UnboundLocalError.
* **Details**: Move the `validate` method out of `class Meta` to the main class scope of `ProductImageSerializer` and initialize `exists = False` at the start of the method.

#### [MODIFY] [views.py](file:///D:/E-commerce%20website%20backend%20development/products/views.py)
* **Goal**: Fix the search field keyword.
* **Details**: Change `'discription'` to `'description'` in the `search_fields` of `ProductViewSets`.

---

## Phase 2: User Authentication & JWT Integration (`accounts` app)
Secure the APIs by implementing token-based authentication.

### Proposed Changes
* **JWT Configuration**: Configure `rest_framework` settings in `settings.py` to use `JWTAuthentication` as the default authentication class.
* **Serializers**: Create `UserRegisterSerializer` and `UserDetailSerializer`.
* **Views**:
  * Implement registration view (`RegisterView`).
  * Implement standard SimpleJWT token views (`TokenObtainPairView`, `TokenRefreshView`) for login and token refresh.
  * Implement user profile detail / edit views.
* **URLs**: Wire up accounts routing inside `accounts/urls.py` and register it in `ecommerce/urls.py`.

---

## Phase 3: Cart Management (`cart` app)
Allow users to add, update, list, and delete items from their shopping cart.

### Proposed Changes
* **Models**: Complete the `CartItem` model.
* **Serializers**: Create `CartItemSerializer` supporting write operations (adding/updating quantities) and read operations (nesting product details).
* **Views**: Create endpoints to:
  * `POST /api/cart/` - Add an item to the cart or update its quantity if it already exists.
  * `GET /api/cart/` - Retrieve all cart items for the authenticated user.
  * `PATCH /api/cart/<int:pk>/` - Update the quantity of a specific cart item.
  * `DELETE /api/cart/<int:pk>/` - Remove an item from the cart.
* **URLs**: Configure `cart/urls.py` and register it in `ecommerce/urls.py`.

---

## Phase 4: Address Management (`addresses` app)
Enable shipping/billing address configurations for order checkouts.

### Proposed Changes
* **Models**: Create `Address` model (fields: user, street_address, city, state, postal_code, country, phone_number, is_default).
* **Serializers**: Create `AddressSerializer` mapping all fields.
* **Views**: Create an `AddressViewSet` (ModelViewSet) restricted to authenticated users. When saving, assign the current user.
* **URLs**: Configure `addresses/urls.py` and register it in `ecommerce/urls.py`.

---

## Phase 5: Ordering System (`orders` app)
Coordinate checkout and manage order tracking.

### Proposed Changes
* **Models**:
  * `Order`: fields like user, shipping_address, status (PENDING, PAID, SHIPPED, DELIVERED, CANCELLED), total_amount, and created_at.
  * `OrderItem`: fields like order, product, price, quantity.
* **Views**:
  * Create a checkout endpoint that:
    1. Validates the cart is not empty.
    2. Validates product stock is sufficient.
    3. Calculates totals.
    4. Creates `Order` and `OrderItem` records.
    5. Deducts stock from products.
    6. Clears the user's cart.
* **URLs**: Configure `orders/urls.py` and register it in `ecommerce/urls.py`.

---

## Phase 6: Payments (`payments` app)
Secure checkout orders with simulated or real payment gateways.

### Proposed Changes
* **Simulation/Gateway**: Set up dummy payment hooks to transition order status from `PENDING` to `PAID`.
* **Models/Logs**: Define a `Payment` transaction record tracking order, transaction ID, payment status, and gateway response details.

---

## Phase 7: API Documentation & Verification
* **Swagger/API Docs**: Set up `drf-yasg` in `ecommerce/urls.py` to auto-generate Swagger UI and ReDoc pages so frontend devs can easily integrate.
* **Automated Tests**: Write basic integration tests for core e-commerce flow (register -> login -> add product -> add to cart -> checkout).

---

## Open Questions & Design Decisions
> [!IMPORTANT]
> 1. **Payment Gateway**: Should we implement a real payment gateway (like Stripe, PayPal, Razorpay) in sandbox mode, or is a dummy simulation endpoint sufficient for your goals?
> 2. **Authentication Flow**: Do you want user email verification (via email sending) or simple registration and immediate login?
