## 🛠️ Training Setup and Parameters 🛠️

| Component       | Details                         |
|----------------|----------------------------------|
| **GPU**         | NVIDIA Tesla T4 (colab)           |
| **Batch Size**  | 16                               |
| **Epochs**      | 50 (Dataset 1), 120 (Dataset 2)  |
| **Frameworks**  | PyTorch, OpenCV, Python          |
| **Model Versions** | YOLOv5s, YOLOv8s, YOLOv11s    |
| **Accelerator** | GPU                             |

---

## 📈 Results

[🔗 Dataset Link (Roboflow)](https://universe.roboflow.com/custom-thxhn/fire-wrpgm/dataset/8)
### Dataset 1: Fire V-8 (979 images)

| Model      | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|------------|-----------|--------|---------|--------------|
| **YOLOv5s**  | 0.930     | 0.927  | 0.957   | 0.698        |
| **YOLOv8s**  | 0.940     | 0.942  | 0.979   | 0.787        |
| **YOLOv11s** | 0.841     | 0.867  | 0.875   | 0.497        |


<img src = "https://github.com/user-attachments/assets/be66d1eb-54a5-4dd9-90ce-a0fa44af1328" width = "500"/>
<img src = "https://github.com/user-attachments/assets/243a5616-202a-442b-ad88-684f6bc1e7ee" width = "500"/>
<img src = "https://github.com/user-attachments/assets/e4c13095-6209-4e3e-84a6-419ac4874fd3" width = "500"/>
<img src = "https://github.com/user-attachments/assets/32436c11-82d7-4596-99ce-aae342319bef" width = "500"/>

### 🔦 Real-world Consideration

To minimize false positives—such as detecting headlights or bright lights as fire—the models were trained with diverse datasets and filtered with a high confidence threshold. This ensures that the detection is based on chaotic visual patterns and context (e.g., flickering edges, smoke trails) rather than just brightness or color.

---
### Detection Results 

## YOLOv5s
<img src = "https://github.com/user-attachments/assets/77e5f23e-292d-4b5a-8c73-5fdb070bef3c" height = "500"/>

## YOLOv8s
![image](https://github.com/user-attachments/assets/0c401bb9-8895-4ff3-ae28-e31b8a8638d8)

## YOLOv11s
![image](https://github.com/user-attachments/assets/2fad1b75-7153-466c-80e0-cdccc3719b57)


---

### 📂 5.1.2 Dataset 2: Fire Smoke Detection (6,526 images)

[🔗 Dataset Link (Roboflow)](https://universe.roboflow.com/veli-t/firesmokedetection-5w49j/dataset/4)


| Model       | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|-------------|-----------|--------|---------|--------------|
| **YOLOv5s**   | 0.716     | 0.567  | 0.580   | 0.326        |
| **YOLOv8s**   | 0.653     | 0.527  | 0.550   | 0.320        |
| **YOLOv11s**  | 0.652     | 0.555  | 0.565   | 0.328        |

<img src = "https://github.com/user-attachments/assets/266f4ecf-86ef-47b0-a2ee-d80f779a5bbe" width = "500"/>
<img src = "https://github.com/user-attachments/assets/f49feee4-63ef-461b-8592-36f198626f38" width = "500"/>
<img src = "https://github.com/user-attachments/assets/e96bcbae-0e52-48d8-a8a6-b6c7fca03166" width = "500"/>
<img src = "https://github.com/user-attachments/assets/3f745919-4c48-4e63-b9fd-fa8d90f54eed" width = "500"/>

---
### Detection Results 

## YOLOv5s
![val_batch0_labels](https://github.com/user-attachments/assets/13c2ed58-3356-4249-b062-44f49e4bbd80)

## YOLOv8s
![val_batch0_labels](https://github.com/user-attachments/assets/e047d834-1d93-4382-9a23-8ad1a66e89a9)

## YOLOv11s
![val_batch0_labels](https://github.com/user-attachments/assets/a09f2769-6b63-4caa-bccc-d1f3bb0ce46a)

---
🧪 *Model training and evaluation were conducted using Google Colab with Tesla T4 GPU acceleration.*  
👉 [Colab Notebook 🔗](https://colab.research.google.com/drive/1VCRa__kG4RYLlHrJl3gW19eRrR8BelTk?usp=sharing)

---
