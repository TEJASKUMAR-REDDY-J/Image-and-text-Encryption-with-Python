import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
import text_encryption
import text_decryption
import encrypted_csv_to_image
import encrypted_data_csv
import RGB_decryption
import RGB_encryption
import RGB_extraction
import encrypted_data_csv
import decrypted_csv_to_image_conversion
import decrypted_data_csv

def button1_click():
    content = text_widget.get("1.0", "end-1c")
    with open("input_text.txt", "w") as file:
        file.write(content)
    print("Text saved to 'input_text.txt'")

    if __name__ == "__main__":
        input_file_path = "input_text.txt"
        output_file_path = "output_encrypted.txt"
        shift_value = 13
        text_encryption.caesar_encrypt(input_file_path, shift_value)

        text_encryption.encrypt_file(input_file_path, output_file_path, shift_value)

    encrypt_txt = open("output_encrypted.txt")
    print(encrypt_txt.read())
    with open("output_encrypted.txt", 'r') as file:
        content = file.read()
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, content)


def button2_click():
    content = text_widget.get("1.0", "end-1c")
    with open("output_encrypted.txt", "w") as file:
        file.write(content)
    print("Text saved to 'input_text.txt'")

    if __name__ == "__main__":
        input_file_path = "output_encrypted.txt"
        output_file_path = "output_decrypted.txt"
        shift_value = 13
        text_decryption.caesar_decrypt(input_file_path, shift_value)

        text_decryption.decrypt_file(input_file_path, output_file_path, shift_value)

    decrypt_txt = open("output_decrypted.txt")
    print(decrypt_txt.read())
    with open("output_decrypted.txt", 'r') as file:
        content = file.read()
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, content)


def button3_click():
    content = text_widget.get("1.0", "end-1c")
    with open("input_image_path.txt", "w") as file:
        file.write(content)
    print("Text saved to 'input_image_path.txt'")
    if __name__ == "__main__":
        with open("input_image_path.txt", "r") as file:
            img = file.readline()
            x = img.split()

        print(img)

        image_path = f"{x[0]}"
        output_path_part1 = "image_data_part1.csv"
        output_path_part2 = "image_data_part2.csv"
        output_path_part3 = "image_data_part3.csv"

        RGB_extraction.image_to_csv(image_path, output_path_part1, output_path_part2, output_path_part3)

    #
    input_csv_file_1 = "image_data_part1.csv"
    output_csv_file_1 = "image_data_part1_encrypted.csv"
    shift_1 = 113

    input_csv_file_2 = "image_data_part2.csv"
    output_csv_file_2 = "image_data_part2_encrypted.csv"
    shift_2 = 251

    input_csv_file_3 = "image_data_part3.csv"
    output_csv_file_3 = "image_data_part3_encrypted.csv"
    shift_3 = 179

    RGB_encryption.encrypt_pixel_data(input_csv_file_1, output_csv_file_1, shift_1)
    RGB_encryption.encrypt_pixel_data(input_csv_file_2, output_csv_file_2, shift_2)
    RGB_encryption.encrypt_pixel_data(input_csv_file_3, output_csv_file_3, shift_3)

    #
    ...
    encrypted_data_csv.combine_csv_files([
        'image_data_part1_encrypted.csv',
        'image_data_part2_encrypted.csv',
        'image_data_part3_encrypted.csv'], "encrypted_image.csv")

    height = int(x[1])
    width = int(x[2])

    encrypted_csv_to_image.csv_to_image(width, height)

    encrypt_img = open("print_encrypt.txt")
    print(encrypt_img.read())
    with open("print_encrypt.txt", 'r') as file:
        content = file.read()
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, content)


def button4_click():
    content = text_widget.get("1.0", "end-1c")
    with open("input_image_path.txt", "w") as file:
        file.write(content)
    print("Text saved to 'input_image_path.txt'")
    if __name__ == "__main__":
        with open("input_image_path.txt", "r") as file:
            img = file.readline()
            x = img.split()

    input_csv_file_1 = "image_data_part1_encrypted.csv"
    output_csv_file_1 = "image_data_part1_decrypted.csv"
    shift_1 = 113

    input_csv_file_2 = "image_data_part2_encrypted.csv"
    output_csv_file_2 = "image_data_part2_decrypted.csv"
    shift_2 = 251

    input_csv_file_3 = "image_data_part3_encrypted.csv"
    output_csv_file_3 = "image_data_part3_decrypted.csv"
    shift_3 = 179

    RGB_decryption.decrypt_pixel_data(input_csv_file_1, output_csv_file_1, shift_1)
    RGB_decryption.decrypt_pixel_data(input_csv_file_2, output_csv_file_2, shift_2)
    RGB_decryption.decrypt_pixel_data(input_csv_file_3, output_csv_file_3, shift_3)

    #
    decrypted_data_csv.combine_csv_files(
        ['image_data_part1_decrypted.csv', 'image_data_part2_decrypted.csv', 'image_data_part3_decrypted.csv'],
        'decrypted_image.csv')

    height = int(x[0])
    width = int(x[1])
    decrypted_csv_to_image_conversion.decrypt_image(height, width)


root = tk.Tk()
root.title("TIDE")
w = Label(root, text='Text or Image: Encryption and Decryption', fg="Black", font="100")
w.pack()

text_widget = tk.Text(root, height=10, width=40)
text_widget.pack(padx=10, pady=10)

button1 = tk.Button(root, text="Text Encryption", command=button1_click, pady=10)
button2 = tk.Button(root, text="Text Decryption", command=button2_click, pady=10)
button3 = tk.Button(root, text="Image Encryption", command=button3_click, pady=10)
button4 = tk.Button(root, text="Image Decryption", command=button4_click, pady=10)

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)

root.geometry('1000x1000')
root.mainloop()