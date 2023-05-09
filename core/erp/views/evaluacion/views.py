from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import EvaluacionForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Evaluacion






from requests import request
from config import settings

from core.erp.forms import EvaluacionForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Evaluacion

from django.shortcuts import  redirect, render, reverse
from django.contrib import messages 



#Correos 
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import threading
#Dominio 
from django.contrib.sites.shortcuts import get_current_site




class EvaluacionListView( ListView):
    model = Evaluacion
    template_name = 'evaluacion/list.html'
    permission_required = 'view_evaluacion'

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
                for i in Evaluacion.objects.all():
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
        context['title'] = 'Listado de evaluacion'
        context['create_url'] = reverse_lazy('erp:evaluacion_create')
        context['list_url'] = reverse_lazy('erp:evaluacion_list')
        context['entity'] = 'Evaluaciones'
        return context


class EvaluacionCreateView(CreateView):
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'evaluacion/create.html'
    success_url = reverse_lazy('erp:evaluacion_list')
    permission_required = 'add_evaluacion'
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
        context['title'] = 'Creación una Evaluacion'
        context['entity'] = 'Evaluacion'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class EvaluacionUpdateView( UpdateView):
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'evaluacion/create.html'
    success_url = reverse_lazy('erp:evaluacion_list')
    permission_required = 'change_evaluacion'
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
        context['title'] = 'Edición una evaluacion'
        context['entity'] = 'evaluacion'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class EvaluacionDeleteView( DeleteView):
    model =Evaluacion
    template_name = 'evaluacion/delete.html'
    success_url = reverse_lazy('erp:evaluacion_list')
    permission_required = 'delete_evaluacion'
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
        context['title'] = 'Eliminación de una evaluacion'
        context['entity'] = 'evaluacion'
        context['list_url'] = self.success_url
        return context




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
                         mail, 'evaluacion/mails/welcome.html',
                         context
                         
        
                         )
   
    
    email.send(fail_silently=False)
    

def mail(request):
   
    user={
        'username': 'desarrollo',
        'email': 'desarrollo@cib.org.co',
        'domain': get_current_site(request).domain,
        
        'url_login': reverse('login')
    }
   
    thread = threading.Thread(target= welcome_mail, args=(user['email'], user))
    thread.start()
    
    
    
    return redirect('index')



# Envio de correos sencillos
#def email(request):

    # send_mail(
    #     'prueba de correo',
    #     'Hola mundo desde django',
    #     'desarrollo@cib.org.co',
    #     [
    #     'desarrollo@cib.org.co',

    #     ],
    #     fail_silently=False
    # )

    #return redirect('index')