# Jak używać programu do szyfrowania sposobem Vigenera

Szyfr Vigenera wykorzystuje klucz (ciąg liter), który jest powtarzany i używany do przesuwania kolejnych liter tekstu.

## Szyfrowanie 

Aby zaszyfrować tekst, używana jest funkcja `vigenere`:

```python
from vigenere import vigenere

tekst = "HELLO WORLD"
klucz = "KEY"

zaszyfrowany = vigenere(text, key)
print(zaszyfrowany)
```