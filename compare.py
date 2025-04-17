import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


v5 = pd.read_csv(r'C:\Users\admin\OneDrive\Desktop\Major Project MCA\yolo v5 results\results.csv')
v8 = pd.read_csv(r'C:\Users\admin\OneDrive\Desktop\Major Project MCA\yolov8 results\results.csv')
print(v5.columns)
print(v8.columns)
v5.columns = v5.columns.str.strip()
v8.columns = v8.columns.str.strip()

epochs = v5['epoch']  # Same for both models

# Function to plot comparisons
def plot_metric(metric_v5, metric_v8, label, ylabel, title):
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, metric_v5, label='YOLOv5', color='blue')
    plt.plot(epochs, metric_v8, label='YOLOv8', color='orange')
    plt.xlabel('Epochs')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

### Plot Training Losses
plot_metric(v5['train/box_loss'], v8['train/box_loss'], 'Box Loss', 'Loss', 'Training Box Loss: YOLOv5 vs YOLOv8')
plot_metric(v5['train/cls_loss'], v8['train/cls_loss'], 'Class Loss', 'Loss', 'Training Class Loss: YOLOv5 vs YOLOv8')
# Plot Validation Losses
plot_metric(v5['val/box_loss'], v8['val/box_loss'], 'Val Box Loss', 'Loss', 'Validation Box Loss: YOLOv5 vs YOLOv8')
plot_metric(v5['val/cls_loss'], v8['val/cls_loss'], 'Val Class Loss', 'Loss', 'Validation Class Loss: YOLOv5 vs YOLOv8')



# Plot Evaluation Metrics
plot_metric(v5['metrics/precision'], v8['metrics/precision(B)'], 'Precision', 'Precision', 'Precision (B): YOLOv5 vs YOLOv8')
plot_metric(v5['metrics/recall'], v8['metrics/recall(B)'], 'Recall', 'Recall', 'Recall (B): YOLOv5 vs YOLOv8')
plot_metric(v5['metrics/mAP_0.5'], v8['metrics/mAP50(B)'], 'mAP@50', 'mAP@50', 'mAP@50 (B): YOLOv5 vs YOLOv8')
plot_metric(v5['metrics/mAP_0.5:0.95'], v8['metrics/mAP50-95(B)'], 'mAP@50-95', 'mAP@50-95', 'mAP@50-95 (B): YOLOv5 vs YOLOv8')


# Get last row (final epoch)
last_v5 = v5.iloc[-1]
last_v8 = v8.iloc[-1]

import pandas as pd

# Define summary data manually from your provided table (image)
data = {
    'Metric': ['Fire', 'Fire', 'Smoke', 'Smoke', 'Other', 'Other', 'Overall', 'Overall'],
    'Model': ['YOLOv5', 'YOLOv8'] * 4,
    'Precision (P)': [0.49, 0.679, 0.321, 0.51, 0.143, 1.0, 0.318, 0.529],
    'Recall (R)': [0.993, 0.772, 0.872, 0.814, 0.8, 0.0, 0.888, 0.554],
    'mAP50': [0.628, 0.727, 0.391, 0.711, 0.214, 0.225, 0.411, 0.554],
    'mAP50-95': [0.536, 0.665, 0.343, 0.649, 0.192, 0.187, 0.357, 0.501]
}

