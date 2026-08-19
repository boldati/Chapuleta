from operacoes_guilda import *

def iniciar_guilda():
    registro_guilda = {}
    
    while True:
        print("\n=== SISTEMA DA GUILDA ===")
        print("1 - Registrar Aventureiro")
        print("2 - Subir de Nível")
        print("3 - Depositar Gold")
        print("4 - Retirar Gold")
        print("5 - Ver Status")
        print("6 - Comprar Itens")
        print("7 - Gerenciar Inventário")
        print("8 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_aventureiro(registro_guilda)
        elif opcao == "2":
            subir_nivel(registro_guilda)
        elif opcao == "3":
            depositar_gold(registro_guilda)
        elif opcao == "4":
            retirar_gold(registro_guilda)
        elif opcao == "5":
            ver_status(registro_guilda)
        elif opcao == "6":
            comprar_itens(registro_guilda)
        elif opcao == "7":
            gerenciar_inventario(registro_guilda)
        elif opcao == "8":
            print("Fechando o sistema...")
            break
        else:
            print("Opção inválida!")

iniciar_guilda()