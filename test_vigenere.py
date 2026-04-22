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

@pytest.mark.parametrize(
    "text,key,expected",
    [
        ("abc", "b", "BCD"),
        ("abc", "c", "CDE"),
        ("xyz", "b", "YZA"),
        ("ABC", "b", "BCD"),
        ("abc", "B", "BCD"),
    ],
    ids=[
        "shift_1",
        "shift_2",
        "wrap_around",
        "uppercase",
        "mixed_cases",

    ]
)
def test_vigenere_mixed(text, key, expected):
    assert vigenere(text, key) == expected


@pytest.mark.parametrize(
    "text,key,expected",
    [
        ("", "a", ""),
        ("abc", "", "ABC"),

    ],
    ids=[
        "empty_text",
        "empty_key",
    ]
)
def test_vigenere_cases(text, key, expected):
    assert vigenere(text, key) == expected


