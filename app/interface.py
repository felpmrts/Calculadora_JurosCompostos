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

# CalculosResult function

def exibir_tabela_evolucao(lista_resultado):

    
    print(f"\n{'Mês':<4} | {'Renda Mensal':>18} | {'Total Invest.':>18} | {'Juros Acum.':>18} | {'Total Acum.':>18}")
    print("-" * 90)

    for item in lista_resultado:
        mes = item['mes']
        renda = item['rendimento']
        total_investido = item['total_investido']
        total_juros = item['total_juros_ate_aqui']
        saldo = item['saldo_acumulado']

        print(f"{mes:<4} | R$ {renda:>15,.2f} | R$ {total_investido:>15,.2f} | R$ {total_juros:>15,.2f} | R$ {saldo:>15,.2f}")

    print("-" * 90 + "\n")

#Gerar TXT

def gerar_arquivoTXT(lista_resultado):
    with open("resultado_JurosCompostos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{'Mês':<4} | {'Renda Mensal':>18} | {'Total Invest.':>18} | {'Juros Acum.':>18} | {'Total Acum.':>18}\n")
        arquivo.write("-" * 90)
    
        for item in lista_resultado:
            mes = item['mes']
            renda = item['rendimento']
            total_investido = item['total_investido']
            total_juros = item['total_juros_ate_aqui']
            saldo = item['saldo_acumulado']

            arquivo.write(f"\n{mes:<4} | R$ {renda:>15,.2f} | R$ {total_investido:>15,.2f} | R$ {total_juros:>15,.2f} | R$ {saldo:>15,.2f}")

        arquivo.write(f"\n")
        arquivo.write("-" * 90 + "\n")


# Menu function

def menu():
    executando = True  
    
    while executando:
        clear_screen()
        lista_resultado = []

        try:
            
            print(f"=== Digite o seu patrimônio inicial ===")
            patrimonio_inicial = float(input(">> R$ "))

            clear_screen()

            print(f"=== Digite o seu aporte mensal ===")
            aporte_mensal = float(input(">> R$ "))

            clear_screen()

            print(f"=== Digite uma taxa de juros anual ===")
            tjuros_anual = float(input(">> % "))

            clear_screen()

            print(f"=== Digite o período em anos ===")
            periodo_anual = int(input(">> "))

        except ValueError:
            print("\n[Erro] Por favor, digite apenas números nos campos de valores.")
            time.sleep(2)
            continue # Volta para o início do loop

        clear_screen()
        
        while True:
            print(f"VALORES DIGITADOS:")
            print(f"Início: R$ {patrimonio_inicial} | Aporte: R$ {aporte_mensal} | Juros: {tjuros_anual}% | Tempo: {periodo_anual} anos")
            print("\n=== Os dados estão corretos? (s/n) ===")
            confirmacao = input(">> ").lower()
        
            if confirmacao == 's':
                clear_screen()
                
                calculos.juros_compostos(lista_resultado, patrimonio_inicial, aporte_mensal, tjuros_anual, periodo_anual)
                exibir_tabela_evolucao(lista_resultado)
                
                input("Aperte Enter para continuar...")

                clear_screen()

                print("Você deseja gerar um relatório em .txt da simulação? (s/n): ")
                gerar_txt = input(">> ").lower()
                if gerar_txt == 's':
                    clear_screen()
                    gerar_arquivoTXT(lista_resultado)
                    print("Relatório gerado com sucesso!")
                    time.sleep(3)
                
                
                clear_screen()
                print("Você deseja fazer uma nova simulação? (s/n): ")
                nova_simulacao = input(">> ").lower()
                if nova_simulacao != 's':
                    executando = False 

                break 
            elif confirmacao == 'n':
                print("\nReiniciando preenchimento...")
                time.sleep(2)
                break 
            else:
                print("[Erro] Digite apenas 's' ou 'n'.")
                time.sleep(1)
                clear_screen()

        

        
     
