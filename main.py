# Autorzy: Rafał Palka, Michał Pawlenka
# Obsługiwane szyfry: Cezar, Vigenere
from cezar import szyfr_cezara
from cezar_brute_force import cezar_brute_force
from vigenere import *
from decrypt_vigenere import *

print(szyfr_cezara("Alan", 3))
cezar_brute_force("Dodq")

print(vigenere('QWERTY', 'ABC'))
print(decrypt_vigenere('QXGRUA', 'ABC'))
