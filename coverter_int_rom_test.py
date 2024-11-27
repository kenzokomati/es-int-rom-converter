import pytest
from converter_int_rom import int_to_roman


def test_int_to_roman_valores_unicos():
    # Teste de números romanos com símbolos únicos
    assert int_to_roman(1) == "I"
    assert int_to_roman(5) == "V"
    assert int_to_roman(10) == "X"
    assert int_to_roman(50) == "L"
    assert int_to_roman(100) == "C"
    assert int_to_roman(500) == "D"
    assert int_to_roman(1000) == "M"

def test_int_to_roman_combinacoes():
    # Teste de números romanos com combinações de símbolos
    assert int_to_roman(23) == "XXIII"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(90) == "XC"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(900) == "CM"
    assert int_to_roman(1987) == "MCMLXXXVII"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_int_to_roman_invalid_input():
    # Teste de entradas inválidas
    with pytest.raises(ValueError):
        int_to_roman(0)  # Números menores ou iguais a zero

    with pytest.raises(ValueError):
        int_to_roman(-1)  # Números negativos

    with pytest.raises(ValueError):
        int_to_roman(4.5)  # Números de ponto flutuante

    with pytest.raises(ValueError):
        int_to_roman("texto")  # Entradas não inteiras