import qrcode
import sys
from tkinter import *
from tkinter import messagebox, filedialog
import os

numero = 0
PASTA = ""

root = Tk()

if getattr(sys, 'frozen', False):
    pasta = sys._MEIPASS
else:
    pasta = os.path.dirname(__file__)

icone = os.path.join(pasta, "icone.ico")

root.iconbitmap(default=icone)

root.title("QR Code Maker")
root.geometry("600x400")
root.resizable(False, False)
root.config(bg="#11244B")

def selecionar_pasta():
    global PASTA

    pasta_escolhida = filedialog.askdirectory()

    if pasta_escolhida != "":
        PASTA = pasta_escolhida
        messagebox.showinfo("Sucesso", "Pasta Selecionada")

def Gerar():
    global numero

    if PASTA == "":
        messagebox.showerror("Erro", "Nenhuma Pasta Foi Selecionada")
        return

    numero +=1

    caminho = rf"{PASTA}\qrcode{numero}.png"

    url = entry.get().strip()

    if url == "":
        messagebox.showerror("Erro", "Nehuma Url Foi Detectada")
    else:
        qr = qrcode.QRCode()
        qr.add_data(url)

        imagem = qr.make_image()
        imagem.save(caminho)

        messagebox.showinfo("Sucesso", f"QR Code salvo como qrcode{numero}.png")

def abrir_pasta():
    if PASTA != "":
        os.startfile(PASTA)
    else:
        messagebox.showerror("Erro", "Nenhuma Pasta Foi Selecionada")

button0 = Button(root,text="Selecionar Pasta", width=13, height=2, font=("Arial Bold", 13, "bold"), command=selecionar_pasta)
button0.grid(row=0,column=0)

button1 = Button(root,text="Gerar QR Code", width=13, height=2, font=("Arial Bold", 13, "bold"), command=Gerar)
button1.grid(row=1,column=0)

button2 = Button(root,text="Abrir Pasta", width=13, height=2, font=("Arial Bold", 13, "bold"), command=abrir_pasta)
button2.grid(row=2,column=0)

entry = Entry(root, font=("Arial Bold", 20, "bold"),width=28)
entry.grid(row=1,column=1)

root.mainloop()