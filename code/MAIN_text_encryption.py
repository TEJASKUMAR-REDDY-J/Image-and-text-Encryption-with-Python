import text_encryption



if __name__ == "__main__":
    input_file_path = "input_text.txt"
    output_file_path = "output_encrypted.txt"
    shift_value = 13
    text_encryption.caesar_encrypt(input_file_path, shift_value)

    text_encryption.encrypt_file(input_file_path, output_file_path, shift_value)

encrypt_txt = open("output_encrypted.txt")
print(encrypt_txt.read())
