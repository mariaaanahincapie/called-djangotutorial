from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django import forms

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World!')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page Online Store is a web application developed as an academic project using the Django framework.",
            "author": "Developed by: Emilton Mena Acevedo",
        })
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "Contact",
            "email": "info@example.com",
            "address": "123 Fake Street, Faketown",
            "phone": "+1 (555) 123-4567",
        })
        return context


from django.views import View

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 499},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 999},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 49},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 79}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        # Validate id: must be an integer within product range; otherwise redirect home
        try:
            idx = int(id) - 1
            if idx < 0 or idx >= len(Product.products):
                return HttpResponseRedirect(reverse('home'))
        except (ValueError, TypeError):
            return HttpResponseRedirect(reverse('home'))

        viewData = {}
        product = Product.products[idx]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] =  product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)


# --- Product creation (simulation) ---
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # simulate creation by appending to in-memory list
            new_id = str(len(Product.products) + 1)
            Product.products.append({
                "id": new_id,
                "name": data['name'],
                "description": data.get('description', ''),
                "price": data['price']
            })
            # Render a created confirmation page
            viewData = {
                "title": "Product created",
                "subtitle": "Product created",
                "product": {"id": new_id, "name": data['name'], "price": data['price']}
            }
            return render(request, 'products/created.html', viewData)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)