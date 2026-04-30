import os
import time
from app import calculos

# Screen functions

def welcome():
    clear_screen()
    print(f"\n==================================")
    print("  CALCULADORA DE JUROS COMPOSTOS  ")
    print("==================================")

    time.sleep(3)

def bye():
    clear_screen()
    print(f"==================================")
    print(f"    Encerrando o programa...     ")
    print(f"==================================")
    time.sleep(3)
    clear_screen()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Menu function

def menu():
    while True:

        clear_screen()

        lista_resultado = [] #começa vazia

        print(f"=== Digite o seu patrimônio inicial ===\n")
        patrimonio_inicial = float(input(">> R$ "))

        clear_screen()

        print(f"=== Digite o seu aporte mensal ===\n")
        aporte_mensal = float(input(">> R$ "))

        clear_screen()

        print(f"=== Digite uma taxa de juros anual ===\n")
        tjuros_anual = float(input(">> % "))

        clear_screen()

        print(f"=== Digite o período em anos ===\n")
        periodo_anual = float(input(">> "))

        clear_screen()
        
        while True:
            try:
                print("=== Os dados estão corretos? (s/n) ===")
                option = input(">> ")
            
                if option == 's' or option == 'S':
                    clear_screen()
                    calculos.juros_compostos(lista_resultado, patrimonio_inicial, aporte_mensal, tjuros_anual, periodo_anual)
                    break
                if option == 'n' or option == 'N':
                    clear_screen()
                    print("Digite os dados novamente ...")
                    time.sleep(3)
                    break

            except ValueError:
                # Caso o usuário digite algo que não seja uma letra válida
                print("[Erro] Entrada inválida! Por favor, digite apenas as letras 's' ou 'n'.")
                time.sleep(3)
        

        

        
     
