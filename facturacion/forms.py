from django import forms

class BasePruebaForm(forms.ModelForm):
    '''
    Formulario para el modelo BasePrueba
    '''
    class Meta:
        model = BasePruebaForm
        fields = "__all__"
        #exclude = ['owner']