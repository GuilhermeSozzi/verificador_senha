while True:
    senha = input("Digite sua senha e descubra se ela é válida:")
    caracteres_especiais = '!?,.;:+=*-_'

    if len(senha) < 8:
        print(f"Senha inválida! Senha tem apenas {len(senha)} caracteres. O mínimo é 8.")
    elif not any(caracter.isdigit() for caracter in senha):
        print("Senha inválida. Insira pelo menos 1 caracter numérico a ela.")
    elif not any(caracter in caracteres_especiais for caracter in senha):
        print("Senha inválida. Insira pelo menos um caractere especial nela (Exemplos: ! ; @ ; _)")
    else:
        print("Senha válida.")
        break