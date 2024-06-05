def calcular_custo(consumo, custo_unitario):
    return consumo * custo_unitario


def calcular_custo_total(consumo_internet, consumo_local, consumo_interurbana, consumo_torpedo):
    desconto_internet = 0.50
    desconto_local = 0.35
    desconto_interurbana = 0.60
    desconto_torpedo = 0.20

    total_internet = calcular_custo(consumo_internet, desconto_internet)
    total_local = calcular_custo(consumo_local, desconto_local)
    total_interurbana = calcular_custo(consumo_interurbana, desconto_interurbana)
    total_torpedo = calcular_custo(consumo_torpedo, desconto_torpedo)

    return total_internet + total_local + total_interurbana + total_torpedo


def calcular_desconto_internet(consumo_internet):
    if consumo_internet > 50:
        return consumo_internet * 0.05

    return 0

def calcular_desconto_local(consumo_local):
    if consumo_local > 200:
        return consumo_local * 0.10

    return 0


def calcular_desconto_interurbana(consumo_interurbana):
    if consumo_interurbana > 150:
        return consumo_interurbana * 0.10

    return 0


def calcular_desconto_torpedo(consumo_torpedo):
    if consumo_torpedo > 50:
        return consumo_torpedo * 0.20

    return 0


def determinar_tipo_desconto(descontos):
    tipos_desconto = ["Internet", "Local", "Interurbana", "Torpedo"]
    maior_desconto_index = descontos.index(max(descontos))
    return tipos_desconto[maior_desconto_index]


def calcular_valor_total_com_desconto(total_fatura_sem_desconto, valor_desconto):
    return total_fatura_sem_desconto - valor_desconto


def calcular_fatura(consumo_internet, consumo_local, consumo_interurbana, consumo_torpedo):
    total_fatura_sem_desconto = calcular_custo_total(consumo_internet, consumo_local, consumo_interurbana,consumo_torpedo)
    desconto_internet = calcular_desconto_internet(consumo_internet)
    desconto_local = calcular_desconto_local(consumo_local)
    desconto_interurbana = calcular_desconto_interurbana(consumo_interurbana)
    desconto_torpedo = calcular_desconto_torpedo(consumo_torpedo)
    descontos = (desconto_internet, desconto_local, desconto_interurbana, desconto_torpedo)
    tipo_desconto = determinar_tipo_desconto(descontos)
    valor_desconto = max(descontos)
    valor_total_com_desconto = calcular_valor_total_com_desconto(total_fatura_sem_desconto, valor_desconto)

    return {
        "total_fatura_sem_desconto": total_fatura_sem_desconto,
        "tipo_desconto": tipo_desconto,
        "valor_desconto": valor_desconto,
        "valor_total_com_desconto": valor_total_com_desconto
    }
