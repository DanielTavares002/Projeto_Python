import tkinter as tk
import math

def clicar_botao(valor):
    texto_atual = campo_texto.get()
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, texto_atual + valor)
    # --- NOVO: Rola o visor para o final da expressão ---
    campo_texto.xview_moveto(1.0) # Move a visualização para o final (direita) do texto

def limpar_tela():
    campo_texto.delete(0, tk.END)

def calcular_resultado():
    try:
        expressao = campo_texto.get()

        if expressao and expressao[-1] in ['+', '-', '*', '/', '%']:
            expressao = expressao[:-1]

        if not expressao:
            campo_texto.insert(0, "")
            return

        safe_dict = {
            "__builtins__": None,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
            'exp': math.exp, 'pow': math.pow,
            'pi': math.pi, 'e': math.e
        }
        resultado = str(eval(expressao, safe_dict))
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, resultado)
        # --- NOVO: Rola o visor para o final do resultado também ---
        campo_texto.xview_moveto(1.0)
    except Exception as e:
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, "Erro")
        print(f"Erro de cálculo: {e}")

def tratar_especial(valor):
    if valor == 'C':
        limpar_tela()
    elif valor == '=':
        calcular_resultado()
    elif valor in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'log10', 'pow']:
        clicar_botao(f'math.{valor}(')
    elif valor == 'e':
        clicar_botao('math.e')
    elif valor == 'pi':
        clicar_botao('math.pi')
    elif valor == '%':
        clicar_botao('%')

janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x500")
janela.configure(bg='#303030')

campo_texto = tk.Entry(
    janela,
    font=("Arial", 24),
    bd=8,
    relief=tk.RIDGE,
    justify="right",
    bg='#414242',
    fg='white'
)
campo_texto.pack(fill=tk.BOTH, expand=True, ipadx=10, ipady=20, padx=10, pady=10)

quadro_botoes = tk.Frame(janela, bg='#353535')
quadro_botoes.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

botoes = [
    ('tan', 'sin', 'cos', 'sqrt'),
    ('log', 'log10', 'e', 'pow'),
    ('pi', '.', '(', ')'),
    ('C', '%', '/', '*'),
    ('7', '8', '9', '-'),
    ('4', '5', '6', '+'),
    ('1', '2', '3', '='),
]

cores_especiais = {
    'C': {'bg': '#FFA500', 'fg': 'white'},
    '%': {'bg': '#606060', 'fg': 'white'}, # Mantido cinza para "%" como na imagem
    '/': {'bg': '#FFA500', 'fg': 'white'},
    '*': {'bg': '#FFA500', 'fg': 'white'},
    '-': {'bg': '#FFA500', 'fg': 'white'},
    '+': {'bg': '#FFA500', 'fg': 'white'},
    '=': {'bg': '#FFA500', 'fg': 'white'}
}

for linha in botoes:
    quadro_linha = tk.Frame(quadro_botoes, bg='#353535')
    quadro_linha.pack(expand=True, fill='both')
    for texto in linha:
        if texto:
            cor_bg = '#606060'
            cor_fg = 'white'
            if texto in cores_especiais:
                cor_bg = cores_especiais.get(texto)['bg']
                cor_fg = cores_especiais.get(texto)['fg']

            botao = tk.Button(
                quadro_linha,
                text=texto,
                font=("Arial", 18, "bold"),
                bg=cor_bg,
                fg=cor_fg,
                relief=tk.FLAT,
                bd=1,
                command=lambda val=texto: tratar_especial(val)
                if val in ['=', 'C', 'sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'log10', 'e', 'pow', 'pi', '%']
                else clicar_botao(val)
            )
            botao.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        else:
            tk.Frame(quadro_linha, bg='#353535').pack(side='left', expand=True, fill='both', padx=2, pady=2)


# --- Criação do botão '0' separado para preencher a última linha ---
quadro_zero = tk.Frame(quadro_botoes, bg='#353535')
quadro_zero.pack(expand=True, fill='both', padx=2, pady=2)

botao_zero = tk.Button(
    quadro_zero,
    text='0',
    font=("Arial", 18, "bold"),
    bg='#606060',
    fg='white',
    relief=tk.FLAT,
    bd=1,
    command=lambda: clicar_botao('0')
)
botao_zero.pack(expand=True, fill='both', padx=2, pady=2)

janela.mainloop()