import tkinter as tk
import math

def clicar_botao(valor):
    texto_atual = campo_texto.get()
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, texto_atual + valor)

def limpar_tela():
    campo_texto.delete(0, tk.END)

def calcular_resultado():
    try:
        expressao = campo_texto.get()
        # 'eval' avalia a expressão, e permite calcular somente funções do módulo "math"
        resultado = str(eval(expressao, {"__builtins__": None}, math.__dict__))
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, resultado)
    except:
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, "Erro")

def tratar_especial(valor):
    if valor == 'C':
        limpar_tela()
    elif valor == '=':
        calcular_resultado()
    elif valor == '^':
        clicar_botao('**')
    elif valor in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
        clicar_botao(f'math.{valor}(')

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x500")
janela.configure(bg='#303030') # Cor de fundo da janela principal para um tema escuro

# Cria o campo de texto (display)
# Alterações aqui: cor de fundo, cor da fonte e borda
campo_texto = tk.Entry(
    janela,
    font=("Arial", 24), # Aumentei um pouco a fonte para melhor visualização
    bd=8, # Borda mais visível para o efeito de profundidade
    relief=tk.RIDGE, # Efeito de borda "moderna" que parece mais profunda
    justify="right",
    bg='#414242', # Cor de fundo do display
    fg='white' # Cor do texto no display
)
campo_texto.pack(fill=tk.BOTH, expand=True, ipadx=10, ipady=20, padx=10, pady=10) # Ajustei o padding interno e externo

# Cria um quadro onde os botões vão ser posicionados
quadro_botoes = tk.Frame(janela, bg='#353535') # Cor de fundo para o quadro dos botões
quadro_botoes.pack(fill=tk.BOTH, expand=True, padx=5, pady=5) # Ajustei o padding do quadro

# Define os rótulos dos botões em linhas
botoes = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('.', '0', '(', ')'),
    ('sin', 'cos', 'tan', '+'),
    ('sqrt', 'log', 'exp', '^'),
    ('C', '=', '', '')
]

# Cria os botões com base na lista acima
for linha in botoes:
    quadro_linha = tk.Frame(quadro_botoes, bg='#353535') # Mantém a cor de fundo para a linha
    quadro_linha.pack(expand=True, fill='both')
    for texto in linha:
        if texto:
            # Alterações aqui: cor de fundo do botão, cor da fonte, borda e relevo
            botao = tk.Button(
                quadro_linha,
                text=texto,
                font=("Arial", 18, "bold"), # Adicionei bold para o texto do botão
                bg='#606060', # Cor de fundo dos botões (um cinza mais claro)
                fg='white', # Cor do texto dos botões
                relief=tk.FLAT, # Estilo de botão "flat" para um visual mais moderno
                bd=1, # Pequena borda para separação
                command=lambda val=texto: tratar_especial(val)
                if val in ['=', 'C', '^', 'sin', 'cos', 'tan', 'sqrt', 'log', 'exp']
                else clicar_botao(val)
            )
            # Adicionado padding interno e externo para a separação dos botões
            botao.pack(side='left', expand=True, fill='both', padx=2, pady=2)

# Mantém a janela aberta esperando interação do usuário
janela.mainloop()