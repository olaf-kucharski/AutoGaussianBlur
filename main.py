import cv2
import numpy as np

images = ["landscape.png"]

image = cv2.imread("landscape.png")

for img in images:
    print(img[0:img.index('.')], img[img.index('.'):])
    image = cv2.imread(f'{img}')
    # cv2.imshow('ORIGINAL', image)
    # definicja filtrów
    Gaussian_7 = cv2.GaussianBlur(image, (7, 7), 0)
    Gaussian_15 = cv2.GaussianBlur(image, (15, 15), 0)
    # cv2.imshow('SHARPEN', Gaussian_7)
    # cv2.waitKey(0)
    # zapisywanie
    cv2.imwrite(f"{img[0:img.index('.')]}_Gaussian7{img[img.index('.'):]}", Gaussian_7)
    cv2.imwrite(f"{img[0:img.index('.')]}_Gaussian15{img[img.index('.'):]}", Gaussian_15)
    # cv2.destroyAllWindows()
