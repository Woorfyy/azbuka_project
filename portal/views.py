from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Mebel




def index(request):
    error_login = None
    form = RegistrationForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')
        elif 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                error_login = 'Неверный логин или пароль'
    context = {
        'form': form,
        'error_login': error_login,
    }
    return render(request, 'portal/index.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def products(request):
    return render(request, 'portal/products.html')
def about_us(request):
    return render (
        request,
        'portal/about_us.html'
    )

def contact(request):
    return render (
        request,
        'portal/contact.html'
    )

def furniture(request):
    category_filter = request.GET.get('category')
    availability_filter = request.GET.get('availability')
    mebels = Mebel.objects.all()
    if category_filter in ['Д', 'КХ', 'Ш', 'КР', 'С']:
        mebels = mebels.filter(category=category_filter)
    if availability_filter in ['Е', 'Н']:
        mebels = mebels.filter(availability=availability_filter)
    return render(
        request,
        'portal/furniture.html',
        {'mebels': mebels}
    )
