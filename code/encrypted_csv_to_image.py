import numpy as np
import PIL
import matplotlib
import matplotlib.pyplot as plt


def csv_to_image(a,b):
    im_l = np.genfromtxt('encrypted_image.csv', delimiter=',')

    img = np.reshape(im_l, (a,b,3))


    plt.figure()
    plt.imshow(img)


    image = PIL.Image.fromarray(img.astype('uint8'), 'RGB')
    image.save('encrypt.jpg')