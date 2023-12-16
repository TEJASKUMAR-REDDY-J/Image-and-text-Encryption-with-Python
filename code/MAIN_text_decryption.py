import text_decryption
if __name__ == "__main__":
    input_file_path = "output_encrypted.txt"
    output_file_path = "output_decrypted.txt"
    shift_value = 13
    text_decryption.decrypt_file(input_file_path, output_file_path, shift_value)

decrypt_txt= open("output_decrypted.txt")
print(decrypt_txt.read())