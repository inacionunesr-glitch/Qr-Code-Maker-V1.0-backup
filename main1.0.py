import qrcode
from tkinter import *
from tkinter import messagebox, filedialog
import os

numero = 0
PASTA = ""

root = Tk()

root.title("QR Code Maker")
root.geometry("500x500")
root.resizable(False, False)

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

button0 = Button(root,text="Selecionar Pasta", width=13, height=2, font=("Arial Bold", 16, "bold"), command=selecionar_pasta)
button0.pack()

button1 = Button(root,text="Gerar QR Code", width=13, height=2, font=("Arial Bold", 16, "bold"), command=Gerar)
button1.pack()

button2 = Button(root,text="Abrir Pasta", width=13, height=2, font=("Arial Bold", 16, "bold"), command=abrir_pasta)
button2.pack()

entry = Entry(root, font=("Arial Bold", 18, "bold"),width=28)
entry.place(x=80, y=200)

root.mainloop()
