from django.urls import path
from django.contrib.auth import views as auth
from app import settings
from . import views as core_views

app_name = 'core'

urlpatterns = [

    path('', auth.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('home/', core_views.index, name='index'),


]