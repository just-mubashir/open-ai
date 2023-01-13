from django.shortcuts import render


# Create your views here.

def api_home(request):
    return render(request, 'api.html')
