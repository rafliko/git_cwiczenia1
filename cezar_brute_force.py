from cezar import szyfr_cezara

def cezar_brute_force(text):
    for i in range(26):
        print(f"{szyfr_cezara(text, 26-i)} (Klucz {i})")