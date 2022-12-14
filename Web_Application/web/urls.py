from django.urls import path

from Web_Application.web.views import Checkout, Store, Cart

urlpatterns = (
    path('', Store.as_view(), name='store'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('cart/', Cart.as_view(), name='cart'),
)
