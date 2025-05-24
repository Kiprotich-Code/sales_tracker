from django.shortcuts import render
from main.models import Item

# Create your views here.
def dashboard(request):
    products = Item.objects.filter(category='product')
    services = Item.objects.filter(category='service')

    context = {
        'products': products,
        'services': services,
    }
    return render(request, 'dashboard.html',context)