from django.shortcuts import render
from .forms import ContactForm

def showPage(request):
    f=ContactForm()
    return render(request,'show.html',{'form':f})




