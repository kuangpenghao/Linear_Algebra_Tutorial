import numpy as np
import matplotlib.pyplot as plt

# —— 自定义参数 ——
mu = [0, 0]
Sigma = [[2, 1],
         [1, 2]]   # ← 修改这里即可改变分布形状

# 构建网格
x = np.linspace(-3.5, 3.5, 200)
y = np.linspace(-3.5, 3.5, 200)
X, Y = np.meshgrid(x, y)
pos = np.dstack([X, Y])

# 计算 PDF
rv = np.random.multivariate_normal(mu, Sigma, size=0)  # 仅用于说明，实际不用
diff = pos - mu
Sigma_inv = np.linalg.inv(Sigma)
Z = np.exp(-0.5 * np.einsum('...i,ij,...j->...', diff, Sigma_inv, diff))

# 绘制等高线
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)
plt.subplots_adjust(left=0.12, right=0.95, bottom=0.12, top=0.92)
#plt.figure(figsize=(6, 5))
plt.contour(X, Y, Z, levels=12, colors='k')  # 黑色等高线，无填充
plt.axis('equal')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('二元正态分布等高线（协方差矩阵可自定义）')
plt.grid(True, linestyle='--', alpha=0.8)
plt.show()