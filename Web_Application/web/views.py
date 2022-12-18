import json

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Web_Application.web.decorators import admin_only
from Web_Application.web.forms import CreateUserForm, EditCustomerForm, DeleteCustomerForm, CreateCustomerForm, \
    CreateShippingAddress
from Web_Application.web.models import Product, Order, OrderItem
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# class Store(TemplateView):
#     model = Product
#     template_name = 'store.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products_list'] = Product.objects.all()
#         return context

@login_required(login_url='login view')
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
        }
        cart_items = order['get_cart_items']

    products = Product.objects.all()
    context = {"products": products,
               "cart_items": cart_items}
    return render(request, 'store.html', context)


@login_required(login_url='login view')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
        }
        cart_items = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login view')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
        }
        cart_items = order['get_cart_items']
    customer_form = CreateCustomerForm()
    if request.method == 'POST':
        customer_form = CreateCustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
    shipping_form = CreateShippingAddress()
    if request.method == 'POST':
        shipping_form = CreateShippingAddress(request.POST)
        if shipping_form.is_valid():
            shipping_form.save()
    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        'customer_form': customer_form,
        'shipping_form': shipping_form,
    }
    return render(request, 'checkout.html', context)


@login_required(login_url='login view')
def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


@login_required(login_url='login view')
def details_item(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'details-product.html', context)


@login_required(login_url='login view')
def details_profile(request):
    customer = request.user.customer
    context = {
        'customer': customer,
    }
    return render(request, 'details-profile.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')

    context = {
    }
    return render(request, 'login.html', context)


def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login view')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login view')


def edit_profile(request):
    customer = request.user.customer
    if request.method == 'GET':
        form = EditCustomerForm(instance=customer)
    else:
        form = EditCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,

    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    customer = request.user
    if request.method == 'POST':
        customer.delete()
        return redirect('login view')

    form = DeleteCustomerForm(instance=customer)

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


@admin_only
def private_view(request):
    pass
