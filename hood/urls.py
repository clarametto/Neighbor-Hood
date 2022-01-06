from django.contrib import admin
from django.urls import path
from hood import views

urlpatterns=[
    path("", views.index, name="index"),
    path('profile/<pk>',views.profile, name = 'profile'),
#     path('update_profile/<int:id>',views.update_picture, name='update_profile'),
#     path('project/', views.upload_project, name = "upload"),
#     path('search/', views.search, name='search'),
#     path("project/<int:project_id>/", views.project_details, name="project_details"),
#     path("rate/<int:id>",views.rate, name='rate'), 
# 
   path('create_profile',views.update_profile, name='update_profile'),
]

