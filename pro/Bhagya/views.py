from django.shortcuts import render
from django.contrib import messages
from Bhagya.models import Contact
# Create your views here.
def Bhagya(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']    
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']   
        print(name,email,subject,message)
        if len(name)<2 or len(email)<4 or len(subject)<10 or len(message)<10:
            messages.error(request,'Please fill the form correctly')
        else:
            contact=Contact(name=name,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,'You massege is successfully sent')
    return render(request,'index.html')