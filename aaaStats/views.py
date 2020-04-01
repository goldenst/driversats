from django.shortcuts import render

# Create your views here.

def home_view(request):
  context = {
    'home': 'Home Page'
  }
  return render(request, 'base/home.html', context)