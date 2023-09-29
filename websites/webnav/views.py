from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''<h1>Website Navigator</h1>
    <h4>Google</h4>
    <a href="http://www.google.com/">Google</a>
    <h4>Facebook</h4>
    <a href="http://www.facebook.com">Facebook</a>
    <h4>Flipkart</h4>
    <a href="http://www.flipkart.com">Flipkart</a>
    <h4>Amazon</h4>
    <a href="http://www.amazon.com">Amazon</a>
    ''')
