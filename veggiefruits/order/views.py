from django.shortcuts import render, redirect
from .forms import CheckoutForm


# Create your views here.
def checkout(request):
    fm = CheckoutForm()
    if request.method == "POST":
        fm = CheckoutForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = CheckoutForm()
    return render(request, 'checkout.html',{'form':fm})