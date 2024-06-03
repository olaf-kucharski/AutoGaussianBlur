import cv2
import random

images = ["landscape.png"]

image = cv2.imread("landscape.png")

for img in images:
    print(img[0:img.index('.')], img[img.index('.'):])
    image = cv2.imread(f'{img}')
    # losowanie rozmycia
    rand = random.randrange(3, 16, 1)
    print(rand)

    # definicja filtrów
    Gaussian = cv2.GaussianBlur(image, (rand, rand), 0)

    # zapisywanie
    cv2.imwrite(f"{img[0:img.index('.')]}_Gaussian{img[img.index('.'):]}", Gaussian)
