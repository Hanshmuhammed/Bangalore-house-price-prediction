from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
                path('api/', include(router.urls)),
                path('', views.price_prediction, name='price_prediction'),
                path('signup/', views.signup, name='signup'),
                path('login/', views.login_view, name='login'),
                path('logout/', views.logout_view, name='logout'),
                path('dashboard/', views.dashboard, name='dashboard'),
                path('download-report/', views.download_report, name='download_report'),
                path('history/', views.history, name='history'),
              ]