from django.shortcuts import render

# Create your views here.

def pooru(request):
    d={'name':'narasimha'}
    return render(request,'pooru.html',context=d)
