import tkinter as tk         # Biblioteca para interface gráfica
import math                  # Biblioteca com funções matemáticas

# Função que será chamada quando um botão comum (número ou operador) for clicado
def clicar_botao(valor):
    texto_atual = campo_texto.get()         # Pega o que está escrito na tela
    campo_texto.delete(0, tk.END)           # Apaga o conteúdo atual
    campo_texto.insert(0, texto_atual + valor)  # Insere o novo valor no final

# Função que limpa a tela (ou botão "C")
def limpar_tela():
    campo_texto.delete(0, tk.END)           # Apaga todo o conteúdo da entrada

# Função que calcula a expressão digitada e mostra o resultado
def calcular_resultado():
    try:
        expressao = campo_texto.get()       # Pega a expressão matemática digitada

        # 'eval' avalia a expressão, e permite calcular somente funções do módulo "math"
        resultado = str(eval(expressao, {"__builtins__": None}, math.__dict__))
        campo_texto.delete(0, tk.END)       # Limpa a tela
        campo_texto.insert(0, resultado)    # Mostra o resultado
    except:
        campo_texto.delete(0, tk.END)       # Limpa a tela
        campo_texto.insert(0, "Erro")       # Mostra "Erro" se algo deu errado

# Função que trata alguns botões especiais como "=", "C", "sin", "sqrt", entre outros
def tratar_especial(valor):
    if valor == 'C':
        limpar_tela()                        # Limpa tudo se for "C"
    elif valor == '=':
        calcular_resultado()                 # Calcula se for "="
    elif valor == '^':
        clicar_botao('**')                   # Insere "**" para potência
    elif valor in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
        clicar_botao(f'math.{valor}(')       # Insere a função matemática, ex: math.sin(

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")      # Título da janela
janela.geometry("400x500")                  # Tamanho da janela (largura x altura)

# Cria o campo de texto onde aparecerão os números e os resultados
campo_texto = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
campo_texto.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Cria um quadro onde os botões vão ser posicionados
quadro_botoes = tk.Frame(janela)
quadro_botoes.pack()

# Define os rótulos dos botões em linhas, como se fosse uma tabela
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
    quadro_linha = tk.Frame(quadro_botoes)      # Cria uma linha de botões
    quadro_linha.pack(expand=True, fill='both') # Expande a linha horizontalmente
    for texto in linha:
        if texto:  # Só cria botão se tiver texto (evita espaços em branco)
            botao = tk.Button(
                quadro_linha,
                text=texto,                     # Texto que aparece no botão
                font=("Arial", 18),
                relief=tk.RAISED,
                command=lambda val=texto: tratar_especial(val)
                if val in ['=', 'C', '^', 'sin', 'cos', 'tan', 'sqrt', 'log', 'exp']
                else clicar_botao(val)          # Define o que acontece ao clicar
            )
            botao.pack(side='left', expand=True, fill='both')  # Adiciona o botão à linha

# Mantém a janela aberta esperando interação do usuário
janela.mainloop()
