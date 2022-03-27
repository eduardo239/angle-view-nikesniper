import cv2

def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)


def save_new_image(img):
    img = cv2.imread(img)
    rows, cols, _ = img.shape
    # print("cols = {}, rows = {}".format(cols, rows))
    cropped = img[762:930, 1098:1266]
    zoomed_and_cropped = zoom(cropped, 3)
    # cv2.imshow("zoom", zoomed_and_cropped)
    # cv2.waitKey()
    cv2.imwrite("new_screenshot.jpg", zoomed_and_cropped)