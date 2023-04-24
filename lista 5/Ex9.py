#Faça um programa Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#a) Para homens: (72.7*h) - 58
#b) Para mulheres: (62.1*h) - 44.7


h = float (input ("Digite sua altura em metros: "))
genero = input ("Seu gênero: homem ou mulher?")
if genero == "homem":
    peso1 = 72.7*h - 58
    print ("Seu peso médio é: ", peso1 )
elif genero == "mulher":
    peso2 = 62.1*h - 44.7
    print ("Seu peso médio é: ", peso2)
else:
    print ("Gênero não identificado")