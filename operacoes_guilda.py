def registrar_aventureiro(guilda):
    id_registro = input("Digite o ID de registro na Guilda: ")
    
    if id_registro in guilda:
        print("Aventureiro já registrado!")
        return
    
    nome = input("Nome do aventureiro: ")
    nivel = int(input("Nível inicial: "))
    gold = float(input("Gold inicial: "))
    
    guilda[id_registro] = {"nome": nome, "nivel": nivel, "gold": gold, "inventario": []}
    print("Aventureiro registrado com sucesso!")

def subir_nivel(guilda):
    id_registro = input("Digite o ID do aventureiro: ")
    
    if id_registro not in guilda:
        print("Aventureiro não encontrado!")
        return
        
    niveis = int(input("Quantos níveis o aventureiro subiu? "))
    guilda[id_registro]["nivel"] += niveis
    print(f"Nível atual: {guilda[id_registro]['nivel']}")

def depositar_gold(guilda):
    id_registro = input("Digite o ID do aventureiro: ")
    
    if id_registro not in guilda:
        print("Aventureiro não encontrado!")
        return
    
    valor = float(input("Quantidade de Gold para depositar: "))
    guilda[id_registro]["gold"] += valor
    print("Gold depositado no cofre!")

def retirar_gold(guilda):
    id_registro = input("Digite o ID do aventureiro: ")
    
    if id_registro not in guilda:
        print("Aventureiro não encontrado!")
        return
    
    valor = float(input("Quantidade de Gold para retirar: "))
    
    if valor > guilda[id_registro]["gold"]:
        print("Gold insuficiente no cofre!")
    else:
        guilda[id_registro]["gold"] -= valor
        print("Gold retirado com sucesso!")

def ver_status(guilda):
    id_registro = input("Digite o ID do aventureiro: ")
    
    if id_registro not in guilda:
        print("Aventureiro não encontrado!")
        return
    
    aventureiro = guilda[id_registro]
    
    print("\n--- STATUS ---")
    print("Nome:", aventureiro['nome'])
    print("Nível:", aventureiro['nivel'])
    print("Gold:", aventureiro['gold'])
    print("Inventário:", aventureiro['inventario'])

def comprar_itens(guilda):
    id_registro = input("Digite o ID do aventureiro: ")
    
    if id_registro not in guilda:
        print("Aventureiro não encontrado!")
        return

    aventureiro = guilda[id_registro]
    nivel = aventureiro["nivel"]

    print("\n--- MERCADO ---")
    print(" 1 - Poção de HP (50 Gold) [Livre]")
    print(" 2 - Poção de Mana (50 Gold) [Livre]")
    print(" 3 - Espada de Ferro (25 Gold) [Lvl 0+]")
    print(" 4 - Armadura de Ferro (25 Gold) [Lvl 0+]")
    print(" 5 - Espada de Aço (125 Gold) [Lvl 10+]")
    print(" 6 - Armadura de Aço (125 Gold) [Lvl 10+]")
    print(" 7 - Espada de Adamantina (625 Gold) [Lvl 20+]")
    print(" 8 - Armadura de Adamantina (625 Gold) [Lvl 20+]")
    print(" 9 - Espada de Mytril (3125 Gold) [Lvl 30+]")
    print("10 - Armadura de Mytril (3125 Gold) [Lvl 30+]")
    print("11 - Anel das Chamas (1500 Gold) [Lvl 20+]")
    print("12 - Anel do Titã (1500 Gold) [Lvl 20+]")
    print("13 - Sair")

    opcao = input("Escolha o número do item: ")

    item = ""
    preco = 0
    nivel_minimo = 0

    if opcao == "1":
        item = "Poção de HP"
        preco = 50
        nivel_minimo = 0
    elif opcao == "2":
        item = "Poção de Mana"
        preco = 50
        nivel_minimo = 0
    elif opcao == "3":
        item = "Espada de Ferro"
        preco = 25
        nivel_minimo = 0
    elif opcao == "4":
        item = "Armadura de Ferro"
        preco = 25
        nivel_minimo = 0
    elif opcao == "5":
        item = "Espada de Aço"
        preco = 125
        nivel_minimo = 10
    elif opcao == "6":
        item = "Armadura de Aço"
        preco = 125
        nivel_minimo = 10
    elif opcao == "7":
        item = "Espada de Adamantina"
        preco = 625
        nivel_minimo = 20
    elif opcao == "8":
        item = "Armadura de Adamantina"
        preco = 625
        nivel_minimo = 20
    elif opcao == "9":
        item = "Espada de Mytril"
        preco = 3125
        nivel_minimo = 30
    elif opcao == "10":
        item = "Armadura de Mytril"
        preco = 3125
        nivel_minimo = 30
    elif opcao == "11":
        item = "Anel das Chamas"
        preco = 1500
        nivel_minimo = 20
    elif opcao == "12":
        item = "Anel do Titã"
        preco = 1500
        nivel_minimo = 20
    elif opcao == "13":
        print("Saindo...")
        return
    else:
        print("Opção inválida!")
        return

    if nivel < nivel_minimo:
        print(f"Você precisa ser nível {nivel_minimo} para comprar isso!")
        return

    if aventureiro["gold"] < preco:
        print("Gold insuficiente!")
        return

    aventureiro["gold"] = aventureiro["gold"] - preco
    aventureiro["inventario"].append(item)
    print(f"Você comprou: {item}")

def gerenciar_inventario(guilda):
    id_registro = input("Digite o ID do aventureiro: ")
    
    if id_registro not in guilda:
        print("Aventureiro não encontrado!")
        return
        
    inventario = guilda[id_registro]["inventario"]
    
    if len(inventario) == 0:
        print("Sua bolsa está vazia!")
        return
        
    print("\n--- INVENTÁRIO ---")
    for indice, item in enumerate(inventario):
        print(f"{indice + 1} - {item}")
        
    escolha = int(input("Digite o número do item para descartar (ou 0 para sair): "))
    
    if escolha == 0:
        return
        
    if 1 <= escolha <= len(inventario):
        item_removido = inventario.pop(escolha - 1)
        print(f"O item '{item_removido}' foi jogado fora!")
    else:
        print("Número inválido!")