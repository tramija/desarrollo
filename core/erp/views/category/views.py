import threading
from crum import get_current_request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.sites.shortcuts  import  get_current_site
from requests import request
from django.contrib import messages
from django.shortcuts import  redirect, render, reverse

from core.erp.forms import CategoryForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Category


from django.shortcuts import redirect, render
from config.wsgi import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string

from config import settings
from core.user.models import User


# Envio de correos 
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template





class CategoryListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    permission_required = 'view_category'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Category.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado del plan de Analisis'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Analisis'
        return context


class CategoryCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')
    permission_required = 'add_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un plan de Analisis'
        context['entity'] = 'Analisis'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class CategoryUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')
    permission_required = 'change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un plan de Analisis'
        context['entity'] = 'Analisis'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class CategoryDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp:category_list')
    permission_required = 'delete_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un plan de Analisis'
        context['entity'] = 'Analisis'
        context['list_url'] = self.success_url
        return context



#eNVIO DE CORREO 


def create_mail(subject, mail, template_path, context):
     template = get_template(template_path)
     content = template.render(
         context)
     
     mail = EmailMultiAlternatives(
         subject,
         body='',
         from_email= settings.EMAIL_HOST_USER,
         to=[
          mail
         ],
         cc=[]
        

    )

     mail.attach_alternative(content, 'text/html')
     return mail

def welcome_mail(mail, context):
    email = create_mail('prueba de correo conmaquetado', 
                         mail, 'category/mails/send_email.html',
                         context
                         
        
                         )
    
    email.send(fail_silently=False)

def mail(request):
    messages.success(request, 'Correo enviado correctamente, ver' )
    user={
        'username': 'desarrollo',
        'email': 'desarrollo@cib.org.co',
        'domain': get_current_request(request).domain,
        
        'url_login': reverse('login')
    }
    thread = threading.Thread(target= welcome_mail, args=(user['email'], user))
    thread.start()
    
    
    return redirect('index')