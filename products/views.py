from django.shortcuts import render, HttpResponse
from .models import Products
# Create your views here.
def index(request):
    product = Products.objects.all()
    return render(request, "index.html", {"product": product})