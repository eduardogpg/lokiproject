from django.shortcuts import redirect

def admin_validator(method):
    def wrapper(request, *args, **kwargs):
        
        if request.user.is_authenticated and request.user.admin():
            return method(request, *args, **kwargs)
        else:
            return redirect('wallets:list')

    return wrapper