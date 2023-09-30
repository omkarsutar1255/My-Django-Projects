from django.shortcuts import render
from myproject.celery import add
from productapp.tasks import sub
from celery.result import AsyncResult
from django.http import HttpResponse

# Enqueue Task using delay()
# def index(request):
#     print("Results: ")
#     result1 = add.delay(10, 20)
#     print("Result 1: ", result1)
#     result2 = sub.delay(80, 10)
#     print("Result 2: ", result2)
#     return render(request, "productapp/home.html")

# # Enqueue Task using apply_async()
# def index(request):
#     print("Results: ")
#     result1 = add.apply_async(args=[10, 20])
#     print("Result 1: ", result1)
#     result2 = sub.apply_async(args=[80, 10])
#     print("Result 2: ", result2)
#     return render(request, "productapp/home.html")

# Display addition value after task execution
def index(request):
    result = add.delay(10, 30)
    # return render(request, "productapp/home.html", {'result':result})
    return HttpResponse("Hello world! ")

def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    # print("Ready: ", result.ready())
    # print("Successful: ", result.successful())
    # print("Failed: ", result.failed())
    # print("Get: ", result.get())
    return render(request, 'productapp/result.html', {'result':result})

def about(request):
    return render(request, 'productapp/about.html')

def contact(request):
    return render(request, 'productapp/contact.html')
