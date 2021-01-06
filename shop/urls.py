from django.urls import path
from .views import product_list, product_detail, contact_us

app_name = 'shop'

urlpatterns = [
    path('contact/', contact_us, name='contact_us'),
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),

]


