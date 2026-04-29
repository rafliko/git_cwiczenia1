# Jak używać szyfru Cezara?

Szyfr Cezara jako klucz wykorzystuje liczbę, która mówi o ile miejsc w alfabecie należy przesunąć daną literę.

---

## Szyfrowanie
Aby zaszyfrować tekst, używamy funkcji `szyfr_cezara`

```python
from cezar import szyfr_cezara

# Wyświetl zaszyfrowany z przesunięciem 3 - DODQ
print(szyfr_cezara("ALAN", 3))
```