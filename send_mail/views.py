from django.shortcuts import render, redirect
# from send_mail.forms import SendMailForm
from send_mail.tasks import send_mail_to_email
from send_mail.models import SendMail


def index(request):
    template_name = './index.html'
    return render(request, template_name)


def send(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    position = request.POST.get('position')
    message = request.POST.get('message')
    print(email)
    send_mail_to_email.delay(
        name,
        email,
        message,
        position)
    print('-'*20, 1)
    SendMail.objects.create(
        name=name,
        email=email,
        message=message,
        position=position)
    return redirect('index')
