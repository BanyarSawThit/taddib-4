from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Table, Category, Item,  Customization, UserOrder, OrderItem

def table_select(request):
    vtables = Table.objects.all()
    return render(request, 'order/table_selection.html', {'tables': vtables})
def menu_page(request, table_id):
    menu_items = Item.objects.all()
    return render(request, 'order/menu_page.html', {'menu_items': menu_items, 'table_id': table_id})

# def customization_page(request, table_id, pk):
#     menu_list = get_object_or_404(Item, pk=pk)
#     return render(request, 'order/customization_page.html', {'menu_list': menu_list})

def customization_page(request, table_id, item_id):


    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'order/customization_page.html', {'item':item,  'table_id': table_id})