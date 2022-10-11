#Tendo como dado de entrada a altura(h) de uma pessoa,construa um algoritmo que calcule seu peso ideal, utilizando as seguintes formulas.

sexo = input("Informe seu sexo, M para masculino e F para feminino: ")

h = float(input("Informa sua altura: "))

if sexo == 'M' or 'm':
    peso = (72.7*h)- 58
else:
    peso = (62.1*h) - 44.7
    
print("Seu peso ideal é: ", peso)