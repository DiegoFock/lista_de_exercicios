# algoritmo
#     inteiro n, i, fatorial
#     n <- 5
#     fatorial <- 1
#     para i de 1 ate n faca
#         fatorial <- fatorial * i
#     fim_para
#     escreva("O fatorial de", n, "é:", fatorial)
# fim_algoritmo

#5! = 1*2*3*4*5 = 120
# fatorial = 1  i = 1   fatorial = 1*1 = 1
# fatorial = 1  i=2     fatorial = 1*2 = 2 
# fatorial = 2  i=3     fatorial = 2*3 = 6
# fatorial = 6  i=4     fatorial = 6*4 = 24
# fatorial = 24 i=5    fatorial = 24*5 = 120      

n = 5
fatorial = 1

for i in range(1,n+1):
    fatorial = fatorial * i

print("o fatorial de ", n, "é:", fatorial)


