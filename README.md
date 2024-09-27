# Marketplace

Welcome to the **Marketplace** project! This repository contains a full-stack marketplace application built using Django for the backend and HTML, CSS, and JavaScript for the frontend.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Marketplace** is a web application that allows users to browse, buy, and sell products. It is designed to be a simple and efficient platform for connecting buyers and sellers, showcasing a variety of goods.

This project leverages Django to handle backend operations, including user authentication, data handling, and server-side logic, while the frontend is built with HTML, CSS, and JavaScript for an engaging user experience.

You can find the source code for this project here: [Marketplace GitHub Repository](https://github.com/Yashpalsinghchouhan11/Marketplace.git).

## Technologies Used

The following technologies were used to develop this project:

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL (configured via Django ORM)
- **Caching**: Redis (via Django Redis Cache)
- **REST Framework**: Django REST Framework
- **Authentication**: Custom User Model, JWT
- **Email**: SMTP via Gmail
- **Other**: Docker (optional), CORS Headers, dotenv for environment configuration

## Features

- User registration and authentication (custom user model)
- Browse a wide range of products
- Add products to sell (authenticated users only)
- Responsive UI built with HTML, CSS, and JavaScript
- REST API for backend communication
- Support for Redis caching to improve performance
- Configurable email service for notifications

## Installation

To get started with this project locally, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Yashpalsinghchouhan11/Marketplace.git
    cd Marketplace
    ```

2. **Set up Virtual Environment**:
    Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    Install the required packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Environment Variables**:
    Create a `.env` file in the project root and add the necessary environment variables (you can refer to the example below):
    ```env
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=localhost
    DB_PORT=3306
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_email_password
    ```

5. **Run Migrations**:
    Set up the database by running Django migrations:
    ```sh
    python manage.py migrate
    ```

6. **Run the Server**:
    Start the local development server:
    ```sh
    python manage.py runserver
    ```

7. **Access the Application**:
    Visit `http://127.0.0.1:8000` in your web browser to access the Marketplace application.

## Usage

- **Home Page**: Browse featured products and categories.
- **User Registration/Login**: Create an account or log in to add your own products.
- **Product Listings**: View product details and add items to your cart.
- **Sell Products**: Authenticated users can add new products for sale.

## Project Structure

The project follows a common Django project structure:


## Contributing

Contributions are welcome! If you would like to contribute to the project:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

Please make sure to follow the code style and add relevant tests if necessary.

## License

This project is open source and available under the [MIT License](LICENSE).

