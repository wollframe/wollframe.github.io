from django.urls import path
from .views import *


urlpatterns = [

    path('',index,  name='index'),
    path('detail/', index, name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('price/', price, name='price'),
    path('contacts/', contacts, name='contacts'),

]
