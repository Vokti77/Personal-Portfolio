from django.shortcuts import render
from django.contrib import messages

from pages.models import Contact


def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        obj = Contact.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)
        obj.save()
        messages.success(request, 'Message Send Successful!!')
        return render(request, 'pages/index.html')
    else:
        return render(request, 'pages/index.html')


def show(request):
    info = Contact.objects.all()
    print(info)
    context = {
        'info': info
    }
    return render(request, 'pages/show.html', context)
