from django.urls import path

from . import views

app_name = 'demo_home'
urlpatterns = [
    path('home/', views.display, name='display'),
    path('home/<int:id>/', views.conditions, name='conditions')
]
