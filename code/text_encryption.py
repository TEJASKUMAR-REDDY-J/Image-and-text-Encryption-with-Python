def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result


def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        plaintext = file.read()

    encrypted_text = caesar_encrypt(plaintext, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)
