
# automacao_app/forms.py
from django import forms

class ConfiguracaoAutomacaoForm(forms.Form):
    hora_inicio = forms.TimeField(
        label='Hora de Início',
        widget=forms.TimeInput(attrs={'class': 'form-control'}),
    )
    hora_termino = forms.TimeField(
        label='Hora de Término',
        widget=forms.TimeInput(attrs={'class': 'form-control'}),
    )
    # Adicione outros campos conforme necessário
