# Projekt kryptograficzny



Progam zawiera:
- Szyfr cezara
    - Szyfr cezara to prosty szyfr podstawieniowy, w którym każdą literę tekstu
zastępuje się literą przesuniętą o stałą liczbę pozycji w alfabecie.

- Szyfr Vigenere'a
  - Szyfr Vigenere'a to szyfr polialfabetyczny, w którym każda litera tekstu jest przesuwana o różną liczbę pozycji 
zależną od powtarzanego hasła (klucza).

- Moduł to łamania szyfru Cezara.

## Funkcjonalności



1. Szyfrowanie i deszyfrowanie tekstu przy użyciu szyfru Cezara.
2. Szyfrowanie i deszyfrowanie tekstu przy użyciu szyfru Vigenere'a.
3. Generowanie losowych kluczy.
4. Próba łamania zaszyfrowanych wiadomości.

## Instalacja



Klonowanie repozytorium [repository](https://github.com/rafliko/git_cwiczenia1).

```
git clone https://github.com/rafliko/git_cwiczenia1.git
cd git_cwiczenia1
```

## Uruchomienie



![python logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/120px-Python-logo-notext.svg.png)

`python main.py`

## Struktura projektu



- `main.py` - główny plik programu
- `cezar.py` - implementacja szyfru Cezara
- `vigenere.py` - implementacja szyfru Vigenere'a
- `cezar_brute_force.py` - łamanie szyfru Cezara
