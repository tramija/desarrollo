from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.erp.models import Category, Tarea, Evaluacion

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
       
        
        

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese  el nombre del Plan',
                }
            ),
            'date_joined': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'descripcionProblema': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese una Descripcion del problema',
                    'rows': 4,
                    'cols': 4
                }
            ),
           
            
            'normaIncumplida': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese una Norma Incumplida',
                    
                }
            ),

            'entidad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la identidad que reporte',
                    
                }
            ),

            'tratamientoInmediato': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese una correciòn o tratamiento',
                    
                }
            ),
            
            
             'analisisCausa': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un analisis sobre la causa ',
                    
                }
            ),
            'causaRaiz': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un causa raiz ',
                    
                }
            ),
            'analisisCausa': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un analisis sobre la causa ',
                    
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data




#Tarea


class TareaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
        
             
         
        
        
        

    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el  nombre del plan de acciòn',
                }
            ),
            'descripcionActividades': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripcion de las Actividades',
                    'rows': 4,
                    'cols': 4,
                }
            ),
            'fecha_inicio': forms.DateInput(
                
                    
                
            ),
            'fecha_terminacion': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'data-target': '#fecha_terminacion',
                    'data-toggle': 'datetimepicker'
                    
                }
            ),
                
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


#Evaluacion


class EvaluacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
        

    class Meta:
        model = Evaluacion
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un el nombre del plan de acciòn',
                }
            ),
              'date_joined': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    # 'class': 'form-control datetimepicker-input',
                    # 'id': 'date_joined',
                    # 'data-target': '#date_joined',
                    # 'data-toggle': 'datetimepicker'
                }
            ),
              'fecha_cierre': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    # 'class': 'form-control datetimepicker-input',
                    # 'id': 'fecha_cierre',
                    # 'data-target': '#fecha_cierre',
                    # 'data-toggle': 'datetimepicker'
                }
            ),
                
                
            'responsable': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un clasificacion ',
                    
                },
                
                
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data





class TestForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))



    # search = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ingrese una descripción'
    # }))

    
