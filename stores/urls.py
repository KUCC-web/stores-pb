from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Store_id>/', views.product_list, name='product_list')
]
