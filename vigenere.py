def vigenere(text, key):
    key_index = 0
    ret = ""
    for letter in text:
        letter = letter.upper()
        if letter.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            new_letter = (ord(letter) - ord('A') + shift) % (ord('Z')-ord('A'))
            new_letter += ord('A')
            ret += chr(new_letter)
            key_index += 1
        else:
            ret += letter

    return ret

