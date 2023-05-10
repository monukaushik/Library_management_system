from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('forgotusername/',views.forgotusername,name='forgotusername'),
    path('forgototp/',views.forgototp,name='forgototp'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('deshboard/',views.deshboard,name='deshboard'),
    path('custom_admin/',views.custom_admin,name='custom_admin'),
    path('allstudent/',views.allstudent,name='allstudent'),
    path('adminbooksummary/',views.adminbooksummary,name='adminbooksummary'),
    path('addnewbook/',views.addnewbook,name='addnewbook'),
    path('notification/',views.notification,name='notification'),
    path('Notification2/<int:id>/',views.Notification2, name='Notification2'),
    path('bookissurreq/<int:id>/', views.bookissurreq,name='bookissurreq'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('bookissuedsumadmin/',views.bookissuedsumadmin,name='bookissuedsumadmin'),
    path('bookissuedetailstu/',views.bookissuedetailstu,name='bookissuedetailstu'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]
