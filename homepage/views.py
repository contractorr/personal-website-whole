from django.shortcuts import render
from .forms import SentMessage 
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def index(request):
    """The home page for my website"""
    form = SentMessage()
    return render(request, 'homepage/index.html', {'form': form})

def project_1(request):
    """Show a specific project."""
    return render(request, 'homepage/projects/project_1.html')

def project_2(request):
    """Show a specific project."""
    return render(request, 'homepage/projects/project_2.html')

def project_3(request):
    """Show a specific project."""
    return render(request, 'homepage/projects/project_3.html')        

def contact(request):
    """Show a specific project."""
    return render(request, 'homepage/index.html#contact')

def send_message(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SentMessage(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            name = form.cleaned_data['name']
            recipients = ['rajcontractor@hotmail.co.uk']
            recipients = recipients.append(form.cleaned_data['email'])
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, name, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SentMessage()
    return render(request, 'homepage/index.html', {'form': form})    