from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_select, name='table_select'),
    path('table/<int:table_id>/', views.menu_page, name='menu_page'),
    path("table/<int:table_id>/item/<int:item_id>", views.customization_page, name="customization_page"),
]