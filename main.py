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
        # Usamos uma lista de funções e constantes permitidas para maior segurança
        safe_dict = {
            "__builtins__": None,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
            'exp': math.exp, 'pow': math.pow, # Adicionado pow
            'pi': math.pi, 'e': math.e # Adicionado pi e e
        }
        resultado = str(eval(expressao, safe_dict))
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, resultado)
    except Exception as e: # Captura a exceção para mostrar um erro mais específico, se necessário
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, "Erro")
        # print(f"Erro: {e}") # Para depuração, se quiser ver o erro no console

def tratar_especial(valor):
    if valor == 'C':
        limpar_tela()
    elif valor == '=':
        calcular_resultado()
    # Funções matemáticas que precisam de 'math.' e parênteses
    elif valor in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'log10', 'pow']:
        clicar_botao(f'math.{valor}(')
    # Constantes matemáticas
    elif valor == 'e':
        clicar_botao('math.e')
    elif valor == 'pi':
        clicar_botao('math.pi')
    # Operador de porcentagem (modulo no Python)
    elif valor == '%':
        clicar_botao('%') # Adiciona o operador de módulo

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x500")
janela.configure(bg='#303030')

# Cria o campo de texto (display)
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

# Cria um quadro onde os botões vão ser posicionados
quadro_botoes = tk.Frame(janela, bg='#353535')
quadro_botoes.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Define os rótulos dos botões em linhas, de acordo com a imagem
# Adaptei para manter 4 colunas por linha, o que se alinha com o código existente.
# O botão '0' será uma célula normal, não ocupando múltiplas colunas visualmente como na imagem.
botoes = [
    ('tan', 'sin', 'cos', 'sqrt'),
    ('log', 'log10', 'e', 'pow'),
    ('pi', '.', '(', ')'), # '.' no lugar da ',' da imagem para padrão Python
    ('C', '%', '/', '*'),
    ('7', '8', '9', '-'),
    ('4', '5', '6', '+'),
    ('1', '2', '3', '='),
    ('0', '', '', '') # '0' na última linha, com 3 células vazias para manter o grid
]

# Cria os botões com base na lista acima
for linha in botoes:
    quadro_linha = tk.Frame(quadro_botoes, bg='#353535')
    quadro_linha.pack(expand=True, fill='both')
    for texto in linha:
        if texto:
            botao = tk.Button(
                quadro_linha,
                text=texto,
                font=("Arial", 18, "bold"),
                bg='#606060',
                fg='white',
                relief=tk.FLAT,
                bd=1,
                # Define o que acontece ao clicar (agora com as novas funções/constantes)
                command=lambda val=texto: tratar_especial(val)
                if val in ['=', 'C', 'sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'log10', 'e', 'pow', 'pi', '%']
                else clicar_botao(val)
            )
            botao.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        else: # Se o texto for vazio, cria um "espaço" invisível para manter o alinhamento
            tk.Frame(quadro_linha, bg='#353535').pack(side='left', expand=True, fill='both', padx=2, pady=2)


# Mantém a janela aberta esperando interação do usuário
janela.mainloop()