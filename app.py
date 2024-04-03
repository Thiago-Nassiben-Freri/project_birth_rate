import tkinter as tk
from tkinter import messagebox

def natalidadeCalculator(pop, nasc_mes):
    try:
        pop = float(pop)
        nasc_mes = float(nasc_mes)
        var_resultado = (nasc_mes / pop) * 1000
        return var_resultado
    except ValueError:
        return 'Erro de valor!'

def exibir_resultados():
    pop = entrada_populacao.get()
    nasc_mes = entrada_nascimentos.get()
    
    taxa_natalidade = natalidadeCalculator(pop, nasc_mes)
    
    if taxa_natalidade is None:
        messagebox.showerror("Erro", "Por favor, insira números válidos para população e número de nascimentos.")
        return
    
    resultado_label.config(text=f"Taxa de Natalidade por mulher é: {taxa_natalidade:.2f} filhos")

def fechar_janela():
    root.destroy()

root = tk.Tk()
root.title("Calculadora de Taxa de Natalidade")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

instrucao_populacao = tk.Label(frame, text="População:")
instrucao_populacao.grid(row=0, column=0, padx=5, pady=5)

entrada_populacao = tk.Entry(frame)
entrada_populacao.grid(row=0, column=1, padx=5, pady=5)

instrucao_nascimentos = tk.Label(frame, text="Número de Nascimentos por Mês:")
instrucao_nascimentos.grid(row=1, column=0, padx=5, pady=5)

entrada_nascimentos = tk.Entry(frame)
entrada_nascimentos.grid(row=1, column=1, padx=5, pady=5)

calcular_btn = tk.Button(frame, text="Calcular", command=exibir_resultados)
calcular_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

fechar_btn = tk.Button(frame, text="Fechar", command=fechar_janela)
fechar_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
