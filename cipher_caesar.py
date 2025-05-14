alphabeta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']

def encrypt(text, shift):
    ciphered_word = ''

    for letter in text:
        if letter not in text:
            ciphered_word += letter


        shifted_pos = alphabeta.index(letter) + shift
        shifted_pos %= len(alphabeta)
        ciphered_word += alphabeta[shifted_pos]

    return ciphered_word

def decrypt(text, shift):
    original_word = ''

    for letter in text:
        shifted_pos = alphabeta.index(letter) - shift
        shifted_pos %= len(alphabeta)
        original_word += alphabeta[shifted_pos]

    return original_word
