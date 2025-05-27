#exercicio9
n1=float(input("digite o primeiro numero:"))
n2=float(input("digite o segundo numero:"))
op=(input("digite a operação desejada (soma(+),divisão(/),subtração(-),multiplicação(*))"))
if op == "+":
    r = n1+n2
elif op == "/":
    r = n1/n2
elif op == "-":
    r = n1-n2
elif op == "*":
    r = n1*n2
else:
    print("operação invalida")
print("o resultado da operação",op,"é:",r)