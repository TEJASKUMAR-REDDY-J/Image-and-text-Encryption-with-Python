from PIL import Image
import numpy as np
import csv

def image_to_csv(image_path, output_path_part1, output_path_part2, output_path_part3):
    image = Image.open(image_path)
    image_np = np.array(image)

    image_np_part1 = image_np[:len(image_np) // 3]
    image_np_part2 = image_np[len(image_np) // 3: 2 * len(image_np) // 3]
    image_np_part3 = image_np[2 * len(image_np) // 3:]
    with open(output_path_part1, 'w', newline='') as csvfile1:
        csv_writer1 = csv.writer(csvfile1)
        for y in range(image_np_part1.shape[0]):
            for x in range(image_np_part1.shape[1]):
                r, g, b = image_np_part1[y, x]
                csv_writer1.writerow([r, g, b])

    with open(output_path_part2, 'w', newline='') as csvfile2:
        csv_writer2 = csv.writer(csvfile2)
        for y in range(image_np_part2.shape[0]):
            for x in range(image_np_part2.shape[1]):
                r, g, b = image_np_part2[y, x]
                csv_writer2.writerow([r, g, b])

    with open(output_path_part3, 'w', newline='') as csvfile3:
        csv_writer3 = csv.writer(csvfile3)
        for y in range(image_np_part3.shape[0]):
            for x in range(image_np_part3.shape[1]):
                r, g, b = image_np_part3[y, x]
                csv_writer3.writerow([r, g, b])