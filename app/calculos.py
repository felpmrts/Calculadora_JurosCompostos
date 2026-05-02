def juros_compostos(lista_resultado, capital_inicial, aporte_mensal, tjuros_anual, tempo_anos):
    meses = int(tempo_anos * 12)
    taxa_mensal = (1 + tjuros_anual/100)**(1/12) - 1
    
    saldo_atual = capital_inicial
    total_investido = capital_inicial

    lista_resultado.clear()

    rendimento_mes_0 = capital_inicial * taxa_mensal
    saldo_atual = capital_inicial + rendimento_mes_0

    lista_resultado.append({
        "mes": 0,
        "rendimento": round(rendimento_mes_0, 2),
        "deposito": 0.0,
        "total_investido": round(total_investido, 2),
        "total_juros_ate_aqui": round(saldo_atual - total_investido, 2),
        "saldo_acumulado": round(saldo_atual, 2)
    })

    for mes in range(1, meses):
    
        saldo_antes_do_juros = saldo_atual + aporte_mensal
        total_investido += aporte_mensal
        
        rendimento_mes = saldo_antes_do_juros * taxa_mensal
        saldo_atual = saldo_antes_do_juros + rendimento_mes
        
        dados_mes = {
            "mes": mes,
            "rendimento": round(rendimento_mes, 2),
            "deposito": aporte_mensal,
            "saldo_acumulado": round(saldo_atual, 2),
            "total_juros_ate_aqui": round(saldo_atual - total_investido, 2),
            "total_investido": round(total_investido, 2)
        }
        lista_resultado.append(dados_mes)
    
