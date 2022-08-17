from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from .import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('login/',views.user_login),
    path('reg/',views.register),
    path('about/',views.about),
    path('bid/',views.bidding),
    path('fea/',views.features),
    path('data/',views.display),
    path('logout/',views.user_logout),
    path ('verifycode/',views.verificationcode),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]