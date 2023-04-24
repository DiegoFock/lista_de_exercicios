#Faça um programa que o IMC de uma pessoa

h = float (input ("Digite sua altura em metros: "))
peso = float (input ("Seu peso em kg: "))
imc = peso/(h**2)
imc = (imc, 0)
print ("Seu IMC é: ", imc, "kg/m²")
