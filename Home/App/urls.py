from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('manage',views.manage,name='manage'),
    path('result',views.result),
    path('add_result',views.add_result),
    path('view',views.view)
]