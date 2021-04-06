from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . models import *

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.user_login, name="login"),
    path('register', views.user_register, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('Grocery', views.Grocery, name="Grocery"),
    path('Dress', views.Dress, name="Dress"),
    path('Electronics', views.Electronics, name="Electronics"),

    path('profile', views.userProfile, name="profile"),
    path('profileedit', views.profileedit, name="profileedit"),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
