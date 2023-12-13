from tkinter import *
from converter import converter

telaPrincipal = Tk()

frame1 = Frame(telaPrincipal)
frame2 = Frame(telaPrincipal)
frame3 = Frame(telaPrincipal)
frame4 = Frame(telaPrincipal)
frame5 = Frame(telaPrincipal)
frame6 = Frame(telaPrincipal)
frame7 = Frame(telaPrincipal)
frame8 = Frame(telaPrincipal)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()
frame6.pack()
frame7.pack()
frame8.pack()

titulo = Label(frame1, text="Conversor de Bases", font=('verdana', 25, 'bold'), pady=20)
titulo.pack()

labelSelecionarBaseNumero = Label(frame2, text="Selecione a base que o número digitado está", font=('verdana', 10))
labelSelecionarBaseNumero.pack()

opcaoBase = IntVar()

opcaoDecimal = Radiobutton(frame3, variable=opcaoBase, text="Decimal", value=10, pady=10, padx=5)
opcaoBinario = Radiobutton(frame3, variable=opcaoBase, text="Binário", value=2, pady=10, padx=5)
opcaoOctal = Radiobutton(frame3, variable=opcaoBase, text="Octal", value=8, pady=10, padx=5)
opcaoHexaDecimal = Radiobutton(frame3, variable=opcaoBase, text="Hexadecimal", value=16, pady=10, padx=5)

opcaoDecimal.pack(side=LEFT)
opcaoBinario.pack(side=RIGHT)
opcaoOctal.pack(side=RIGHT)
opcaoHexaDecimal.pack(side=RIGHT)

labelBaseConvertida = Label(frame4, text="Escolha para qual base você quer converter", font=('verdana', 10))
labelBaseConvertida.pack()

escolhaBase = IntVar()

escolhaDecimal = Radiobutton(frame5, variable=escolhaBase, text="Decimal", value=10, pady=10, padx=5)
escolhaBinario = Radiobutton(frame5, variable=escolhaBase, text="Binário", value=2, pady=10, padx=5)
escolhaOctal = Radiobutton(frame5, variable=escolhaBase, text="Octal", value=8, pady=10, padx=5)
escolhaHexaDecimal = Radiobutton(frame5, variable=escolhaBase, text="Hexadecimal", value=16, pady=10, padx=5)

escolhaDecimal.pack(side=LEFT)
escolhaBinario.pack(side=RIGHT)
escolhaOctal.pack(side=RIGHT)
escolhaHexaDecimal.pack(side=RIGHT)

labelNumeroEscolhido = Label(frame6, text="Digite o número que você deseja converter", font=('verdana', 10, 'bold'), padx=10, pady=20)
labelNumeroEscolhido.pack(side=LEFT)

numeroEscolhido = StringVar()
entradaNumero = Entry(frame6, textvariable=numeroEscolhido, width=5, font=('verdana', 15, 'bold'))
entradaNumero.pack(side=RIGHT)

labelResultado = Label(frame8, text="", font=('verdana', 9, 'bold'), pady=50)
labelResultado.pack()

def converterNumero():

    numero = str(numeroEscolhido.get()).upper()
    baseOriginal = opcaoBase.get()
    baseConverter = escolhaBase.get()

    if bool(numero) and bool(baseOriginal) and bool(baseConverter):
        if (baseOriginal == baseConverter):
            resultado = "Operações com mesma base não são feitas"
        else:
            resultado = converter(baseOriginal, baseConverter, numero)

        labelResultado["text"] = resultado
    else:
        labelResultado["text"] = "Você deixou de preencher algo!"

buttonConverter = Button(frame7, text="Converter", pady=5, padx=5, font=('verdana', 10, 'bold'), command=converterNumero)
buttonConverter.pack()

telaPrincipal.geometry("500x500")
telaPrincipal.mainloop()