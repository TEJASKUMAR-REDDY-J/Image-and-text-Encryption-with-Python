import csv
import decrypted_csv_to_image_conversion
import decrypted_data_csv
#import encrypted_csv_to_image
#import encrypted_data_csv
import RGB_decryption
#import RGB_encryption
#import RGB_extraction
#import PIL
#import numpy as np
from image_encryption_main import height, width

#
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
decrypted_data_csv.combine_csv_files(['image_data_part1_decrypted.csv', 'image_data_part2_decrypted.csv', 'image_data_part3_decrypted.csv'],'decrypted_image.csv')

decrypted_csv_to_image_conversion.decrypt_image(height,width)

