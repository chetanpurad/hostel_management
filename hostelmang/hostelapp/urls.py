from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.home,name='home'),
    path('studentlogin/',views.student_login,name='studentlogin'),
    path('application/',views.application,name='application'),
    path('wardenlogin/',views.warden_login,name='wardenlogin'),
    path('adminlogin',views.admin_login,name='adminlogin'),
    path('addhostel',views.addhostel,name='addhostel'),
    path('viewhostel',views.viewhostel,name='viewhostel'),
    path('edithostel/<int:hostel_id>/',views.edithostel,name='edithostel'),
    path('add_depar',views.add_depar,name='add_depar'),
    path('view_dep',views.view_dep,name='view_dep'),
    path('edit_dep/<int:dep_id>/',views.edit_dep,name='edit_dep'),
    path('add_warden',views.add_warden,name='add_warden'),
    path('view_warden',views.view_warden,name='view_warden'),
    path('edit_warden/<int:warden_id>/',views.edit_warden,name='edit_warden'),
    path('warden/delete/<int:warden_id>/',views. delete_warden, name='delete_warden'),
    path('add_gender',views.add_gender,name='add_gender'),
    path('add_course',views.add_course,name='add_course'),
    path('approve_application/<int:stud_id>/',views.approve_application,name='approve_application'),
    path('reject_application/<int:stud_id>/',views.reject_application,name='reject_application'),
    
    path('warden_dash/', views.warden_dash, name='warden_dash'),
    path('view_applications/<hostel_id>/', views.view_applications, name='view_applications'),
    path('room_allotment/<hostel_id>/', views.room_allotment, name='room_allotment'),
    path('room_allotment_success/', views.room_allotment_success, name='room_allotment_success'),
    path('check_status/', views.check_status, name='check_status'),
    path('payment/<int:student_id>/', views.payment, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('student_dashboard/<int:student_id>/', views.student_dashboard, name='student_dashboard'),
    path('hostel_details/<int:hostel_id>/', views.hostel_details, name='hostel_details'),
    path('hostel_details_page', views.hostel_details_page, name='hostel_details_page'),
    path('raise_complaint/', views.raise_complaint, name='raise_complaint'),
    path('pay_mess_bill/', views.pay_mess_bill, name='pay_mess_bill'),
    path('apply_fund/', views.apply_for_fund, name='apply_fund'),
    path('view_complaints/<hostel_id>/', views.view_complaints, name='view_complaints'),
    path('accept_complaint/<int:stud_id>/',views.accept_complaint,name='accept_complaint'),
    path('delete_dep/<int:dep_id>/', views.delete_department, name='delete_dep'),
    path('delete_warden/<int:warden_id>/', views.delete_warden, name='delete_warden'),
    path('delete_hostel/<int:hostel_id>/', views.delete_hostel, name='delete_hostel'),
    path('view_allocations/<hostel_id>/', views.view_allocations, name='view_allocations'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
]












urlpatterns += staticfiles_urlpatterns()

