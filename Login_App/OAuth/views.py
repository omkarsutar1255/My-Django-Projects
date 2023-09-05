from django.shortcuts import render, HttpResponse, redirect
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.response import Response

# Create your views here.
def index(request):
    print('TXN 1')
    CLIENT_ID = '862176511370-jc4jqldb9vkveteroa3jlulo8ohe92a7.apps.googleusercontent.com'
    token = request.data.get('id_token')
    # token = 'b7be25f0-0f21-420e-bb07-481997239ba1'
    # name = request.GET.get("name")
    # email = request.GET.get("email")
    # picture = request.GET.get("picture")
    # sub = request.GET.get("sub")
    # userRole = request.GET.get("userRole")
    # iat = request.GET.get("iat")
    # exp = request.GET.get("exp")
    # jti = request.GET.get("jti")
    print("Token value = ", token)
    
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        print('userid = ', idinfo['sub'])
        userid = idinfo['sub']
        return Response(idinfo)
        # redirect('/loggeed')

    except ValueError as e:
        # Invalid token
        return HttpResponse("Error Occured")

def logged(request):
    return render(request, 'logged.html')