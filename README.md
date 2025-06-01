## 🛠️ Training Setup and Parameters

| Component       | Details                         |
|----------------|----------------------------------|
| **GPU**         | NVIDIA Tesla T4 (13GB VRAM)     |
| **Batch Size**  | 16                               |
| **Epochs**      | 50 (Dataset 1), 120 (Dataset 2)  |
| **Frameworks**  | PyTorch, OpenCV, Python          |
| **Model Versions** | YOLOv5s, YOLOv8s, YOLOv11s    |
| **Accelerator** | GPU                             |

---

## 📈 Results and Discussion

### 🔍 5.1 Result and Analysis

This section presents a detailed comparative analysis of three object detection models—YOLOv5s, YOLOv8s, and YOLOv11s—on two curated fire and smoke detection datasets. The evaluation focuses on core performance metrics such as Precision, Recall, and mean Average Precision (mAP) to determine the robustness and generalization capability of each model.

---

### 📂 5.1.1 Dataset 1: Fire V-8 (979 images)

This is a small but well-balanced dataset containing labeled images across three categories: **fire**, **smoke**, and **background**. Each model was evaluated for its ability to accurately detect and classify instances of fire and smoke under varying lighting and background conditions.

YOLOv8s emerged as the best-performing model on this dataset, showing superior generalization and robustness. YOLOv5s followed closely, while YOLOv11s underperformed, likely due to its complexity being underutilized on a smaller dataset—leading to possible overfitting.

#### 📊 Table 3: Performance Comparison of YOLO Models on Dataset 1

| Model      | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|------------|-----------|--------|---------|--------------|
| **YOLOv5s**  | 0.930     | 0.927  | 0.957   | 0.698        |
| **YOLOv8s**  | 0.940     | 0.942  | 0.979   | 0.787        |
| **YOLOv11s** | 0.841     | 0.867  | 0.875   | 0.497        |

---

> 📌 *Note: Additional performance graphs, training loss plots, and real-time detection snapshots are included in the `/assets/` folder for deeper analysis.*

---

### 🔦 Real-world Consideration

To minimize false positives—such as detecting headlights or bright lights as fire—the models were trained with diverse datasets and filtered with a high confidence threshold. This ensures that the detection is based on chaotic visual patterns and context (e.g., flickering edges, smoke trails) rather than just brightness or color.

---

📸 *[Insert detection screenshots and loss curves here]*


---

### 📂 5.1.2 Dataset 2: Fire Smoke Detection (6,526 images)

[🔗 Dataset Link (Roboflow)](https://universe.roboflow.com/veli-t/firesmokedetection-5w49j/dataset/4)

This larger dataset presents complex, real-world scenes involving dynamic fire and smoke patterns across different lighting conditions and partial occlusions. It’s significantly more challenging than Dataset 1, making it ideal for evaluating a model's generalization ability.

YOLOv5s delivered the strongest results overall, particularly in **mAP@0.5**, suggesting better localization and detection on visually diverse data. Surprisingly, **YOLOv11s** slightly outperformed YOLOv8s in **mAP@0.5:0.95**, indicating its deeper architecture handled nuanced detection tasks better—despite the added training cost.

#### 📊 Table 4: Performance Comparison of YOLO Models on Dataset 2

| Model       | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|-------------|-----------|--------|---------|--------------|
| **YOLOv5s**   | 0.716     | 0.567  | 0.580   | 0.326        |
| **YOLOv8s**   | 0.653     | 0.527  | 0.550   | 0.320        |
| **YOLOv11s**  | 0.652     | 0.555  | 0.565   | 0.328        |

---

🧪 *Model training and evaluation were conducted using Google Colab with Tesla T4 GPU acceleration.*  
👉 [Colab Notebook 🔗](https://colab.research.google.com/drive/1VCRa__kG4RYLlHrJl3gW19eRrR8BelTk?usp=sharing)

> ⚠️ YOLOv11’s complexity benefits start to appear only with larger datasets. Its slight edge over YOLOv8 in fine-grained accuracy suggests better potential with further tuning or multi-scale augmentation.

---

📸 *[Add training logs, confusion matrices, and qualitative sample outputs here]*

