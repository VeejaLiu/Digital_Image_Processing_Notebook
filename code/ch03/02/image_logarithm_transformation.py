import cv2
import numpy as np

image = cv2.imread('images/DFT_no_log.tif', cv2.IMREAD_GRAYSCALE)

# 对数变换 logaritmic transformation
# s = c * log(1 + r)
c = 1
image_log = c * np.log1p(image)
image_log = np.array(image_log, dtype=np.uint8) # 转换数据类型

# 将原始图像和对数变换后的图像拼接在一起
combined_image = cv2.hconcat([image, image_log])

cv2.imwrite('images/DFT_log.png', combined_image)