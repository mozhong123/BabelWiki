from django.contrib import admin
from django.urls import path
from shujukeshe import views
from django.urls import include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),
    path('confirm/', views.user_confirm),
    path('user_homepage/', views.user_homepage),
    path('modify/', views.modify),
    path('repassword/', views.repassword),
    path('contact_us/', views.contact_us),
    path('', views.to_index),


]