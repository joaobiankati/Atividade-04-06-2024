from funcoes import *


def test_verificar_calculo_custo_true():
    assert calcular_custo(10, 5) == 50


def test_verificar_calculo_custo_false():
    assert not calcular_custo(10, 5) == 49


def test_verificar_custo_total_true():
    assert calcular_custo_total(50, 200, 150, 50) == 195


def test_verificar_custo_total_false():
    assert not calcular_custo_total(49, 199, 149, 49) == 450


def test_verificar_desconto_internet_com_desconto():
    assert calcular_desconto_internet(60) == 3


def test_verificar_desconto_internet_sem_desconto():
    assert calcular_desconto_internet(49) == 0


def test_verificar_desconto_local_com_desconto():
    assert calcular_desconto_local(250) == 25


def test_verificar_desconto_local_sem_desconto():
    assert calcular_desconto_local(199) == 0


def test_verificar_desconto_interurbana_com_desconto():
    assert calcular_desconto_interurbana(160) == 16


def test_verificar_desconto_interurbana_sem_desconto():
    assert calcular_desconto_interurbana(140) == 0


def test_calcular_desconto_torpedo_com_desconto():
    assert calcular_desconto_torpedo(60) == 12


def test_calcular_desconto_torpedo_sem_desconto():
    assert calcular_desconto_torpedo(49) == 0


def test_determinar_tipo_desconto():
    descontos = [10, 20, 5, 30]
    tipo_desconto = determinar_tipo_desconto(descontos)
    assert tipo_desconto == "Torpedo"


def test_verificar_valor_total_com_desconto():
    assert calcular_valor_total_com_desconto(1000,200) == 800


def test_calcular_fatura():
    consumo_internet = 10
    consumo_local = 20
    consumo_interurbana = 5
    consumo_torpedo = 50

    resultado = calcular_fatura(consumo_internet, consumo_local, consumo_interurbana, consumo_torpedo)

    assert resultado["total_fatura_sem_desconto"] == 25
    assert resultado["tipo_desconto"] == "Internet"
    assert resultado["valor_desconto"] == 0
    assert resultado["valor_total_com_desconto"] == 25





