from django.shortcuts import render,redirect
from django.core.mail import send_mail
from job.forms import ContactForm

# Create your views here.

def home(request):
    return render (request,'job/home.html')

def about(request):
    return render(request,'job/about.html')

def contact(request):
    # return render(request,'job/contact.html')
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can send an email here or store the message.
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['support@careerconnect.com'],
            )
            return redirect('contact')  # Redirect after submission
    return render(request, 'job/contact.html', {'form': form})

    # return render(request,'job/contact.html')

def index(request):
    return render(request,'base.html')