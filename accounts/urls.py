from django.urls import path
from . import views

urlpatterns = [
    # Placeholder views if not set up yet
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
