#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55... Faça um programa capaz de gerar a série até o n-ésimo termo.


n = int (input ("digite a quantidade de termos: "))
fib= []
if n == 1:
    fib = [1]
elif n == 2:
    fib = [1, 1]
else:
    fib = [1, 1]
    a = 1
    b = 1
    for i in range(2, n):
        c = a + b
        fib += [c]
        a = b
        b = c
print(fib)
        