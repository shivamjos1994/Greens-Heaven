from django.urls import path
from .views import add_cart, cart, sub_cart
from shop.views import showcategories

urlpatterns = [
         path('cart/', cart, name="cart"),
         path('add_cart/<int:product_id>', add_cart, name="add_cart"),
         path('sub_cart/<int:product_id>', sub_cart, name="sub_cart"),
         path('product_detail/',showcategories,name="shopping"),

]