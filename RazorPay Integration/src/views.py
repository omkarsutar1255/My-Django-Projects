from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import Coffee
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# @csrf_exempt
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        email = request.POST.get('email')
        client = razorpay.Client(auth=("rzp_test_TJDnCpeNr6synY", "rUFtB2K7f1aGk0ycVE6PabTT"))
        print("******************")
        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
        print('###################')
        coffee = Coffee(name=name, amount=amount, email=email, order_id=payment['id'])
        coffee.save()

        return render(request, 'index.html', {'payment': payment})
    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print("AAA = ", a)
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        print("#### order id = ", order_id)
        user = Coffee.objects.filter(order_id=order_id).first()
        print("** User = ", user)
        user.paid = True
        user.save()
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.html')
        send_mail("Your payment has been received", msg_plain, settings.EMAIL_HOST_USER,
                  [user.email], html_message=msg_html)

    return render(request, "success.html")
