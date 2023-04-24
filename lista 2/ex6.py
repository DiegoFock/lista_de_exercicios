#.Calcule o fatorial de um numero
n1 = int (input ("Digite o número: "))
fatorial = 1
for c in range (1, n1+1):
    if n1 > 0:
        fatorial *= c
        print (fatorial)