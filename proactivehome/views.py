from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def index(request):

            

    return render(request,"index.html")