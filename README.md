# Django Tutorials — Online Store

This repository is the sample Django application built while following a Django tutorial. It includes simple pages (Home, About, Contact), a Products section with listing, detail, and a form to create products, a shopping cart system using sessions, and dependency injection with image upload functionality.

## Quick start

1. Clone the repo:
git clone https://github.com/mariaaanahincapie/called-djangotutorial.git
cd called-djangotutorial

2. Create and activate a virtual environment (Anaconda):
conda create -n django_env python=3.11
conda activate django_env

3. Install dependencies:
pip install django
pip install factory_boy

4. Apply migrations and seed the database:
python manage.py migrate
python manage.py seed_products

5. Run the development server:
python manage.py runserver

6. Open the app in your browser at http://127.0.0.1:8000/

## Useful routes

* `/` — Home
* `/about/` — About
* `/contact/` — Contact
* `/products/` — Product list
* `/products/<id>` — Product detail
* `/products/create` — Create product form
* `/cart/` — Shopping cart
* `/image/` — Image upload with Dependency Injection
* `/imagenotdi/` — Image upload without Dependency Injection

## Author

Developed by: Mariana Hincapie Henao
