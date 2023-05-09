from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from config import settings

from core.erp.forms import TareaForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import  Tarea


from django.shortcuts import  redirect, render, reverse
from django.contrib import messages 



#Correos 
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import threading
#Dominio 
from django.contrib.sites.shortcuts import get_current_site



class TareaListView( ListView):
    model = Tarea
    template_name = 'tarea/list.html'
    permission_required = 'view_tarea'

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
                for i in Tarea.objects.all():
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
        context['title'] = 'Listado de tarea'
        context['create_url'] = reverse_lazy('erp:tarea_create')
        context['list_url'] = reverse_lazy('erp:tarea_list')
        context['entity'] = 'Tarea'
        return context


class TareaCreateView( CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/create.html'
    success_url = reverse_lazy('erp:tarea_list')
    permission_required = 'add_tarea'
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
        context['title'] = 'Creación una tarea'
        context['entity'] = 'Tarea'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TareaUpdateView( UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/create.html'
    success_url = reverse_lazy('erp:tarea_list')
    permission_required = 'change_tarea'
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
        context['title'] = 'Edición una tarea'
        context['entity'] = 'tarea'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TareaDeleteView( DeleteView):
    model = Tarea
    template_name = 'tarea/delete.html'
    success_url = reverse_lazy('erp:tarea_list')
    permission_required = 'delete_tarea'
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
        context['title'] = 'Eliminación de una tarea'
        context['entity'] = 'Tareas'
        context['list_url'] = self.success_url
        return context



# ENVIO DE CORREOS 



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
    messages.success(request, 'Correo enviado correctamente, ver' )
    user={
        'username': 'desarrollo',
        'email': 'desarrollo@cib.org.co',
        'domain': get_current_site(request).domain,
        
        'url_login': reverse('login')
    }
    thread = threading.Thread(target= welcome_mail, args=(user['email'], user))
    thread.start()
    
    
    return redirect('index')

