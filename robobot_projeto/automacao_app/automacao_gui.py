# automacao_app/automacao_gui.py
import tkinter as tk
from tkinter import filedialog

class AutomacaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuração de Automação")

        # Adicione os componentes da interface aqui
        self.btn_imagens = tk.Button(root, text="Escolher Pasta de Imagens", command=self.escolher_pasta_imagens)
        self.btn_imagens.pack()

        self.btn_videos = tk.Button(root, text="Escolher Pasta de Vídeos", command=self.escolher_pasta_videos)
        self.btn_videos.pack()

        self.btn_legendas = tk.Button(root, text="Escolher Pasta de Legendas", command=self.escolher_pasta_legendas)
        self.btn_legendas.pack()

        self.btn_iniciar = tk.Button(root, text="Iniciar Automação", command=self.iniciar_automacao)
        self.btn_iniciar.pack()

    def escolher_pasta_imagens(self):
        pasta_imagens = filedialog.askdirectory()
        print("Pasta de Imagens:", pasta_imagens)

    def escolher_pasta_videos(self):
        pasta_videos = filedialog.askdirectory()
        print("Pasta de Vídeos:", pasta_videos)

    def escolher_pasta_legendas(self):
        pasta_legendas = filedialog.askdirectory()
        print("Pasta de Legendas:", pasta_legendas)

    def iniciar_automacao(self):
        print("Iniciar Automação")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomacaoGUI(root)
    root.mainloop()

