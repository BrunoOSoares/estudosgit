#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = int(input("Informa o peso de peixes pego: "))

limite = 50

excesso = peso > limite

if excesso == True:
    multa = (peso - limite) * 4
    print("O peso trazido foi:", peso , "e o valor a pagar de multa é ", multa )
else:
    print("O peso é inferior à quantidade maxima")
    
