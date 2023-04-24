#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#1 Esse funcionário foi contratado em 2005, com salário inicial de R$ 1000,00
#2 Em 2006 recebeu aumento de 1,5% sobre seu salário inicial
#3 A partir de 2007(inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto,altere o programa permitindo que o usuário digite o salário inicial do funcionário


aumento = 0.015
sal = 1000

#2006 até 2023 = 17 anos

for ano in range(2006, 2024):
    porc = ano*aumento
    if ano <= 2023:
        porc = porc*2
        total = sal*porc
print (total)

#Alterando para o usuário colocar seu salário

aumento = 0.015
sal = float (input ("digite seu salário: R$ "))

#2006 até 2023 = 17 anos

for ano in range(2006, 2024):
    porc = ano*aumento
    if ano <= 2023:
        porc = porc*2
        total = sal*porc
print (f"Seu salário era {sal}, com a correção do ano 2023, foi para {total}")