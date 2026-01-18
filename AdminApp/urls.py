from django.urls import path
from AdminApp import views
urlpatterns=[
    path('index_page/', views.index_page, name="index_page"),
    path('category_page/',views.category_page,name="category_page"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:c_id>/',views.edit_category,name="edit_category"),
    path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),
    path('update_category/<int:c_id>/', views.update_category, name="update_category"),
    #**********************************************************************************************#
    path('company_page/',views.company_page,name="company_page"),
    path('save_company/',views.save_company,name="save_company"),
    path('display_company/', views.display_company, name="display_company"),
    path('edit_company/<int:comp_id>/', views.edit_company, name="edit_company"),
    path('update_company/<int:comp_id>/', views.update_company, name="update_company"),
    path('delete_company/<int:comp_id>/', views.delete_company, name="delete_company"),
    #************************************************************************************************#
    path('job_page/',views.job_page,name="job_page"),
    path('save_job/',views.save_job,name="save_job"),
    path('display_job/', views.display_job, name="display_job"),
    path('edit_job/<int:job_id>/', views.edit_job, name="edit_job"),
    path('update_job/<int:job_id>/', views.update_job, name="update_job"),
    path('delete_job/<int:job_id>/', views.delete_job, name="delete_job"),
    #*************************************************************************************************#
    path('adminLogins/', views.adminLogins, name='adminLogins'),
    path('AdminLoginPage/', views.AdminLoginPage, name='AdminLoginPage'),
    path('AdminLogout/', views.AdminLogout, name='AdminLogout'),
    #**************************************************************************************************#
    path('contact_data/', views.contact_data, name="contact_data"),
    path('delete_contact_data/<int:cnt_id>/', views.delete_contact_data, name="delete_contact_data"),
    path('display_applied/', views.display_applied, name="display_applied")





    ]