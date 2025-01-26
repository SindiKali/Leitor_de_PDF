#Leitor de PDF da SDCT
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from PyPDF2 import PdfReader

def abrir_pdf():
    try:
        caminho_do_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo PDF",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        if not caminho_do_arquivo:
            return

        leitor = PdfReader(caminho_do_arquivo)
        texto_pdf = ""

        for pagina in leitor.pages:
            texto_pdf += pagina.extract_text() + "\n"

        if not texto_pdf.strip():
            raise ValueError("Não foi possível extrair texto do PDF. O arquivo pode estar protegido ou ser apenas uma imagem.")

        area_texto.delete(1.0, tk.END)
        area_texto.insert(tk.END, texto_pdf)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir o PDF: {e}")

janela = tk.Tk()
janela.title("Leitor de PDF")
janela.geometry("800x600")

botao_abrir = tk.Button(janela, text="Abrir PDF", command=abrir_pdf, font=("Arial", 12))
botao_abrir.pack(pady=10)

area_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, font=("Arial", 12))
area_texto.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

janela.mainloop()