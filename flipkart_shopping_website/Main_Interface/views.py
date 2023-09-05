from django.shortcuts import render, HttpResponse
from django.template import loader
from Main_Interface.models import LoginForm

# Create your views here.

def Flipkart(request):
    return render(request, 'main_page.html')
    
def login(request):
    return render(request, 'main_page.html')

# def SaveDetails(request):
    # print("request111" , request.method)
    # if request.method == 'POST':
    #     print("request.POST = ", request.POST)
    #     print("name = ", request.POST.get('name'))
    #     name = request.POST.get('name')
    #     print("name2 = ", name1)
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     detail = LoginForm(user=email, password=password, name=name)
    #     detail.save()


    # print("request333 = ", request.GET)
    # if request.method == 'GET':
    #     print("request.GET = ", request.GET)
    #     print("name = ", request.GET.get('name'))
    #     name = request.GET.get('name')
    #     print("name2 = ", name)
    #     print("name object= ", name.objects.email())
    #     print("name object= ", name.objects.password())
    #     email = name.objects.email()
    #     password = name.objects.password()
    # return render('main_page.html', name, email, password)

def fetchdetails(request):
    login = LoginForm.objects.all()
    context = {
        "login" : login,
    }
    print("context = " , context)
    return render(request, 'CRUD.html', context)
