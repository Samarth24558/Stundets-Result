from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('header_footer',views.header_footer,name='header_footer')
]