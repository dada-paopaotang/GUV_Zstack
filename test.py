from aicsimageio import AICSImage
from skimage.restoration import denoise_tv_chambolle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from skimage.restoration import denoise_wavelet


# 加载你的 CZI 文件
file_path = 'Sample8 e-DR NOdye-bound GUV 50mM sucrose_Actin_NP-open_2 mM ATP-11.czi'
img = AICSImage(file_path)

# 获取 Z-stack 数据
data = img.get_image_data("ZYX", C=1)

# 对每个 Z-slice 应用去噪声
#denoised_data = denoise_tv_chambolle(data, weight=0.1)

#
denoised_data = denoise_wavelet(data, method='BayesShrink', mode='soft', rescale_sigma=True)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 创建一个 x, y, z 坐标网格
_x = np.arange(denoised_data.shape[2])
_y = np.arange(denoised_data.shape[1])
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

print(1)
# 为了简化，我们只可视化一个 Z 层
top = denoised_data[15, :, :].ravel()  # 选择一个 Z 层
bottom = np.zeros_like(top)
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)
print(2)
# plt.show()
plt.savefig('filename.png')
print(3)