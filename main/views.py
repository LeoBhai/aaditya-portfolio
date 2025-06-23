from django.shortcuts import render, redirect
from .models import Contact  # 👈 required to save data
from django.contrib import messages  # 👈 for flash messages

def home(request):
    return render(request, 'main/home.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, "Your message has been sent!")

        return redirect('home')
    return redirect('home')