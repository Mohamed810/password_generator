from generator import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password),
    path('about/', views.about, name='about')
]

urlpatterns += staticfiles_urlpatterns()