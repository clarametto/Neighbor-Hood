from django.contrib import admin
from django.urls import path
from hood import views

urlpatterns=[
    path("", views.index, name="index"),
    path('create_profile',views.create_profile, name='create_profile'),
    path('profile/',views.profile,name = 'profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hoods, name = 'hood'),
    # path('hood/<str:name>',views.single_hood,name='single_hood'),

]

