import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==============================
# 🎯 自定义参数（可任意修改）
# ==============================
mu = np.array([0, 0])
Sigma = np.array([[1, 0],
                  [0, 1]])

# 检查协方差矩阵正定性
eigvals = np.linalg.eigvals(Sigma)
assert np.all(eigvals > 0), "协方差矩阵必须正定！"

# ==============================
# 📐 构建网格
# ==============================
stds = np.sqrt(np.diag(Sigma))
margin = 3 * np.max(stds)
x = np.linspace(mu[0] - margin, mu[0] + margin, 100)
y = np.linspace(mu[1] - margin, mu[1] + margin, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# ==============================
# 📊 计算 PDF
# ==============================
def multivariate_gaussian_pdf(pos, mu, Sigma):
    n = mu.shape[0]
    diff = pos - mu
    Sigma_inv = np.linalg.inv(Sigma)
    Sigma_det = np.linalg.det(Sigma)
    mahal = np.einsum('...i,ij,...j->...', diff, Sigma_inv, diff)
    norm_const = np.sqrt((2 * np.pi) ** n * Sigma_det)
    return np.exp(-0.5 * mahal) / norm_const

Z = multivariate_gaussian_pdf(pos, mu, Sigma)

# ==============================
# 🖼️ 绘制纯颜色曲面（无网格线）
# ==============================
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 关键：设置 edgecolor='none' 或 linewidth=0 来去除网格线
surf = ax.plot_surface(
    X, Y, Z,
    cmap='viridis',          # 颜色映射（可换为 'plasma', 'coolwarm' 等）
    edgecolor='none',        # 🔥 去掉所有网格线
    antialiased=True         # 平滑表面
)

# 添加颜色条（显示概率密度值对应的颜色）
fig.colorbar(surf, shrink=0.6, aspect=20, label='概率密度')

# 标签与标题
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('概率密度')
ax.set_title(f'二元正态分布（纯色曲面）\nμ={mu}, Σ={Sigma}')

# 可选：调整视角
ax.view_init(elev=30, azim=-60)

plt.tight_layout()
plt.show()