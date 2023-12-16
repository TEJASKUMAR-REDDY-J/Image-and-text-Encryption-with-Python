import csv

import row


def combine_csv_files(input_files, output_file):
    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        for file in input_files:
            with open(file, 'r', newline='') as input:
                reader = csv.reader(input)
                for row in reader:
                    writer.writerow(row)


input_files = ['image_data_part1_decrypted.csv', 'image_data_part2_decrypted.csv', 'image_data_part3_decrypted.csv']
output_file = 'decrypted_image.csv'

if __name__ == "__main__":
    output_file = "decrypted_image.csv"

combine_csv_files(input_files, output_file)