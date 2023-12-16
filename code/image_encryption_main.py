#import csv
#import decrypted_csv_to_image_conversion
#import decrypted_data_csv
import encrypted_csv_to_image
import encrypted_data_csv
import RGB_decryption
import RGB_encryption
import RGB_extraction
import encrypted_data_csv
import PIL
import numpy as np


if __name__ == "__main__":
    img=input("Enter the image name: ")
    image_path = f"{img}"
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

height=int(input("Enter height: "))
width=int(input("Enter width: "))

encrypted_csv_to_image.csv_to_image(width,height)
