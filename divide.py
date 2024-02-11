# step 1: divide the string into n parts
def divide_string(string, parts):
    part_length = len(string) // parts
    divided_parts = []

    for i in range(parts):
        start_index = i * part_length
        end_index = (i + 1) * part_length
        divided_parts.append(string[start_index:end_index])

    return divided_parts

# Main function
if __name__ == "__main__":
    # take the input from the text file
    input_string = open("cipher_text_one.txt", "r")
    num_parts = input("Enter the number of parts to divide the string into: ")

    # Divide the string into n parts
    divided_string = divide_string(input_string.read(), int(num_parts))

    # Print each part
    for i, part in enumerate(divided_string):
        print(f"Part {i + 1}: {part}")
