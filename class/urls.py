from django.urls import path
from .views import *
from . import views
app_name= 'class'
urlpatterns = [
    path('', DisplayClass.as_view(), name='display_class')

]
