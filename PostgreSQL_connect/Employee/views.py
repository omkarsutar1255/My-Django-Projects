from django.shortcuts import render
from .models import employee


# Create your views here.
def index(request):
    return render(request, 'index.html')


def save(request):
    print(request.method)
    if request.method == 'GET':
        email = request.GET.get('email')
        textarea = request.GET.get('textarea')
        print('data = ', email, textarea)
        Employee = employee.objects.create(Email=email, Text=textarea)
        Employee.save()
        print("inside save")
        emp = employee.objects.all()
        obj = {
            'emp': emp
        }
        print("bfr render : ", obj)
        return render(request, 'save.html', context=obj)
