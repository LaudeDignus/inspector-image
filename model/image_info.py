import cv2

def info(path):
    image = cv2.imread(path)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
