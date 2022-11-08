from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.say_firstapp_hello),
    path('',views.say_home_firstapp_hello,name='home'),
    path('detail/<int:name_id>/<slug>',views.detail,name='details'),
    path('delete/<int:name_id>',views.delete,name='delete'),
    path('form/user',views.creatUserForm,name='userForm'),
    path('updateUser/<int:user_id>',views.updateUser,name='updateUser'),

]