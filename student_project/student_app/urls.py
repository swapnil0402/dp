from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form_page, name='form_page'),
    path('display/', views.display_page, name='display_page'),
    path('api/students/', views.student_list, name='student_list'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student')
]
