from django.shortcuts import redirect, render
from config.wsgi import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string

from config import settings
from core.user.models import User


# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template


#ef send_email():
#     try:
#         mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
#         print(mailServer.ehlo())
#         mailServer.starttls()
#         print(mailServer.ehlo())
#         mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#         print('Conectado..')

#         email_to = 'desarrollo@cib.org.co'
#         # Construimos el mensaje simple
#         mensaje = MIMEMultipart()
#         mensaje['From'] = settings.EMAIL_HOST_USER
#         mensaje['To'] = email_to
#         mensaje['Subject'] = "Tienes un correo"

#         content = render_to_string('send_email.html', {'user': User.objects.get(pk=1)})
#         mensaje.attach(MIMEText(content, 'html'))

#         mailServer.sendmail(settings.EMAIL_HOST_USER,
#                             email_to,
#                             mensaje.as_string())

#         print('Correo enviado correctamente')
#     except Exception as e:
#         print(e)


# send_email()


def create_mail(subject, mail, path_template,  context):
    template = get_template(path_template)
    content = template.render(
        context
    )
    
    mail= EmailMultiAlternatives(
        subject=subject, 
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            mail
        ],
        cc=[]
    )
    mail.attach_alternative(content, 'text/html')
    
    return mail

def index(request):
    return render(request, 'index.html', {})

def mail(request):
    email = create_mail('prueba de correo con maquetado',
                         'desarrollo@cib.org.co',
                         'mails/welcome.html',
                         {'user': 'desarrollo'}
                         )
    email.send(fail_silently=False)
 
   
    
    return redirect('index')
     
