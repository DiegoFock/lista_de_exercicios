#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo.
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo
n1 = int (input("Valor inteiro 1: "))
n2 = int (input("Valor inteiro 2: "))
n3 = float (input ("Valor real: "))

#a)

a = (n1*2)*(n2/2)
print ("Letra a", a)

#b)

b = (n1*3)+n3
print ("Letra b", b)

#c)

c = n3**3
print ("Letra c", c)