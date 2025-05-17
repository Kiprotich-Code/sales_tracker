from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Item, Rim, Print
from .forms import ItemForm, RimForm, PrintForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'main.html')


# ADD ITEM 
class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'items/items.html'


# class ItemDetailView(DetailView):
#     model = Item
#     context_object_name = 'item'
#     template_name = 'items/item_detail.html'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/item_form.html'
    success_url = reverse_lazy('item-list')


# class ItemUpdateView(UpdateView):
#     model = Item
#     form_class = ItemForm
#     template_name = 'items/item_form.html'
#     success_url = reverse_lazy('item-list')


# class ItemDeleteView(DeleteView):
#     model = Item
#     context_object_name = 'item'
#     template_name = 'items/item_confirm_delete.html'
#     success_url = reverse_lazy('item-list')


# CRUD RIM 
class RimListView(ListView):
    model = Rim
    context_object_name = 'rims'
    template_name = 'rims/rim_list.html'


class RimDetailView(DetailView):
    model = Rim
    context_object_name = 'rim'
    template_name = 'rims/rim_detail.html'


class RimCreateView(CreateView):
    model = Rim
    form_class = RimForm
    template_name = 'rims/rim_form.html'
    success_url = reverse_lazy('rim-list')


class RimUpdateView(UpdateView):
    model = Rim
    form_class = RimForm
    template_name = 'rims/rim_form.html'
    success_url = reverse_lazy('rim-list')


class RimDeleteView(DeleteView):
    model = Rim
    context_object_name = 'rim'
    template_name = 'rims/rim_confirm_delete.html'
    success_url = reverse_lazy('rim-list')


# CRUD PRINTS
class PrintListView(ListView):
    model = Print
    context_object_name = 'prints'
    template_name = 'prints/print_list.html'


class PrintDetailView(DetailView):
    model = Print
    context_object_name = 'print'
    template_name = 'prints/print_detail.html'


class PrintCreateView(CreateView):
    model = Print
    form_class = PrintForm
    template_name = 'prints/print_form.html'
    success_url = reverse_lazy('print-list')


class PrintUpdateView(UpdateView):
    model = Print
    form_class = PrintForm
    template_name = 'prints/print_form.html'
    success_url = reverse_lazy('print-list')


class PrintDeleteView(DeleteView):
    model = Print
    context_object_name = 'print'
    template_name = 'prints/print_confirm_delete.html'
    success_url = reverse_lazy('print-list')