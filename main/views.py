from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Contact

def home(request):
    return render(request, 'main/home.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)

            # ✅ If it's a JS fetch() request, return JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'}, status=200)

            # Fallback for traditional form (not used here, but safe)
            return redirect('home')
        else:
            # Missing fields
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'Missing fields'}, status=400)

            return HttpResponseBadRequest("Missing fields")

    # Non-POST request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    return HttpResponseBadRequest("Invalid request method")
