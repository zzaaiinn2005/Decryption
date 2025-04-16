from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    x ={'name':'zain hassn kaml',
        'age':20}
    
    return render(request, 'pages/index.html',x)
def about(request):
    return HttpResponse('about page')