nome_user = input("Qual seu nome de usuario? ")
senha = input("Insira uma senha: ")

while senha == nome_user:
    senha = input("Informe uma senha que não contenha o nome do usuario: ")