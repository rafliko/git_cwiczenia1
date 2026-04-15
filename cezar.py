def szyfr_cezara(tekst, klucz):
    if not isinstance(tekst, str) or not isinstance(klucz, int):
        raise TypeError("zły typ danych")

    wynik = ""
    for znak in tekst:
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
