from django.urls import path
from .views import register_view, login_view, dashboard_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),  # Page d'inscription
    path('login/', login_view, name='login'),  # Page de connexion
    path('logout/', logout_view, name='logout'),  # Déconnexion
    path('dashboard/', dashboard_view, name='dashboard'),  # Tableau de bord après connexion
]
