from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

app_name='login'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='todo_list:login'), name = 'logout'),
]
