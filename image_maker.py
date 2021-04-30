import cv2
import numpy as np

drawing = False  # true if mouse is pressed
ix, iy = -1, -1
line_thick = 25  # change this for each image of same alphabet


def alphabet_draw(event, x, y, flags, param):  # flags and param are some arguments req. for the setMouseCallBack
    global ix, iy, drawing, line_thick

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (ix, iy), (x, y), (0, 0, 0), line_thick)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), (x, y), (0, 0, 0), line_thick)


img = np.zeros((512, 512, 3), np.uint8) + 255  # White image
cv2.namedWindow('image')  # make a window
cv2.setMouseCallback('image', alphabet_draw)  # call a fn on a window


def remove_borders(image):
    # img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img2 = image[:, :, 0] / 3 + image[:, :, 1] / 3 + image[:, :, 2] / 3
    v_s = 0
    v_e = img2.shape[0]

    h_s = 0
    h_e = img2.shape[1]

    for i in range(img2.shape[0]):
        if np.min(img2[i, :]) > 30:
            v_s += 1
        else:
            break
    for i in reversed(range(img2.shape[0])):
        if np.min(img2[i, :]) > 30:
            v_e -= 1
        else:
            break
    for i in range(img2.shape[1]):
        if np.min(img2[:, i]) > 30:
            h_s += 1
        else:
            break
    for i in reversed(range(img2.shape[1])):
        if np.min(img2[:, i]) > 30:
            h_e -= 1
        else:
            break

    # Slicing that image
    img3 = img2[v_s:v_e, h_s:h_e]
    # Maintaining the aspect ratio
    ih = h_e - h_s
    iv = v_e - v_s
    if ih > iv:
        p = int((ih - iv) / 2)
        img4 = np.pad(np.array(img3), ((p, p), (0, 0)), 'constant', constant_values=(255, 255))
    else:
        p = int((iv - ih) / 2)
        img4 = np.pad(np.array(img3), ((0, 0), (p, p)), 'constant', constant_values=(255, 255))
    img5 = cv2.resize(img4, (10, 10))
    return img5


def start_draw():  # Displays the drawing screen
    while 1:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # Escape key to quit
            break
    img_border = remove_borders(img)
    name = input("Name of img ")
    cv2.imwrite(name + ".jpeg", img_border)
    img_2_vec(img_border)
    cv2.destroyAllWindows()


def img_2_vec(image):
    vec = np.reshape(image, (1, 100))
    for i in range(vec.shape[1]):
        if vec[0][i] != 0:
            vec[0][i] = 1

    array = np.array(vec.astype(int))
    lst = array.tolist()
    # print(array)
    with open('Output.txt', 'a') as f:
        for item in lst:
            f.write("%s\n" % item)


start_draw()
