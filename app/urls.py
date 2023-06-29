from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('hello/', views.hello),
    path('', views.register, name='register') ,
    path('profile/', views.profile, name='profile'),
    path('login/', views.LoginView.as_view() , name="login"),

]
