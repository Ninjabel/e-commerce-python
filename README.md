# E-Commerce API

## Overview

This is a simple e-commerce API built with Flask. It includes endpoints for managing users, products, orders, and shopping carts. You can create, read, update, and delete entities via RESTful APIs.

## Installation

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Application

To start the application, run the `run.py` file:

```bash
python run.py
```

## How to Run Tests

To run unit tests, use the following command:

```bash
python -m unittest discover -s app/tests
```

### 1. Users
- **GET `/users/`**: Retrieves all users.
- **GET `/users/<int:user_id>`**: Retrieves a user by ID.
- **POST `/users/`**: Creates a new user.
- **DELETE `/users/<int:user_id>`**: Deletes a user.
- **PUT `/users/<int:user_id>`**: Updates a user.

---

### 2. Products
- **GET `/products/`**: Retrieves the list of products.
- **GET `/products/<int:product_id>`**: Retrieves a product by ID.
- **POST `/products/`**: Creates a new product.
- **DELETE `/products/<int:product_id>`**: Deletes a product.
- **PUT `/products/<int:product_id>`**: Updates a product.

---

### 3. Orders
- **GET `/orders/`**: Retrieves all orders.
- **GET `/orders/<int:order_id>`**: Retrieves order details by ID.
- **POST `/orders/`**: Creates a new order.
- **DELETE `/orders/<int:order_id>`**: Deletes an order.
- **PUT `/orders/<int:order_id>`**: Updates an order.

---

### 4. Cart
- **GET `/cart/<int:user_id>`**: Retrieves the details of the user's cart.
- **POST `/cart/<int:user_id>/add`**: Adds a product to the user's cart.
- **POST `/cart/<int:user_id>/remove`**: Removes a product from the user's cart.
- **POST `/cart/<int:user_id>/clear`**: Empties the user's cart.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
