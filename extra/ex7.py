# programa em Python que lê 3 notas de um aluno e
# calcula a média, além de verificar se o aluno foi aprovado ou não, 
# com base em um critério de nota mínima = 6.0

n1 = float(input("digite nota1: "))
n2 = float(input("digite nota2: "))
n3 = float(input("digite nota3: "))

# calcular media
media = (n1+n2+n3)/3
# imprime media
print("Sua média é: ", (media,2),"%.2f" %media)
# verifica se foi aprovado
if media >=6.0:
    print("aprovado")
else:
    print("reprovado")
