import pytest
from decrypt_vigenere import decrypt_vigenere
from vigenere import vigenere

def test_vigenere_basic():
    text = "COS"
    key = "A"
    encrypt_vigenere_test = vigenere(text, key)
    decrypt_vigenere_test = decrypt_vigenere(encrypt_vigenere_test, key)
    assert decrypt_vigenere_test == text

def test_aaa_key_a():
    text = "AAA"
    key = "A"
    assert vigenere(text, key) == "AAA"

def test_dl_key():
    text = "ABCDE"
    key = "AB"
    encrypt_vigenere_test = vigenere(text, key)
    decrypt_vigenere_test = decrypt_vigenere(encrypt_vigenere_test, key)
    assert encrypt_vigenere_test == "ACCEE"
    assert decrypt_vigenere_test == text

def test_vigenere_empty():
    with(pytest.raises(ValueError)):
        vigenere("COS", "")
    with(pytest.raises(ValueError)):
        vigenere("COS", None)

def test_modulo_error():
    text = "Z"
    key = "A"
    assert vigenere(text, key) == "A"




