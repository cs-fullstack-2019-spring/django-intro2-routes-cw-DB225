from django.urls import path

from . import views

# Paths for each request
urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood/', views.thegood, name='index'),
    path('happyhappyjoyjoy/', views.happy, name='index'),

    # Challenge path
    path('string/text/', views.string, name='index'),
]