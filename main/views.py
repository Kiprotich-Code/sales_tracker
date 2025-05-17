from django.shortcuts import render, get_object_or_404
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
    success_url = reverse_lazy('items')


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
    success_url = reverse_lazy('rims')


class RimUpdateView(UpdateView):
    model = Rim
    form_class = RimForm
    template_name = 'rims/rim_form.html'
    success_url = reverse_lazy('rims')


class RimDeleteView(DeleteView):
    model = Rim
    context_object_name = 'rim'
    template_name = 'rims/rim_confirm_delete.html'
    success_url = reverse_lazy('rims')


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
    fields = ['qnty', 'amount', ]
    template_name = 'prints/print_form.html'
    success_url = reverse_lazy('print-list')

    def dispatch(self, request, *args, **kwargs):
        self.rim = get_object_or_404(Rim, id=self.kwargs['rim_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.rim = self.rim
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rim'] = self.rim
        return context


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