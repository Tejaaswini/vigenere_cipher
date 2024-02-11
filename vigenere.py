# consolidated vignere decryption code
# step1: divide the string into parts
# step2: frequency analysis
# step3: find repeating sequences
# step4: find key length
# step5: vigenere decryption
# step6: brute force vigenere

import csv
import re
import string

LETTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits


def divide_string(string, parts):
    part_length = len(string) // parts
    divided_parts = []

    for i in range(parts):
        start_index = i * part_length
        end_index = (i + 1) * part_length
        divided_parts.append(string[start_index:end_index])

    return divided_parts


def frequency_analysis(ciphertext):
    frequency = {}

    for char in ciphertext:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequency


def find_repeating_sequences(ciphertext, min_length=3, max_length=5):
    sequences = {}

    for length in range(min_length, max_length + 1):
        for i in range(len(ciphertext) - length):
            sequence = ciphertext[i:i + length]
            if sequence in sequences:
                sequences[sequence].append(i)
            else:
                sequences[sequence] = [i]

    repeating_sequences = {sequence: positions for sequence, positions in sequences.items() if len(positions) > 1}
    sorted_sequences = sorted(repeating_sequences.items(), key=lambda x: len(x[1]), reverse=True)

    return sorted_sequences


def find_key_length(ciphertext):
    sequences = find_repeating_sequences(ciphertext)
    spacings = []

    for sequence, positions in sequences:
        for i in range(len(positions) - 1):
            spacing = positions[i + 1] - positions[i]
            spacings.append(spacing)

    factors = []
    for spacing in spacings:
        for i in range(2, min(20, spacing)):
            if spacing % i == 0:
                factors.append(i)

    unique_factors = list(set(factors))
    counts = {factor: factors.count(factor) for factor in unique_factors}
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    possible_lengths = [item[0] for item in sorted_counts]
    return possible_lengths


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


if __name__ == "__main__":
    input_file = "cipher_text_two.txt"
    num_parts = int(input("Enter the number of parts to divide the string into: "))

    with open(input_file, "r") as file:
        input_string = file.read()

    divided_string = divide_string(input_string, num_parts)

    for i, part in enumerate(divided_string):
        print(f"Part {i + 1}: {part}")

    result = frequency_analysis(input_string)
    print("\nCharacter\tFrequency")
    print("=========================")
    for char, freq in result:
        print(f"{char}\t\t{freq}")

    key_lengths = find_key_length(input_string)
    print("\nThe Kasiski method predicts key sizes of:", key_lengths)

    key_length = int(input("Enter the key length: "))
    output_file = 'decrypted_texts_4.csv'
    brute_force_vigenere(input_string, key_length, output_file)
