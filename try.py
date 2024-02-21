from aicsimageio import AICSImage
import math
import matplotlib.pyplot as plt
import numpy as np


file_path = './Sample8 e-DR NOdye-bound GUV 50mM sucrose_Actin_NP-open_2 mM ATP-11.czi'
img = AICSImage(file_path)

data = img.get_image_data("ZYX", C=1)
stacks_mean = []
print(0)
    
normalized_data = np.zeros_like(data)
for z in range(data.shape[0]):
    layer_mean = np.mean(data[z])
    stacks_mean.append(layer_mean)
    normalized_data[z] = data[z] - layer_mean
    
selected_layers = [0, data.shape[0] // 2, data.shape[0] - 1]  # 例如，选择第一层、中间一层和最后一层


print(1)
# 创建图形来展示选定的层
fig, axes = plt.subplots(1, len(selected_layers), figsize=(15, 5))
for i, z in enumerate(selected_layers):
    ax = axes[i]
    ax.imshow(normalized_data[z], cmap='gray')
    ax.set_title(f'Layer {z}')
    ax.axis('off')
print(2)
plt.tight_layout()
print(3)
plt.savefig('test.png')