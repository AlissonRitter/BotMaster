# automacao_app/automacao_script.py
import os
import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from automacao_app.models import ConfiguracaoAutomacao

class Command(BaseCommand):
    help = 'Script de automação para postagens no Instagram'

    def handle(self, *args, **options):
        # Obter as configurações de automação
        configuracao = ConfiguracaoAutomacao.objects.first()

        if configuracao:
            # Caminhos para as pastas de imagens, vídeos e legendas
            pasta_imagens = configuracao.caminho_imagens
            pasta_videos = configuracao.caminho_videos
            pasta_legendas = configuracao.caminho_legendas

            # Obter listas de arquivos nas pastas
            lista_imagens = [f for f in os.listdir(pasta_imagens) if f.endswith(('.png', '.jpg', '.jpeg'))]
            lista_videos = [f for f in os.listdir(pasta_videos) if f.endswith(('.mp4', '.avi', '.mov'))]
            lista_legendas = [f for f in os.listdir(pasta_legendas) if f.endswith('.txt')]

            # Verificar se há conteúdo nas pastas
            if lista_imagens and lista_videos and lista_legendas:
                # Escolher aleatoriamente uma imagem, um vídeo e uma legenda
                imagem_escolhida = random.choice(lista_imagens)
                video_escolhido = random.choice(lista_videos)
                legenda_escolhida = random.choice(lista_legendas)

                # Realizar a postagem no Instagram (simulado)
                self.simular_postagem(imagem_escolhida, video_escolhido, legenda_escolhida)

                self.stdout.write(self.style.SUCCESS('Postagem realizada com sucesso!'))
            else:
                self.stdout.write(self.style.ERROR('Não há conteúdo suficiente para postagem. Verifique as pastas.'))
        else:
            self.stdout.write(self.style.ERROR('Configuração de automação não encontrada.'))

    def simular_postagem(self, imagem, video, legenda):
        # Simulação de postagem (substitua com a lógica real de postagem no Instagram)
        data_hora_postagem = datetime.now() + timedelta(minutes=random.randint(1, 60))
        self.stdout.write(f'Simulando postagem no Instagram:')
        self.stdout.write(f'Imagem: {imagem}')
        self.stdout.write(f'Vídeo: {video}')
        self.stdout.write(f'Legenda: {legenda}')
        self.stdout.write(f'Data/Hora: {data_hora_postagem.strftime("%Y-%m-%d %H:%M:%S")}')
