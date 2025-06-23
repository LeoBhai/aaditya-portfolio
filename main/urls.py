from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),  # ✅ add this
]
