from django.urls import path
from . import views

urlpatterns=[
    path("login",views.loginUser,name="Login"),
    path("logout",views.logOut,name="Logout"),
    path("signup",views.signup,name="Signup"),
    path('',views.index,name='index'),
    path('manage',views.manage,name='manage'),
    path('result',views.result),
    path('add_result',views.add_result),
    path('view',views.view,name="view"),
    path("invoice<str:pk>",views.invoice,name="invoice"),
    path("delete_result<str:num>",views.delete_result,name="delete_result"),
    path("view_result",views.view_result,name="View Result"),
    path("delete<str:pk>",views.delete,name="delete"),
    path("deletestud/<str:pk>",views.delete_stud,name="deletestud"),
    path("deleteres/<str:num>",views.delete_res,name="deleteres"),
    path("search",views.search_res,name="Search Result"),
    path("updatestud<str:pk>",views.update_stud,name="updatestud"),
    path("update<str:pk>",views.update,name="update"),
    path("update_result/<str:num>",views.update_result,name="update_result"),
    path("updateres/<str:num>",views.updateres,name="updateres"),
    


]