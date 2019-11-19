# Brady Bellini 
# I certify this is my own work

import string

alphabet = list(string.ascii_lowercase)
cipher = []

def encrypt():
    encrypted = []
    original = []
    with open("secret.txt", "r") as file:
        for letter in file.read():
            if letter in alphabet:
                index = alphabet.index(letter.lower())
                original.append(index)
                cipher_numbers = (index + 3) % 26
                encrypted.append(cipher_numbers)
    for i in range(len(encrypted)):
        cipher.append(alphabet[encrypted[i]])
    return ''.join(str(i) for i in cipher)

def decrypt(key):
    enc = []
    original = []
    og_2 = []
    print(key)
    for letters in key:
        enc.append(letters) 
        if letters in alphabet:
            key_index = alphabet.index(letters)
            og_index = (key_index - 3) % 26
            original.append(og_index)
    for i in range(len(original)):
        og_2.append(alphabet[original[i]])
    return ''.join(str(i) for i in og_2)



if __name__ == "__main__":
    print(decrypt(encrypt()))


