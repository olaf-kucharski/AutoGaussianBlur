import cv2
import random
import os

for img in os.listdir('Pictures'):
    with open(f'Pictures/{img}') as f:
        print(f"{img[0:img.index('.')]}{img[img.index('.'):]}")
        image = cv2.imread(f'Pictures/{img}')

        # losowanie rozmycia
        rand = random.randrange(3, 16, 2)
        print(rand)

        # definicja filtrów
        Gaussian = cv2.GaussianBlur(image, (rand, rand), 0)

        # folder docelowy
        path = f'Zgaussowane/'

        # zapisywanie
        # cv2.imwrite(f"{path}{img[0:img.index('.')]}_Gaussian{img[img.index('.'):]}", Gaussian)
        cv2.imwrite(f"{path}{img}", Gaussian)
