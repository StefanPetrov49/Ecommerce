from django.urls import path

from Web_Application.web.views import checkout, store, cart, update_item, details_item, login_view, register_view, \
    logout_view, details_profile, edit_profile, delete_profile, private_view

urlpatterns = (
    path('', store, name='store'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update item'),
    path('item/details/<int:product_id>', details_item, name='details item'),
    path('login/', login_view, name='login view'),
    path('register/', register_view, name='register view'),
    path('logout/', logout_view, name='logout view'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('private/', private_view, name='private view'),

)
