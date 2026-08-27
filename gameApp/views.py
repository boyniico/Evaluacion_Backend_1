from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request, 'main.html')

def detail(request):
    return render(request, )