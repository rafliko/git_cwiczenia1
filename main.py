# Autorzy: Rafał Palka, Michał Pawlenka
# Obsługiwane szyfry: Cezar, Vigenere
from cezar import szyfr_cezara
from cezar_brute_force import cezar_brute_force
from vigenere import *
from decrypt_vigenere import *
import secrets
import string
import time

def gen_random_key(param: int):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(param))

start_time = time.time()
print(szyfr_cezara("Alan", 3))
c_time = time.time() - start_time
print(f"Czas wykonania {c_time}")
cezar_brute_force("Dodq")

start_time = time.time()
print(vigenere('QWERTY', 'ABC'))
v_time = time.time() - start_time
print(f"Czas wykonania {v_time}")
print(decrypt_vigenere('QXGRUA', 'ABC'))

print(f"Różnica w czasie: {abs(v_time - c_time)}")
