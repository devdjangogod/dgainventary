from django.shortcuts import redirect
from django.contrib import messages

def roles_permitidos(*roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            if request.user.groups.filter(name__in=roles).exists():
                return view_func(request, *args, **kwargs)

            messages.error(request, "No tienes permiso para acceder a esta sección.")
            return redirect('dashboard')

        return wrapper
    return decorator