from django.shortcuts import render
from phones.models import Phone
from django.http import HttpResponse


def show_catalog(request):
    phone = Phone.objects.all()
    str_phone = ", ".join(phone)
    return HttpResponse(str_phone)



    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
