from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Item, Rim, Print
from .forms import ItemForm

# Create your views here.
def home(request):
    return render(request, 'main.html')


# ADD ITEM 
class AddItemView(CreateView):
    form_class = ItemForm
    model = Item
    success_url = '/'
    template_name = 'items/add_item.html'


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'items/items.html'

# CRUD RIM 

# CRUD PRINTS