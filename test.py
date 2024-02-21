from aicsimageio import AICSImage
from skimage.restoration import denoise_nl_means, estimate_sigma
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import plotly.graph_objects as go


file_path = './Sample8 e-DR NOdye-bound GUV 50mM sucrose_Actin_NP-open_2 mM ATP-11.czi'
img = AICSImage(file_path)

data = img.get_image_data("ZYX", C=1)

# 估算图像噪声标准差
sigma_est = np.mean(estimate_sigma(data))
print()
# 使用非局部均值去噪
patch_kw = dict(patch_size=5,  # 5x5 修补块
                patch_distance=6)  # 考虑6个像素内的修补块
print(1)

denoised_data = denoise_nl_means(data, h=1.15 * sigma_est, fast_mode=True, **patch_kw)
print(2)
fig = go.Figure(data=go.Isosurface(
    x=np.linspace(0, denoised_data.shape[2]-1, denoised_data.shape[2]).flatten(),
    y=np.linspace(0, denoised_data.shape[1]-1, denoised_data.shape[1]).flatten(),
    z=np.linspace(0, denoised_data.shape[0]-1, denoised_data.shape[0]).flatten(),
    value=denoised_data.flatten(),
    isomin=0.2,  # 可能需要根据 denoised_data 调整
    isomax=0.8,  # 可能需要根据 denoised_data 调整
    opacity=0.5,  # 减少以提高渲染速度
    surface_count=5,  # 减少表面数量以提高处理速度
))
print(3)

# ax.bar3d(x, y, bottom, width, depth, top, shade=True)
fig.write_image('3d_plot.png')
# plt.close(fig)