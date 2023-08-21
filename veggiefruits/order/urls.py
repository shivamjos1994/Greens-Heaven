from django.contrib import admin
from django.urls import path
from .views import checkout

urlpatterns = [
          path('admin/', admin.site.urls),
          path('checkout/', checkout, name="checkout")

]