from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout, name="logout_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', auctions, name="auctions_url"),
    path('auction_add', auction_add, name="auction_add_url"),
    path('products', products, name="products_url"),
    path('product_add', product_add, name="product_add_url"),
    path('product_delete/<int:product_id>', product_delete, name="product_delete_url"),
    path('product_edit/<int:product_id>', product_edit, name="product_edit_url"),
    path('farms', farms, name="farms_url"),
    path('farm_add', farm_add, name="farm_add_url"),
    path('account/<int:user_id>', account, name="account_url"),
    ]