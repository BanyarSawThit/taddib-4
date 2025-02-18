from django.shortcuts import render
from django.utils import timezone
from .models import Table, Category, Item,  Customization, UserOrder, OrderItem

def menu_list(request, table_number):
    menu_items = Item.objects.all()
    return render(request, 'order/menu_page.html', {'menu_items': menu_items, "table_number": table_number})