from django import forms

from app.models import Solicitation

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitation
        fields = ('justify', 'date', 'entry_hour', 'exit_hour')
        widgets = {
            "date": forms.DateInput(format = ('%Y-%m-%d'), attrs = {'type': 'date', 'class': 'form-control'}),
            "entry_hour": forms.TimeInput(format = "%H:%M", attrs = {'type': 'time', 'class': 'form-control'}),
            "exit_hour": forms.TimeInput(format = "%H:%M", attrs = {'type': 'time', 'class': 'form-control'}),
            "justify": forms.TextInput(attrs={'placeholder': 'Justifique sua solicitação'})
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Solicitation
        fields = ('status', 'justify_status')
        labels = {
            'status': 'Selecione um status', 
            'justify_status': 'Justificar Status',  
        }
        
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['justify_status'].help_text = 'Justifique o porque do status selecionado.'