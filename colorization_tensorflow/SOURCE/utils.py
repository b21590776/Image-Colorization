import cv2
import os

"""
print(os.listdir("../DATASET/Gland/test"))

for i in os.listdir("../DATASET/Gland/test"):
    img = cv2.imread("../DATASET/Gland/test/"+i, 0)
    cv2.imwrite("../DATASET/Gland/testGray/"+i, img)
"""

img = cv2.imread("/Users/hadwrf/Downloads/100.jpg", 0)
cv2.imshow("mm", img)
cv2.imwrite("/Users/hadwrf/Downloads/100gray.jpg", img)
cv2.waitKey()
cv2.destroyAllWindows()