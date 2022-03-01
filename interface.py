import tkinter as tk
from tkinter import ttk

lista_confianca = ['90', '95', '95.5', '99']

janela = tk.Tk()
janela.title("Amostragem")
janela.geometry("450x350")
janela['bg'] = "#A63D40"


def amostra():
    N = int(entry_populacao.get())
    Z = combobox_tipo.get()
    if Z == '90':
        Z = 1.65
    elif Z == '95':
        Z = 1.96
    elif Z == '95.5':
        Z = 2
    elif Z == '99':
        Z = 2.57
    p = float(entry_proporcao.get())
    p /= 100
    e = float(entry_erro_amostral.get())
    e /= 100

    n = (N * (Z**2) * p * (1 - p)) / ((e**2) * (N - 1) + (Z**2) * p * (1 - p))

    resultado["text"] = n


label_populacao = tk.Label(text="AMOSTRAGEM", bg="#E9B872", fg="#151515", font="Arial 12 bold italic")
label_populacao.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_populacao = tk.Label(text="Tamanho da população", bg="#E9B872", fg="#151515", font="Arial 12 bold italic")
label_populacao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_populacao = tk.Entry()
entry_populacao.grid(row=1, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_confianca = tk.Label(text="Nível de confiança", bg="#E9B872", fg="#151515", font="Arial 12 bold italic")
label_confianca.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_tipo = ttk.Combobox(values=lista_confianca)
combobox_tipo.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_proporcao = tk.Label(text="Estimativa da verdadeira proporção", bg="#E9B872", fg="#151515", font="Arial 12 bold italic")
label_proporcao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_proporcao = tk.Entry()
entry_proporcao.insert(0, 50)
entry_proporcao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_erro_amostral = tk.Label(text="Erro amostral", bg="#E9B872", fg="#151515", font="Arial 12 bold italic")
label_erro_amostral.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_erro_amostral = tk.Entry()
entry_erro_amostral.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao = tk.Button(text="Calcular", command=amostra, bg="#E9B872", fg="#151515", font="Arial 12 bold italic")
botao.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

resultado = tk.Label(janela, text="")
resultado.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()