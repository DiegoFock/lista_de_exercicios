# <18 menor de idade
# acima de 18 e abaixo que 60 aulto
# acima de 60 idoso
idade = int(input("digite sua idade"))

if idade < 18:
    print("menor de idade")
elif idade  >=18 and  idade < 60:
    print("adulto")
else:
    print("idoso")