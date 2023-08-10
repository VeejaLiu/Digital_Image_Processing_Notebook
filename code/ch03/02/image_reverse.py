import cv2

# 读取灰度图像
image = cv2.imread('images/digital_Xray.tif', cv2.IMREAD_GRAYSCALE)

# s = L - 1 - r
L = 255
# 反转图像
image_reverse = L - 1 - image

# 将原始图像和反转图像拼接在一起
combined_image = cv2.hconcat([image, image_reverse])

cv2.imwrite('images/digital_Xray_reverse.png', combined_image)
