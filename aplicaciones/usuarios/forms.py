from django import forms
from django.contrib.auth import authenticate
from .models import Usuario

class Login(forms.Form):
    nombre_usuario = forms.CharField()
    contrasenia = forms.CharField(widget=forms.PasswordInput)

    #metodo que limpia los campos
    def limpiar(self, *args, **kwargs):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        contrasenia = self.cleaned_data.get('contrasenia')

        #valida que ambos campos esten digitados
        if usuario and contrasenia:

            #el metodo 'authenticate' valida que ambos campos coincidan y devuelve un
            #objeto de tipo 'User'
            usuario= authenticate(username=nombre_usuario,password=contrasenia)

            if not usuario:
                raise forms.ValidationError('Usuario No Existe')
            if not usuario.check_password(contrasenia):
                raise forms.ValidationError('Contraseña Incorrecta')
        #se llama al metodo y limpia todo
        return super(Login, self).clean(*args, **kwargs)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields= [
            'rut','nombre','apellido','email','usuario','contrasenia',
        ]
