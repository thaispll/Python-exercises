def verificador_ano_bissexto():
    ano = int(input("Digite o ano: "))  # Recebe a entrada do ano

    # Verificação se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")

# Chamada da função para verificar o ano bissexto
verificador_ano_bissexto()