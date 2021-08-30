from django.urls import path
from .views import *
from . import views
app_name= 'enroll'
urlpatterns = [
    path('', EnrollView.as_view(), name='enroll'),
    path('1', EnrollView2.as_view(), name='index'),
    path('thanks/', views.ThanksView, name='thanks')
]
