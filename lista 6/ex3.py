#Faça um programa que leia o n termos a seguir
# S= 1/1 + 2/3 + 3/5 + 4/7 + 5/9 +... + n/m

n = int(input("Digite o valor de n: "))
s = []
denominador = 1
for numerador in range(1, n+1):
    s.append(f"{numerador}/{denominador}")
    denominador += 2
print(s)