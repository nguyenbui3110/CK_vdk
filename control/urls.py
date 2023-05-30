from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('update-status/', views.update_status, name='update_status'),
    path('update-mode/', views.update_mode, name='mode'),
    path('fetch-data/', views.fetch_data, name='fetch_data'),
]