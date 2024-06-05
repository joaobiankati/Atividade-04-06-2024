from funcoes import *


def main():
    consumo_internet = int(input("Informe o consumo de internet em Mb: "))
    consumo_local = int(input("Informe o consumo de minutos locais: "))
    consumo_interurbana = int(input("Informe o consumo de minutos interurbanos: "))
    consumo_torpedo = int(input("Informe o consumo de torpedos: "))

    resultado = calcular_fatura(consumo_internet, consumo_local, consumo_interurbana, consumo_torpedo)
    print(f"Total sem desconto: {resultado['total_fatura_sem_desconto']}")
    print(f"Tipo de desconto aplicado: {resultado['tipo_desconto']}")
    print(f"Valor do desconto: {resultado['valor_desconto']}")
    print(f"Valor total com desconto: {resultado['valor_total_com_desconto']}")

main()