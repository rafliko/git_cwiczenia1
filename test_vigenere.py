import pytest
from decrypt_vigenere import decrypt_vigenere
from vigenere import vigenere

@pytest.mark.basic
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
@pytest.mark.exceptions
@pytest.mark.parametrize(
    "text,key,expected",
    [
        ("abc", "b", "BCD"),
        ("abc", "c", "CDE"),
        ("abc", "d", "CDE"),
        ("xyz", "b", "YZA"),
        ("ABC", "b", "BCD"),
        ("abc", "B", "BCD"),
    ],
    ids=[
        "shift_1",
        "shift_2",
        "shift_3",
        "wrap_around",
        "uppercase",
        "mixed_cases",

    ]
)
def test_vigenere_mixed(text, key, expected):
    assert vigenere(text, key) == expected

@pytest.mark.extended
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



@pytest.mark.parametrize(
    "text,shift,expected",
    [
        ("cde", "2", "ABC"),
        ("abc", "3", "XYZ"),

    ],
    ids=[
        "decrypt",
        "decrypt_wrap",
    ]
)
def test_vigenere_decrypt(text, shift, expected):
    assert decrypt_vigenere(text, shift) == expected

@pytest.fixture
def key():
    return "KEY"

@pytest.mark.parametrize(
    "text,expected",
    [
        ("HELLO", "RIJVS"),
        ("TEST!","DIQD!"),
        ("A B!","K Z?"),

    ],
    ids=[
        "basic",
        "special_char",
        "special_char_2",
    ]
)
def test_viginere_decrypt(text,expected, key):
    assert decrypt_vigenere(text, key) == expected

