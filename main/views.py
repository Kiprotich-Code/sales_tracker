from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Item, Rim, Print
from .forms import ItemForm, RimForm, PrintForm
from django.urls import reverse_lazy
from django.db.models import Sum, F, FloatField
from django.db.models.functions import Cast
from collections import defaultdict
from django.utils.timezone import localtime

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


class ItemDeleteView(DeleteView):
    model = Item
    context_object_name = 'item'
    template_name = 'items/item_confirm_delete.html'
    success_url = reverse_lazy('items')


# CRUD RIM 
class RimListView(ListView):
    model = Rim
    context_object_name = 'rims'
    template_name = 'rims/rim_list.html'

    def get_queryset(self):
        rims = Rim.objects.all().prefetch_related('prints', 'item')
        for rim in rims:
            total_amount = rim.prints.aggregate(total=Sum('amount'))['total'] or 0
            rim.total_prints = total_amount // 10
            rim.deviation = rim.total_prints - 500
        return rims


class RimDetailView(DetailView):
    model = Rim
    context_object_name = 'rim'
    template_name = 'rims/rim_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prints'] = self.object.prints.all().order_by('-id')  # latest first
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouped_prints = defaultdict(list)

        prints = Print.objects.select_related('rim__item').order_by('-id')

        for print_obj in prints:
            local_date = localtime(print_obj.rim.added_on).date()
            grouped_prints[local_date].append(print_obj)

        # Sort by date descending
        context['grouped_prints'] = dict(sorted(grouped_prints.items(), reverse=True))
        return context


class PrintDetailView(DetailView):
    model = Print
    context_object_name = 'print'
    template_name = 'prints/print_detail.html'



class PrintCreateView(CreateView):
    model = Print
    fields = ['qnty', 'amount']
    template_name = 'prints/print_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.rim = get_object_or_404(Rim, id=self.kwargs['rim_id'])
        self.next_url = request.META.get('HTTP_REFERER')  # Save the previous page
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.rim = self.rim
        self.object = form.save()
        return redirect(self.next_url or 'print-list')  # fallback to print-list if no referrer

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