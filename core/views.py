from django.shortcuts import render

# Create your views here.
# automacao_app/views.py
from django.shortcuts import render, redirect
from ..robobot_projeto.automacao_app.forms import ConfiguracaoAutomacaoForm

def configuracao_automacao(request):
    if request.method == 'POST':
        form = ConfiguracaoAutomacaoForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário, se necessário
            # Redirecionar para outra página, se necessário
            pass
    else:
        form = ConfiguracaoAutomacaoForm()

    return render(request, 'automacao_app/configuracao_automacao.html', {'form': form})
# core/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

