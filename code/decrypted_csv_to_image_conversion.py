import numpy as np
import PIL
import matplotlib
import matplotlib.pyplot as plt

def decrypt_image(height1,width1):

    im_l = np.genfromtxt('decrypted_image.csv', delimiter=',')
    img = np.reshape(im_l, (height1, width1, 3))

    plt.figure()
    plt.imshow(img)

    image = PIL.Image.fromarray(img.astype('uint8'), 'RGB')
    image.save('decrypted.jpg')