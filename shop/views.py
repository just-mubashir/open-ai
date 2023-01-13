from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'message': 'Welcome to my website'}
    return render(request, 'home.html',context=context)
