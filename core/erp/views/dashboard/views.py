
import dataclasses
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.models import Category, Evaluacion, Tarea

from random import randint


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
    
    def get_graph_planes_year_month(self):
        data=[]
        
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Category.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r'),
                data.append(float(total))
        
        
        except:
            pass
        return data
            
                                               

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['graph_planes_año_mes'] = self.get_graph_planes_year_month()
       
        return context
