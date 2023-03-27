from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import School, Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login


# Create your views here.

def home(request):
    return render(request, 'home.html')


def loggin(request):
    print("inside login")
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('action') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            print(username, password)
            # newpass = User.objects.filter(username=username)
            # print(newpass)
            # check_if_user_exists = User.objects.filter(username=username).exists()
            # print(check_if_user_exists)
            # if check_if_user_exists:
            #     user = authenticate(request, username=username, password=password)
            #     if user is not None:
            #         print("User is logged")
            #     else:
            #         print("User is None")
            # else:
            #     print("Not present in the table")
            # schoolvalidate = School.objects.filter(name=username, password=password1)
            # print(schoolvalidate)
            # if schoolvalidate:
            #     print("inside if")
            # else:
            #     print("inside else")
            # studentvalidate = Student.objects.filter(name=username, password=password1)
            # print(studentvalidate)
            # if schoolvalidate:
            #     print("inside if")
            # else:
            #     print("inside else")
            user = authenticate(username=username, password=password)
            print("before user isnot none", user)
            if user is not None:
                print("inside user is not none", user.is_active)
                if user.is_active:
                    login(request, user)
                    # messages.success(request, "Successfully Logged In")
                    print("rendering logged html")
                    studentobj = School.objects.all()
                    context = {
                      'student': studentobj
                    }
                    return render(request, 'student.html', context)
                else:
                    print("User is not active")
                    return redirect('/')
            else:
                print("User is None")
                return redirect('/')
        elif request.POST.get('action') == 'signup':
            print('inside signup render')
            return render(request, 'signup.html')
        else:
            print("error in direct")
    elif request.method == 'GET':
        print('It is a get method')
    else:
        HttpResponse("404- Not found")


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['emailid']
        city = request.POST['city']
        pincode = request.POST['pincode']
        password = request.POST['password']
        print("before validating signup details ", len(name))
        if len(name) < 5:
            print("comming here")
            # messages.error(request, " Your username must be under 10 characters")
            return redirect('signup')

        print("after validated signup page")
        user = User.objects.create_user(name, email, password)
        print("User1 = ", user)
        user.first_name = name
        print("User2 = ", user)
        user.save()
        # messages.success(request, " Your iCoder has been successfully created")

        userob = School(name=name, email=email, city=city, pincode=pincode, password=password)
        userob.save()
        # studentobj = School.objects.all()
        # context = {
        #     'student': studentobj
        # }
        # return render(request, 'student.html', context)
        return redirect('/')
    elif request.method == 'GET':
        return redirect('/')
    else:
        return HttpResponse("Error occured")


def student(request):
    print("student details ", request.method)
    if request.method == 'POST':
        if request.POST.get('action') == 'save':
            # Do some read table and provide data
            print(request.POST)
            name = request.POST.get('name1')
            username = request.POST.get('username')
            password = request.POST.get('password')
            id1 = request.POST.get('dropdown1')
            print("id = ", id1)
            school = School.objects.get(id=id1)
            print("reached", name, username, password, school)
            print("before validating student name")
            if len(name) < 8:
                # messages.error(request, " Your username must be under 10 characters")
                return HttpResponse("Name should be more than 10 charater")

            if not username.isalnum():
                # messages.error(request, " Username should only contain letters and numbers")
                return HttpResponse("Spaces and special charater not allowed in name")
            print("after validated student name")
            stu = Student(name=name, username=username, password=password, school=school)
            print("reached ", stu)
            stu.save()
            studentobj = School.objects.all()
            context = {
                'student': studentobj
            }
            return render(request, 'student.html', context)
        elif request.POST.get('action') == 'logout':
            logout(request)
            print("User logged out ")
            return redirect('/')
        else:
            print("error in direct")
    else:
        return HttpResponse("NOT GET request")
