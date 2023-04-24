# .Faça um programa que calcule as potências de 2 até um determinado número
n1 = int(input("insira até que número determinado: "))

for c in range(n1+1):
    potencia = 2 ** c
    if potencia > n1:
        print (f"2 elevado à {c} = {potencia}")