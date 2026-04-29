def szyfr_cezara(tekst, klucz):
    """
    Szyfruje tekst za pomocą szyfru Cezara.

    Args:
        text: tekst do zaszyfrowania
        key: klucz, przesunięcie

    Returns:
        Zaszyfrowany tekst

    Raises:
        TypeError: jeśli zły typ danych
    """

    if not isinstance(tekst, str) or not isinstance(klucz, int):
        raise TypeError("zły typ danych")

    wynik = ""
    for znak in tekst:
        znak = znak.upper()
        if znak.isalpha():
            if znak.isupper():
                podstawa = ord('A')
            else:
                podstawa = ord('a')

            nowy_znak = chr((ord(znak) - podstawa + klucz) % 26 + podstawa)
            wynik += nowy_znak
        else:
            wynik += znak
    return wynik
