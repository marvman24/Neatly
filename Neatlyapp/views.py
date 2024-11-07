from django.shortcuts import render,HttpResponse, redirect
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Custom(request):
    return render(request, 'custom.html')

def Daf(request):
    return render(request, 'daf.html')

def HeavyDuties(request):
    return render(request, 'heavyduties.html')

def Iveco(request):
    return render(request, 'iveco.html')

def Man(request):
    return render(request, 'man.html')

def Mercerdes(request):
    return render(request, 'mecerdes.html')

def Renault(request):
    return render(request, 'renalt.html')

def Scania(request):
    return render(request, 'scania.html')

def Volvo(request):
    return render(request, 'volvo.html')

def contact_view(request):
    if request.method == 'POST':

        full_name = request.POST.get('fuln')
        email = request.POST.get('email')
        phone_number = request.POST.get('num')
        country = request.POST.get('country')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal')
        address = request.POST.get('address')
        car_brand = request.POST.get('car_brand')
        car_model = request.POST.get('car_model')
        message = request.POST.get('message')
        quantity = request.POST.get('quantity')

        subject = "New Contact Form Submission"
        body = (
            f"Name: {full_name}\n"
            f"Email: {email}\n"
            f"Phone Number: {phone_number}\n"
            f"Country: {country}\n"
            f"State: {state}\n"
            f"Postal/Zip Code: {postal_code}\n"
            f"Address: {address}\n"
            f"Car Brand: {car_brand}\n"
            f"Car Model: {car_model}\n"
            f"Quantity: {quantity}\n"
            f"Message: {message}\n"
        )

        try:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                ['customers.neatlytrucksintl@gmail.com'],
                fail_silently=False,
            )
            return redirect('thank_you')
        except Exception as e:
            return HttpResponse(f"Error Sending Message: {e}")
    return render(request, 'contact.html')

def thank_you(request):
    return render(request, 'thank_you.html')