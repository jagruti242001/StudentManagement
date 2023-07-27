from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_view, name = "home"),
    path("signin/", views.signin_view, name = "signin"),
    path('signout/',views.signout_view , name = 'signout'),
    path('staffDetails/',views.staffDetails_view , name = 'staffDetails'),
    path('studentDetails/', views.studentDetails_view , name = 'studentDetails'),
    path('students/<int:id>',views.students_view , name = 'students'),
    path('staff/<int:id>',views.staff_view , name = 'staff'),
    path('fees/',views.fees_view , name = 'fees'),
    path('feedback/',views.feedback_view , name='feedback'),
    path('adminlogin/' , views.adminlogin_view , name = 'adminlogin'),
    path("contactus/", views.contactus_view, name = "contactus"),
    path('aboutus/' , views.aboutus , name = 'aboutus'),
    path('leave/' , views.leave , name = 'leave' ),
    path('deletestudent/<int:id>' , views.deletestudent , name='deletestudent'),



    # student urls
    path('register/',views.register_view , name = 'register'),
    path('registration/', views.registration.as_view() , name = 'registration'),
    path('studentHome/' , views.studentHome_view , name = 'studentHome'),
    path("update/<int:id>", views.update_view, name = "update"),
    path('studentlogin/' , views.studentlogin , name = 'studentlogin'),
    # path('studentsignin/', views.studentsignin , name = 'studentsignin'),
    path('studentprofile/<int:id>', views.studentprofile , name = 'studentprofile'),
    path('studentfeedback/' , views.studentfeedback, name = 'studentfeedback'),
    path('studentleave/' , views.studentleave , name = 'studentleave'),

    #Staff urls
    path('staffregistration/', views.staffregistration.as_view() , name = 'staffregistration'),
    path('staff_signin/',views.staff_signin_view ,name='staff_signin'),
    path('staffhome/' , views.staffhome_view , name = 'staffhome'),
    path("staffupdate/<int:id>", views.staffupdate_view, name = "staffupdate"),
    path('stafflogin/' , views.stafflogin , name = 'stafflogin'),
    path('staffprofile/<int:id>', views.staffprofile , name = 'staffprofile'),
    


]