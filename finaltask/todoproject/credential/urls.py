from . import views
from django.urls import path,include


urlpatterns = [

    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
     path('home',views.add,name='home'),
     path('cbv/', views.Taskview.as_view(), name='cbv'),

    ]


