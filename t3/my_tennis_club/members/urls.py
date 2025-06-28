from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members, name='members'),
    path('print-pdf/', views.pdf_view, name='print_pdf'),
]