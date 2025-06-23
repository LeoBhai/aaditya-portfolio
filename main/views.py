from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse, HttpResponseBadRequest

def home(request):
    return render(request, 'main/home.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)

            # Detect if it's a JavaScript fetch call
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})

            # Normal form fallback (not used in your case)
            return render(request, 'main/home.html', {'success': True})
        else:
            return HttpResponseBadRequest("Missing fields")

    return HttpResponseBadRequest("Invalid method")
