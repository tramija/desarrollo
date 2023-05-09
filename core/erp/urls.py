from django import views
from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.tarea.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.evaluacion.views import *
from core.erp import *



from core.erp.views.tests.views import TestView

app_name = 'erp'
urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/mail/', mail, name= 'category_mail'),
    
   
   
    
    # client
    path('evaluacion/list/', EvaluacionListView.as_view(), name='evaluacion_list'),
    path('evaluacion/add/', EvaluacionCreateView.as_view(), name='evaluacion_create'),
    path('evaluacion/update/<int:pk>/', EvaluacionUpdateView.as_view(), name='evaluacion_update'),
    path('evaluacion/delete/<int:pk>/', EvaluacionDeleteView.as_view(), name='evaluacion_delete'),
   # path('evaluacion/delete/<int:pk>/', EvaluacionDeleteView.as_view(), name='evaluacion_delete'),
    
    path('evaluacion/mail/', mail, name= 'evaluacion_mail'),
    

    #Tarea
    path('tarea/list/', TareaListView.as_view(), name='tarea_list'),
    path('tarea/add/', TareaCreateView.as_view(), name='tarea_create'),
    path('tarea/update/<int:pk>/', TareaUpdateView.as_view(), name='tarea_update'),
    path('tarea/delete/<int:pk>/', TareaDeleteView.as_view(), name='tarea_delete'),
    path('tarea/mail/', mail, name= 'tarea_mail'),
    
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # test
    path('test/', TestView.as_view(), name='test'),
    
]