import cv2
from algorithm import AlgorithmBase

class GrayscaleHistogramStretching(AlgorithmBase):
    def __init__(self):
        super().__init__("Histogram Stretching")

    def run(self, image, out):
        img = cv2.imread(image, 0)
        equ = cv2.equalizeHist(img)
        cv2.imwrite(out, equ)
        cv2.waitKey()
        cv2.destroyAllWindows()

class RGBHistogramStretching(AlgorithmBase):
    def __init__(self):
        super().__init__("Histogram Stretching")

    def run(self, image, out):
        img = cv2.imread(image)
        b, g, r = cv2.split(img)
        bH = cv2.equalizeHist(b)
        gH = cv2.equalizeHist(g)
        rH = cv2.equalizeHist(r)
        # 合并每一个通道
        result = cv2.merge((bH, gH, rH))
        cv2.imwrite(out, result)
        cv2.waitKey()
        cv2.destroyAllWindows()

