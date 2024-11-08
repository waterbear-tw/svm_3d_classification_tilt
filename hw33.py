import numpy as np
from sklearn.svm import LinearSVC
import plotly.graph_objects as go
import streamlit as st

# 設定標題
st.title("3D SVM Classification with Adjustable Distance Threshold and Hyperplane Tilt")

# 步驟 1: 生成 600 個隨機點，並根據距離分成兩類
np.random.seed(42)
n_points = 600

# 隨機產生 x1, x2，分佈在 (0,0) 且方差為 10 的高斯分佈內
x1 = np.random.normal(0, 10, n_points)
x2 = np.random.normal(0, 10, n_points)

# 計算每個點到原點的距離
distances = np.sqrt(x1**2 + x2**2)

# 設定 Streamlit 的滑桿來調整距離閾值
threshold = st.slider("Distance Threshold for Classification", min_value=1.0, max_value=10.0, value=4.0, step=0.5)

# 根據距離分類：距離小於閾值的標記為 0，其餘為 1
y = np.where(distances < threshold, 0, 1)

# 步驟 2: 定義高斯函數來產生第三個維度 x3
def gaussian_function(x1, x2):
    return np.exp(-0.5 * (x1**2 + x2**2) / 10)

# 計算 x3，並將 x1, x2 和 x3 合併成三維特徵矩陣 X
x3 = gaussian_function(x1, x2)
X = np.column_stack((x1, x2, x3))

# 步驟 3: 使用 LinearSVC 來訓練模型
svc_model = LinearSVC()
svc_model.fit(X, y)

# 獲取模型的係數和截距，用來繪製分隔超平面
coef = svc_model.coef_
intercept = svc_model.intercept_

# 設定 Streamlit 滑桿來調整超平面傾斜度
tilt_factor_x = st.slider("Tilt Factor for X-axis", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
tilt_factor_y = st.slider("Tilt Factor for Y-axis", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

# 步驟 4: 視覺化
# 創建 3D 散點圖
fig = go.Figure()

# 將類別為 0 的點繪製成藍色，類別為 1 的點繪製成紅色
fig.add_trace(go.Scatter3d(
    x=x1[y == 0],
    y=x2[y == 0],
    z=x3[y == 0],
    mode='markers',
    marker=dict(color='blue', size=5),
    name='Class 0'
))

fig.add_trace(go.Scatter3d(
    x=x1[y == 1],
    y=x2[y == 1],
    z=x3[y == 1],
    mode='markers',
    marker=dict(color='red', size=5),
    name='Class 1'
))

# 計算分隔超平面的 z 值
# 在超平面方程式中加入 tilt_factor_x 和 tilt_factor_y
# 超平面方程式： coef[0] * (x1 * tilt_factor_x) + coef[1] * (x2 * tilt_factor_y) + coef[2] * x3 + intercept = 0
# 整理得到 x3 = -(coef[0] * x1 * tilt_factor_x + coef[1] * x2 * tilt_factor_y + intercept) / coef[2]

x1_grid, x2_grid = np.meshgrid(np.linspace(-20, 20, 50), np.linspace(-20, 20, 50))
x3_grid = -(coef[0, 0] * x1_grid * tilt_factor_x + coef[0, 1] * x2_grid * tilt_factor_y + intercept[0]) / coef[0, 2]

# 繪製分隔超平面
fig.add_trace(go.Surface(
    x=x1_grid,
    y=x2_grid,
    z=x3_grid,
    colorscale='gray',
    opacity=0.5,
    name='Decision Boundary'
))

# 設定 3D 圖的標題和軸標籤
fig.update_layout(
    title="SVM Decision Boundary in 3D with Adjustable Tilt Factors",
    scene=dict(
        xaxis_title="X1",
        yaxis_title="X2",
        zaxis_title="Gaussian Value (X3)"
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# 顯示圖形
st.plotly_chart(fig)
