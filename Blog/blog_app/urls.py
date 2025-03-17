from django.urls import path,include
from . views import *

urlpatterns = [

    path('', home,name="home"),
    path('register/', register,name="register"),
    path('login/', login_user,name="login_user"),
    path('test/', test,name="test"),
    path('logout/', logout_user,name="logout_user"),
    path('add_post/', user_post,name="add_post"),
    path('edit_post/', edit_post,name="edit_post"),
    path('delete_post/', delete_post,name="delete_post"),
    path('change-password/', change_password,name="change_password"),
    path('forgot-password/', forgot_password,name="forgot_password"),
    path('forgot-password-sent/<str:uid>/<str:token>/', forgot_password_send,name="forgot_password_send"),
]
