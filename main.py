# Autorzy: Rafał Palka, Michał Pawlenka
# Obsługiwane szyfry: Cezar, Vigenere
from cezar import szyfr_cezara
from cezar_brute_force import cezar_brute_force
from vigenere import *
from decrypt_vigenere import *
import secrets
import string

def gen_random_key(param: int):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(param))

print(szyfr_cezara("Alan", 3))
cezar_brute_force("Dodq")

print(vigenere('QWERTY', 'ABC'))
print(decrypt_vigenere('QXGRUA', 'ABC'))
