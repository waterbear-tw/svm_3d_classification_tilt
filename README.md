# 3D SVM 分類互動應用程式

此應用程式已經部署到 Streamlit Cloud。  
你可以透過以下連結來查看並互動操作該應用程式：  
**[3D SVM 分類應用程式](https://3d-svm-classification-popo.streamlit.app/)**

這是一個基於 [Streamlit](https://streamlit.io/) 的互動應用程式，用於在三維空間中視覺化 SVM 分類模型。使用者可以調整距離閾值以及超平面的傾斜度，觀察不同分類區域的變化情況。

---

## 功能

- 使用者可以透過拉桿調整：
  - **距離閾值**: 用於將隨機點根據與原點的距離分成不同的類別
  - **X 軸傾斜因子**: 控制超平面的 X 軸傾斜度，從而改變分類區域形狀
  - **Y 軸傾斜因子**: 控制超平面的 Y 軸傾斜度，產生橢圓形切面效果
- 透過三維視覺化呈現分類結果，紅色和藍色分別代表不同的類別
- 超平面顯示為灰色表面，可即時調整並反映分類邊界的變化

---

## 外觀

![App Screenshot](Screenshot.png)

---

## 如何運行應用程式

### 1. 安裝需求套件

首先，請確保已經安裝好所需的 Python 套件。在專案目錄下執行以下指令來安裝 `requirements.txt` 中列出的套件：

```bash
pip install -r requirements.txt
```
### 2. 運行應用程式
執行下列指令以啟動應用程式：

```bash
streamlit run svm_3d_classification_app.py
```

### 3. 在瀏覽器中查看
執行後，應用程式會在本地瀏覽器中打開，網址通常是 http://localhost:8501。
---
## 專案結構

1. svm_3d_classification_app.py: 應用程式的主要 Python 程式碼
2. requirements.txt: 列出了應用程式所需的依賴套件
3. README.md: 專案介紹與說明文件
4. Dependencies: Streamlit, Plotly, Scikit-learn, Numpy
---