#step 2: frequency analysis
def frequency_analysis(ciphertext):
    frequency = {}

    for char in ciphertext:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # sort the dictionary by values in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequency

# read the ciphertext from the file
ciphertext = open("cipher_text_one.txt", "r")
result = frequency_analysis(ciphertext.read())

print("Character\tFrequency")
print("=========================")
for char, freq in result:
    print(f"{char}\t\t{freq}")
