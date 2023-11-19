

# Flask PayPal Integration

This project demonstrates how to integrate PayPal Checkout with a Flask web application. The application displays a list of products, and when a user selects a product, the PayPal Checkout button allows them to make a purchase.

## Getting Started

### Prerequisites

- Python 3.x
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

### Setting Up

1. Clone the repository:

    ```bash
    https://github.com/Orrv2904/Flask-Paypal-Integration.git
    cd Flask-Paypal-Integration
    code .
    ```

2. Create a virtual environment:

    ```bash
    virtualenv venv
    ```
    or
   ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

5. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Replace the placeholder in `.env` with your own PostgreSQL database connection string:

```dotenv
DATABASE_URL=your_postgresql_connection_string
```

### Running the Application

1. Create tables in the database:

    ```bash
    python -m create
    ```

2. Add data to the products table, you can do it from the database manager.

3. Run the application:

    ```bash
    flask run
    ```



The application should be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## PayPal Integration

The PayPal integration is implemented in the `index.html` file. It fetches product information from the server and uses the PayPal SDK to create a checkout button.

Ensure you have a PayPal Sandbox account, and replace `client-id` in the script tag with your own PayPal client ID.

```html
<script src="https://www.paypal.com/sdk/js?client-id=your_paypal_client_id&currency=USD"></script>
```

## Usage

1. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

2. Select a product to view its details.

3. Click the PayPal Checkout button to initiate the payment process.

4. Complete the payment on the PayPal sandbox.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Authors

- [@orrv2904](https://github.com/Orrv2904)
