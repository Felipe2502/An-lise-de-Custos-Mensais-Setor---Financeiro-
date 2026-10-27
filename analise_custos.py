metas = {"jan": 1000, "fev": 1200, "mar": 1100}
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

# Loop que percorre cada mês do dicionário de metas
for mes in metas:
    meta = metas[mes]
    gasto = gastos[mes]

    # Condicional para verificar a situação do orçamento
    if gasto <= meta:
        print(f"Mês {mes}: Dentro do orçamento.")
    else:
        diferenca = gasto - meta
        print(f"Mês {mes}: Orçamento estourado em R${diferenca}.")