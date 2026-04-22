from cezar import *
import pytest

def test_cezar_basic():
    assert szyfr_cezara('ABC', 1) == 'BCD'

def test_cezar_wrap():
    assert szyfr_cezara('XYZ', 3) == 'ABC'

def test_cezar_decrypt():
    assert szyfr_cezara('BCD', -1) == 'ABC'

def test_cezar_empty():
    assert szyfr_cezara('', 1) == ''

def test_cezar_wrongType():
    with pytest.raises(TypeError):
        szyfr_cezara(2,2)

@pytest.mark.parametrize('a,k,expected', [
    ('ABC', 2, 'CDE'),
    ('XYZ', 2, 'ZAB'),
    ('abc', 2, 'CDE')
], ids=[
    "Prosty przypadek",
    "Koniec alfabetu",
    "Male litery"
])
def test_cezar_shift(a,k,expected):
    assert szyfr_cezara(a, k) == expected