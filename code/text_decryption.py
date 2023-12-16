def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A' ) - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a' ) - shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        ciphertext = file.read()

    decrypted_text = caesar_decrypt(ciphertext, shift)

    with open(output_file, 'w') as file:
        file.write(decrypted_text)