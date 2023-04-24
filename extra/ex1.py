# calcular a media de n elementos
# (10+3.5+7.5)/3
# soma = 0
# soma = soma + elemento => 0+10 = 10
# soma = soma + elemento => 10+3.5 = 13.5
# soma = soma + elemento => 13.5 + 7.5 = 21
# media = soma/n

#(10+3+7+...+)/n
#1 2 3 4 5 n
n = int(input("Digite uma entrada: "))

# inicia uma variavel para soma
soma = 0

# minha estrura de repeticao
for i in range(n):
    elemento = float(input("entre com os elementos: "))
    soma = soma + elemento

media = soma/n
print("a media dos elemntos e: ",media)



