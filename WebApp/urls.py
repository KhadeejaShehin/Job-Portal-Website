from django.urls import path
from WebApp import views

urlpatterns=[
    path('Index/',views.Index,name="Index"),
    path('about_page/', views.about_page, name="about_page"),
    path('jobs_page/',views.jobs_page,name="jobs_page"),
    path('contact/', views.contact, name="contact"),
    path('Save_contact_details/', views.save_contact_details, name="Save_contact_details"),
    path('Filtered_items/<str:cat_name>/', views.Filtered_items, name='Filtered_items'),
    path('single_item/<int:item_id>/', views.single_item, name="single_item"),
    path('', views.sign_in, name="sign_in"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('save_signup/', views.save_signup, name="save_signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('save_applied/',views.save_applied,name="save_applied"),
    path('applied_page/',views.applied_page,name="applied_page"),
    path('delete_applied/<int:applied_id>/', views.delete_applied, name="delete_applied"),
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),


]