# accounts/urls.py
from django.urls import path
from .views import register_user, login_user, get_user, supabase_register_user, supabase_login_user, supabase_oauth_login, refresh_token

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('refresh/', refresh_token, name='refresh_token'),
    path('supabase/register/', supabase_register_user, name='supabase_register_user'),
    path('supabase/login/', supabase_login_user, name='supabase_login_user'),
    path('account/<slug:username>/', get_user, name='get_user'),
    path('supabase/oauth-login/', supabase_oauth_login, name='supabase_oauth_login'),
]