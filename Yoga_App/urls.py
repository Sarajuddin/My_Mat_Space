from django.urls import path
from Yoga_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('get-register-data/', views.getRegisterData, name='getRegisterData'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    # path('dashboard/beginner/', views.beginner, name='beginner'),
    # path('dashboard/intermediate/', views.intermediate, name='intermediate'),
    # path('dashboard/advanced/', views.advanced, name='advanced'),
    # path('dashboard/courses/', views.courses, name='courses'),
    path('dashboard/help/', views.help, name='help'),
    path('dashboard/contact/', views.contact, name='contact'),
    path('home/yoga-poses/', views.yogaPoses, name='yogaPoses'),
    path('home/yoga-for-women/', views.yogaForWomen, name='yogaForWomen'),
    path('home/yoga-for-men/', views.yogaForMen, name='yogaForMen'),
    path('home/profile/', views.profile, name='profile'),
    path('home/about/', views.about, name='aboutus'),
]