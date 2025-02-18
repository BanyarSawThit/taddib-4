from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path("order/<int:table_number>/customization_page/", views.customization_page, name="customization_page"),
]