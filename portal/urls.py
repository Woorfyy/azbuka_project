from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('furniture/', views.furniture, name='furniture'),
]
