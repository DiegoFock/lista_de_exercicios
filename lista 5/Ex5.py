#. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês
pagamento = float (input ("Salário por hora trabalhada: "))
hora = int (input ("Horas trabalhadas no mês: "))
salario = pagamento*hora
print (f"O salário esse mês é de: {salario} R$")