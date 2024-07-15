import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread('D:\\AIO Exercise\\AIO-Exercise\\download.jpg')

# Lightness


def color2grayscale(vector):
    return np.max(vector)*0.5 + np.min(vector)*0.5


grayscale_1 = np.apply_along_axis(color2grayscale, axis=2, arr=img)
print(grayscale_1[0, 0])

# Average


def color2grayscale(vector):
    return np.sum(vector)/3


grayscale_2 = np.apply_along_axis(color2grayscale, axis=2, arr=img)
print(grayscale_2[0, 0])

# Luminosity


def color2grayscale(vector):
    return vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07


grayscale_3 = np.apply_along_axis(color2grayscale, axis=2, arr=img)
print(grayscale_3[0, 0])
