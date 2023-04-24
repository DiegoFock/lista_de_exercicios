#Faça um programa que receba um número e determine se ele é primo ou não.
n1 = int (input ("digite o número: "))
if n1 == 2:
    print (f"O número {n1} é primo")
elif n1 % 2 == 0:
    print (f"O número {n1} não é primo")

else:
    print (f"O número {n1} é primo")