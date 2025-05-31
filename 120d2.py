import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Paths
csv_paths = {
    'YOLOv5': 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/v5_120_epochs.csv',
    'YOLOv8': 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/v8_120_epochs.csv',
    'YOLOv11': 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/v11_120.csv'
}
save_folder = 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/graphs'
os.makedirs(save_folder, exist_ok=True)

# 2. Load CSVs
dfs = {}
for name, path in csv_paths.items():
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    dfs[name] = df

# 3. Metrics for each model
metrics_dict = {
    'YOLOv5': [
        'train/box_loss', 'train/obj_loss', 'train/cls_loss',
        'metrics/precision', 'metrics/recall',
        'val/box_loss', 'val/obj_loss', 'val/cls_loss',
        'metrics/mAP_0.5', 'metrics/mAP_0.5:0.95'
    ],
    'YOLOv8': [
        'train/box_loss', 'train/cls_loss', 'train/dfl_loss',
        'metrics/precision(B)', 'metrics/recall(B)',
        'val/box_loss', 'val/cls_loss', 'val/dfl_loss',
        'metrics/mAP50(B)', 'metrics/mAP50-95(B)'
    ],
    'YOLOv11': [
        'train/box_loss', 'train/cls_loss', 'train/dfl_loss',
        'metrics/precision(B)', 'metrics/recall(B)',
        'val/box_loss', 'val/cls_loss', 'val/dfl_loss',
        'metrics/mAP50(B)', 'metrics/mAP50-95(B)'
    ]
}

# 4. Plotting
for model_name, df in dfs.items():
    metrics = metrics_dict[model_name]

    fig, axes = plt.subplots(2, 5, figsize=(12, 5))  # Wider figure
    axes = axes.flatten()

    for i, metric in enumerate(metrics):
        ax = axes[i]
        if metric in df.columns:
            ax.plot(df[metric], label='result', color='blue', linewidth=1)
            ax.plot(df[metric].rolling(5).mean(), label='smooth', color='orange', linestyle='--', linewidth=1)
        else:
            ax.text(0.5, 0.5, 'No Data', ha='center', va='center', fontsize=10)
        ax.set_title(metric, fontsize=11)
        ax.grid(True)
        ax.tick_params(axis='both', which='major', labelsize=8)  # <-- show x and y ticks

    # Remove extra empty subplots if any
    for j in range(len(metrics), len(axes)):
        fig.delaxes(axes[j])

    # Only one legend for all
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=2, fontsize=8)

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for legend
    save_path = os.path.join(save_folder, f'{model_name}_metrics.png')
    plt.savefig(save_path, dpi=300)
    print(f"Saved {save_path}")
    plt.close()
