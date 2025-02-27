from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Table, Category, Item,  Customization, UserOrder, OrderItem
from .forms import CustomizationForm
def table_select(request):
    vtables = Table.objects.all()
    return render(request, 'order/table_selection.html', {'tables': vtables})
def menu_page(request, table_id):
    menu_items = Item.objects.all()
    return render(request, 'order/menu_page.html', {'menu_items': menu_items, 'table_id': table_id})

def customization_page(request, table_id, item_id):
    form = CustomizationForm()
    item = get_object_or_404(Item, pk=item_id)
    table = get_object_or_404(Table, pk=table_id)

    if request.method == 'POST':
        form = CustomizationForm(request.POST)
        if form.is_valid():
            customization = form.save(commit=False)
            customization.item = item
            customization.save()
            return render(request, 'order/customization_page.html', {'item':item, 'form': form, 'table_id': table_id})
        else:
            form = CustomizationForm()

    return render(request, 'order/customization_page.html', {'item':item, 'form': form, 'table_id': table_id})
