email = input("Entre com seu e-mail: ")
nome = email.split("@")[0]
print("Olá, {}".format(nome))
dominio = email.split("@")[1]
print("O domínio do seu e-mail é: http://{}".format(dominio))