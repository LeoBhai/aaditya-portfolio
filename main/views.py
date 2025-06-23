from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            subject = f"📩 New Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['aaditya.sharma.58592@gmail.com'],
                    fail_silently=False,
                )
                return JsonResponse({'status': 'success'}, status=200)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

        return JsonResponse({'status': 'error', 'message': 'Missing fields'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)