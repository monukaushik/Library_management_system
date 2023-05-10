from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random
from .models import *
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')


        if password == cpassword:
            User = get_user_model()
            user=User.objects.create_user(email=email,password=password)
            user.save()
            return redirect('/signin/')  
    return render(request,'signup.html')     

def signin(request):
    if request.method=='POST':
        email=request.POST.get('useremail')
        password=request.POST.get('password')

        user=authenticate(request,email=email,password=password)
        if user is None:
            return render(request,'signin.html')
        auth.login(request,user)
        return (
            redirect('/custom_admin/')
            if user.is_superuser
            else redirect('/deshboard/')
        )
    return render(request,'signin.html')  


def forgotusername(request):
    if request.method != 'POST':
        return render(request,'forgotusername.html' )
    User = get_user_model()
    useremail=request.POST.get('useremail')
    useremail2=User.objects.get(email= useremail)

    if useremail2 is None:
        return render(request,'forgotusername.html' )
    otp=random.randint(1,10000)
    request.session['otp']=otp
    request.session['email']=useremail

    subject = 'OTP for reset password'
    message = """otp :%d
                      """ %otp
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [useremail2, ]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/forgototp/')


def forgototp(request):
    if request.method=='POST':
        otp=int(request.POST.get('otp'))

        if (otp==int(request.session.get('otp'))):
            return redirect('/forgotpassword/')  
        else:
            return render(request,'forgototp.html' )
    return render(request,'forgototp.html' )

def forgotpassword(request):
    if request.method != 'POST':
        return render(request,'forgotpassword.html' )
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    if password != cpassword:
        return render(request,'forgotpassword.html' )
    User = get_user_model()
    user=User.objects.get(email=request.session.get('email'))
    user.set_password(password)
    user.save()
    return redirect('/signin/')


def profile(request):
    User = get_user_model()
    data=User.objects.filter(email=request.user.email).first()
    username=data.username
    useremail=data.email
    studentimg=data.studentimg
    studentbranch=data.studentbranch
    studentrollno=data.studentrollno
    studentadd1=data.studentadd1
        
    context={
        'username':username,
        'useremail':useremail,
        'studentimg':studentimg,
        'studentbranch':studentbranch,
        'studentrollno':studentrollno,
        'studentadd1':studentadd1,
    }   
    if request.method=='POST':
        data.username=request.POST.get('username')
        data.studentimg=request.FILES.get('userimage')
        data.studentbranch=request.POST.get('stuclass')
        data.studentrollno=request.POST.get('sturoll')
        data.studentadd1=request.POST.get('address1')
        data.save()
        return redirect('/deshboard/')
    return render(request,'profile.html',context)

def delete(request,id):
    data=bookdetail.objects.filter(bookid=id)
    data.delete()
    return redirect('/adminbooksummary/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def deshboard(request):
    if request.method=='POST':
        enterclass=request.POST.get('class1')
        all_book=bookdetail.objects.filter(branch=enterclass)
        return render(request,'deshboard.html',{'all':all_book})
    return render(request,'deshboard.html')

def bookissurreq(request,id):
    if username := request.user.username:
        data=Userdetail.objects.filter(username=username)
        for i in data:
            studentbranch=i.studentbranch
            studentrollno=i.studentrollno
        bookdetail.objects.filter(bookid=id).update(stuname=username,sturollno=studentrollno,requiredqty=1,status='pending')
        return redirect('/deshboard/')
    return render(request,'deshboard.html')

def bookissuedsumadmin(request):
    data3=bookdetail.objects.filter(status='completed')
    return render(request,'bookissuedsumadmin.html',{'data3':data3})

def bookissuedetailstu(request):
    username=request.user.username
    alldata=bookdetail.objects.all().filter(stuname=username,status='completed')
    return render(request,'bookissuedetailstu.html',{'alldata':alldata})

def custom_admin(request):
    return render(request,'custom_admin.html')

def allstudent(request):
    all_data=Userdetail.objects.filter(is_superuser=0)
    return render(request,'allstudent.html',{'all_data':all_data})

def adminbooksummary(request):
    if request.method=='POST':
        enterclass=request.POST.get('class')
        all_book=bookdetail.objects.filter(branch=enterclass)
        return render(request,'adminbooksummary.html',{'all':all_book})
    return render(request,'adminbooksummary.html')

def addnewbook(request):
    if request.method != 'POST':
        return render(request,'addnewbook.html')
    bookname=request.POST.get('bookname')
    bookimage=request.FILES.get('bookimage')
    bookauthor=request.POST.get('bookauthor')
    branch=request.POST.get('branch')
    price=request.POST.get('price')
    bqty=request.POST.get('bqty')

    book_entered=bookdetail.objects.create(bookname=bookname,bookimage=bookimage,bookauthor=bookauthor,branch=branch,price=price,Qty=bqty)
    book_entered.save()
    return redirect('/adminbooksummary/')

def notification(request):
    request_data=bookdetail.objects.all().filter(status='pending')
    return render(request,'notification.html',{ 'request_data':request_data})
    

def Notification2(request,id):  
    today = date.today()
    if data := bookdetail.objects.all().filter(bookid=id):
        for i in data:
            totalqty=i.Qty
            requestqty=i.requiredqty
            updatedqty=totalqty-requestqty
    bookdetail.objects.filter(bookid=id).update(
        status='completed', issuedate=today, Qty=updatedqty
    )
    return redirect('/bookissuedsumadmin/')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
