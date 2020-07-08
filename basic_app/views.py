from django.shortcuts import render

# Create your views here.

context_dict = {'text':'hello world', 'num':100}

def index(request):
    return render(request, 'index.html', context_dict)

def relative(request):
    return render(request, 'basic_app/relative_url_page.html')

def other(request):
    return render(request, 'basic_app/other.html')
