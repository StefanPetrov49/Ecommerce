from django.http import HttpResponse
from django.shortcuts import redirect


def admin_only(func):
    def wrapper(request, *args, **kwargs):
        group = None
        try:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
        except:
            return redirect('store')

        if group == 'customer':
            return redirect('store')

        if group == 'superadmin':
            return redirect('private view')

        if group == 'admin':
            return redirect('private view')

    return wrapper
