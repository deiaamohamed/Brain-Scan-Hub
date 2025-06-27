from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('Doctor_dashboard/',views.doctor_dashboard,name='Doctor_dashboard'),
    path('mri_analysis',views.mri_analysis,name='mri_analysis'),
    path('patient_data' ,views.patient_data,name='patient_data'),
    path('contact_div',views.contact_dev,name='contact_dev'),
    path('issue-submitted/', views.issue_submitted_success, name='issue_submitted'),
    path('Admin_dashboard/',views.admin_dashboard,name='Admin_dashboard'),
    path('signup/',views.signup,name='signup'),
    path('logout',views.logoutpage,name='logout'),
    path('mri/result/<int:mri_id>/', views.view_result, name='view_result'), # added by me
    path('analysis_result/<int:mri_id>/', views.analysis_result, name='analysis_result'),
    path('send_report_email/<int:mri_id>/', views.send_report_email, name='send_report_email'),
] 