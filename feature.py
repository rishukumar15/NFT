import numpy as np
import cv2

imageNames = ['R_1.png','R_2.png','R_3.png','R_4.png','R_5.png',
              'K_1.png','K_2.png','K_3.png','K_4.png','K_5.png',
              'S_1.png','S_2.png','S_3.png','S_4.png','S_5.png']


for imageName in imageNames:
    print(f"Matrix for {imageName}")
    img = cv2.imread(f"{imageName}",0)
    for i in range(10):
        for j in range(10):
            if img[i][j] == 255:
                img[i][j] = 1
            else:
                img[i][j] = 0
    A = np.asarray(img).reshape(-1)
    print(A.tolist())