from cezar import *
import pytest

@pytest.mark.basic
def test_cezar_basic():
    assert szyfr_cezara('ABC', 1) == 'BCD'

@pytest.mark.basic
def test_cezar_wrap():
    assert szyfr_cezara('XYZ', 3) == 'ABC'

@pytest.mark.basic
@pytest.mark.parametrize('a,k,expected', [
    ('CDE', -2, 'ABC'),
    ('ZAB', -2, 'XYZ'),
], ids=[
    "Prosty przypadek",
    "Koniec alfabetu"
])
def test_cezar_decrypt(a, k, expected):
    assert szyfr_cezara(a, k) == expected

@pytest.mark.basic
def test_cezar_empty():
    assert szyfr_cezara('', 1) == ''

@pytest.mark.exceptions
def test_cezar_wrongType():
    with pytest.raises(TypeError):
        szyfr_cezara(2,2)

@pytest.mark.basic
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

@pytest.fixture
def key():
    return 2

@pytest.mark.parametrize("txt,expected", [
    ("HELLO","JGNNQ"),
    ("TEST", "VGUV"),
    ("!? ","!? "),
    ("@#*","@#*")
])

@pytest.mark.extended
def test_cezar_shift2(txt, key, expected):
    assert szyfr_cezara(txt, key) == expected
