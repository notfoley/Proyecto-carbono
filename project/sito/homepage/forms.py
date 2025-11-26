from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SpanishUserCreationForm(forms.ModelForm):
    username = forms.CharField(
        label='Usuario',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_'
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Mínimo 8 caracteres, no solo números y no demasiado común.'
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Ingresa la misma contraseña para verificación.'
    )
    
    class Meta:
        model = User
        fields = ('username',)
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if len(password1) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        if password1.isdigit():
            raise ValidationError('La contraseña no puede ser completamente numérica.')
        
        common_passwords = ['123456', '12345678', 'password', '123456789', '1234567']
        if password1.lower() in common_passwords:
            raise ValidationError('La contraseña es demasiado común.')
            
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user