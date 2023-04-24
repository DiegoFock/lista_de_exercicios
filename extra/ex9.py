# fibonacci
# 1,1,2,3,5,8,...
# x y
# n= -2 entrada invalida

#Forma + fácil
n = int(input("digite o elememto: ")) 

anterior = 1
proximo = 1
temp = 0

for i in range(n):
    print(anterior)
    temp=anterior
    anterior=proximo
    proximo=temp+anterior

#forma mais apropriada
# n = int(input("digite a qtd"))
# if n <= 0:
#     print("entrada invalida")
# else:
#     x,y = 0,1
#     print("a sequencia ate a entrada n, ", n, "é")
#     print(x) 
#     print(y)

#     for _ in range(n-2):
#         x,y = y, x+y
#         print(y)
