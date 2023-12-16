from Lib import csv


def encrypt_pixel_data(input_csv_file, output_csv_file, shift):
    with open(input_csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        pixel_data = list(reader)

    encrypted_pixel_data = []
    for row in pixel_data:
        encrypted_row = []
        for pixel in row:
            pixel_value = int(pixel)
            encrypted_value = (pixel_value + shift) % 256
            encrypted_pixel = str(encrypted_value)
            encrypted_row.append(encrypted_pixel)
        encrypted_pixel_data.append(encrypted_row)
    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in encrypted_pixel_data:
            writer.writerow(row)

    print("Pixel data encrypted and stored in:", output_csv_file)