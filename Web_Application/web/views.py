from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from Web_Application.web.models import Product


# Create your views here.

class Store(TemplateView):
    model = Product
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_list'] = Product.objects.all()
        return context


class Cart(TemplateView):
    template_name = 'cart.html'


class Checkout(TemplateView):
    template_name = 'checkout.html'
