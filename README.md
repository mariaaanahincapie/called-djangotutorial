Django Tutorials — Online Store
===============================

This repository is the sample Django application built while following a Django tutorial. It includes simple pages (Home, About, Contact), a Products section with listing, detail, and a form to create products (in-memory simulation), and basic static styling.

Quick start
-----------
1. Clone the repo:

   git clone https://github.com/EmiltonMenaA/called-DjangoTutorials.git
   cd called-DjangoTutorials

2. Create and activate a virtual environment (Windows PowerShell):

   python -m venv venv
   .\venv\Scripts\Activate.ps1

3. Install dependencies (Django 6.x recommended):

   pip install django==6.0.1

4. Apply migrations and run the development server:

   python manage.py migrate
   python manage.py runserver

5. Open the app in your browser at http://127.0.0.1:8000/

Useful routes
-------------
- / — Home
- /about/ — About
- /contact/ — Contact
- /products/ — Product list
- /products/<id> — Product details
- /products/create — Create product form

