from Lib import csv
def decrypt_pixel_data(input_csv_file, output_csv_file, shift):
    with open(input_csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        encrypted_pixel_data = list(reader)
    decrypted_pixel_data = []
    for row in encrypted_pixel_data:
        decrypted_row = []
        for pixel in row:
            encrypted_value = int(pixel)
            decrypted_value = (encrypted_value - shift) % 256
            decrypted_pixel = str(decrypted_value)
            decrypted_row.append(decrypted_pixel)
        decrypted_pixel_data.append(decrypted_row)

    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in decrypted_pixel_data:
            writer.writerow(row)

    print("Pixel data decrypted and stored in:", output_csv_file)


