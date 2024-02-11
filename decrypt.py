# step 4: decrypt the text

import csv
import string

LETTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ''
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char in LETTERS:
            key_char = key[key_index % key_length]
            key_index += 1

            key_position = LETTERS.index(key_char)
            ciphertext_position = LETTERS.index(char)

            decrypted_position = (ciphertext_position - key_position) % len(LETTERS)
            decrypted_char = LETTERS[decrypted_position]

            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def brute_force_vigenere(ciphertext, key_length, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Key', 'Decrypted Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(len(LETTERS) ** key_length):
            key = ''
            num = i
            for _ in range(key_length):
                key = LETTERS[num % len(LETTERS)] + key
                num //= len(LETTERS)

            decrypted_text = vigenere_decrypt(ciphertext, key)
            try:
                writer.writerow({'Key': key, 'Decrypted Text': decrypted_text.encode('utf-8').decode('utf-8')})
            except UnicodeDecodeError:
                writer.writerow({'Key': key, 'Decrypted Text': decrypted_text})

ciphertext = open("cipher_text_one.txt", "r").read()
key_length = input("Enter the key length: ")
output_file = 'decrypted_texts_3.csv'

brute_force_vigenere(ciphertext, key_length, output_file)
