# contato/forms.py
from django import forms
from .models import MensagemContato

class ContatoModelForm(forms.ModelForm):
    
    class Meta:
        model = MensagemContato
        
        # CAMPOS ATUALIZADOS
        fields = ['nome', 'email', 'celular', 'assunto', 'descricao']

        # WIDGETS ATUALIZADOS
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ex: (XX) XXXXX-XXXX', 'class': 'form-control'}), # NOVO WIDGET
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto da mensagem', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem...', 'class': 'form-control'}), # Mensagem renomeada para descricao
        }
        
        # LABELS ATUALIZADOS
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
            'celular': 'Celular/Contato', # NOVO LABEL
            'descricao': 'Descrição (Mensagem)', # LABEL AJUSTADO
        }