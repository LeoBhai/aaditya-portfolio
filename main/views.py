from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, message=message)

        # 👉 Detect if request is from fetch()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})

        messages.success(request, "Your message has been sent!")
        return redirect('home')

    # Fallback for non-POST
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'fail'}, status=400)
    return redirect('home')
