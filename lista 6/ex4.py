#Sendo H= 1+ 1/2 + 1/3 + 1/4 +... +1/n. Faça um programa que calcule o valor de H com n termos
n = int(input("Digite o número de termos: "))
soma = 0
for i in range(1, n+1):
    soma += 1/i
print("O valor de H com", n, "termos é:", soma)