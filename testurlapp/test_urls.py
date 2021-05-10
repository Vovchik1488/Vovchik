from django.urls import path
from testurlapp import views

urlpatterns = [
    path('user/(\d+)/', views.home, name='home'),
    #site.com/user/12
]