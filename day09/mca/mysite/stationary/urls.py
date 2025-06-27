from django.urls import path
from.import views
urlpatterns = [
    path('maggi/',views.maggi,name='maggi'),
]