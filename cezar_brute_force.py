from cezar import szyfr_cezara

def cezar_brute_force(text):
    common_letters = "AEOZINR"
    for i in range(26):
        result = szyfr_cezara(text, 26-i)
        score = 0
        for l in result:
            if l in common_letters:
                score+=1
        print(f"{szyfr_cezara(text, 26-i)} (Klucz: {i}) (Wynik: {score})")

        # naprawione