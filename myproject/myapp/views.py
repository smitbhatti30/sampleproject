from django.shortcuts import render,redirect
from datetime import datetime
from .forms import ContactForm
from .models import ContactSubmission

def index(request):
    current_datetime = datetime.now()
    
    return render(request, 'myapp/index.html', {
        'current_datetime': current_datetime,
    })

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'myapp/submit_form.html', {
            'name': name,
            'email': email
        })
    else:
        return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')


def contact_view(request):
    if request.method == 'POST':
        return render(request, 'myapp/contact.html', {'submitted': True})
    return render(request, 'myapp/contact.html')


def submit_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you') 
    else:
        form = ContactForm()
    
    return render(request, 'myapp/contact_form.html', {'form': form})


def submissions_list(request):
    submissions = ContactSubmission.objects.all()
    return render(request, 'myapp/submissions_list.html', {'submissions': submissions})



def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ContactForm()
    
    return render(request, 'myapp/contact_form.html', {'form': form, 'submitted': False})

def submit_form(request):
    return render(request, 'myapp/contact_form.html', {'submitted': True})

def thank_you(request):
    return render(request, 'myapp/thank_you.html')
