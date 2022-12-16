from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('view', views.view, name='view'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvd/<int:pk>/', views.TaskDview.as_view(), name='cbvd'),
   # path('details', views.details, name='details'),
    path('cbvu/<int:pk>/', views.updatwview.as_view(), name='cbvu'),
    path('cbvu/<int:pk>/view', views.view, name='cbvu'),
    path('cbvu/<int:pk>/registration', views.view, name='cbvu'),
    path('cbvu/<int:pk>/login', views.add, name='cbvu'),
    path('cbvu/<int:pk>/logout', views.view, name='cbvu'),
    path('cbvde/<int:pk>/', views.Deleteview.as_view(), name='cbvde'),
]
