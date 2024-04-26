while True:
    print("[*] Sobre")
    print("[1] Decimal para Binário")
    print("[2] Decimal para Octal")
    print("[3] Decimal para Hexadecimal")
    print("[4] Sair")

    base = input("Escolha uma opção: ")

    if base == "1":
        decimal = int(input("Insira o número decimal a ser convertido: "))
        binary = ""
        while decimal:
            resto = decimal % 2
            decimal = decimal // 2
            binary = str(resto) + binary
        print(f"O número {decimal} em base decimal equivale a 0b{binary} em base binária.")
    
    elif base == "2":
        decimal = int(input("Insira o número decimal a ser convertido: "))
        octal = ""
        while decimal:
            resto = decimal % 8
            decimal = decimal // 8
            octal = str(resto) + octal
        print(f"O número {decimal} em base decimal equivale a {octal} em base octal.")
    
    elif base == "3":
        decimal = int(input("Insira o número decimal a ser convertido: "))
        hex_value = ""
        while decimal:
            resto = decimal % 16
            decimal = decimal // 16
            if resto < 10:
                hex_value = str(resto) + hex_value
            else:
                hex_value = chr(55 + resto) + hex_value
        print(f"O número {decimal} em base decimal equivale a 0x{hex_value} em base hexadecimal.")
    
    elif base == "4":
        print("Obrigado pela visita :)")
        break
    
    elif base == "*":
        print("========================================")
        print("------PROGRAMAÇÃO DE COMPUTADORES------")
        print("========================================")
        print("------COMPONENTES DO GRUPO: GABRIEL LUIGI; RGM: 30144221; KAYKY CANDIDO TEIXEIRA; RGM: 29239575------")
        print("========================================")
        print("------PROGRAMAÇÃO DE COMPUTADORES------")
        print("========================================")
        print("------CONVERSOR DE BASES NUMÉRICAS------")
        print("----------DEC--> BIN/OCTA/HEXA----------")
        print("\n--------------VERSÃO 1.0----------------")
        print("========================================")
    
    else:
        print("Caractere Inválido")