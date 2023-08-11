import cv2
import numpy as np

image = cv2.imread('images/DFT_no_log.tif', cv2.IMREAD_GRAYSCALE)

# 对数变换 logaritmic transformation
# s = c * log(1 + r)
c = 1
image_log = c * np.log1p(image)
# image_log = np.array(image_log, dtype=np.uint8) # 转换数据类型

max_pixel = np.max(image_log)
min_pixel = np.min(image_log)

print('max_pixel: ', max_pixel)
print('min_pixel: ', min_pixel)

# 将图像线性缩放到 0-255
image_log = (image_log - min_pixel) / (max_pixel - min_pixel) * 255

# 转换数据类型
image_log = np.array(image_log, dtype=np.uint8) # 转换数据类型

# 将原始图像和对数变换后的图像拼接在一起
combined_image = cv2.hconcat([image, image_log])

cv2.imwrite('images/DFT_log.png', combined_image)