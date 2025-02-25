from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Table, Category, Item, Customization, UserOrder, OrderItem


def table_select(request):
    vtables = Table.objects.all()
    return render(request, 'order/table_selection.html', {'tables': vtables})


def menu_page(request, table_id):
    # Fetch all categories
    categories = Category.objects.all()
    # Fetch the selected category if available
    selected_category = request.GET.get('category', None)
    if selected_category:
        # Filter items by the selected category
        menu_items = Item.objects.filter(category_id=selected_category)
    else:
        # If no category is selected, show all items
        menu_items = Item.objects.all()
    # Pass categories and selected category to the template
    return render(request, 'order/menu_page.html', {
        'menu_items': menu_items,
        'categories': categories,
        'table_id': table_id,
        'selected_category': selected_category
    })
    menu_items = Item.objects.all()
    return render(request, 'order/menu_page.html', {'menu_items': menu_items, 'table_id': table_id})


# def customization_page(request, table_id, pk):
#     menu_list = get_object_or_404(Item, pk=pk)
#     return render(request, 'order/customization_page.html', {'menu_list': menu_list})

def customization_page(request, table_id, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'order/customization_page.html', {'item': item, 'table_id': table_id})