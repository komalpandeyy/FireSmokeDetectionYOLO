import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Paths
csv_paths = {
    'YOLOv5': 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/v5_120_epochs.csv',
    'YOLOv8': 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/v8_120_epochs.csv',
    'YOLOv11': 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial/v11_120.csv'
}
save_folder = 'C:/Users/admin/OneDrive/Desktop/Major Project MCA/120 epochs trial'
os.makedirs(save_folder, exist_ok=True)
# 2. Load all CSVs
dfs = {}
for name, path in csv_paths.items():
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()  # <-- strip spaces
    dfs[name] = df
# 2. Load all CSVs
##dfs = {}
##for name, path in csv_paths.items():
##    dfs[name] = pd.read_csv(path)

# 3. Define plotting function for one model

def plot_individual_graphs(model_name, df):
    epochs = range(len(df))
    
    # Dynamic column selection
    precision_col = 'metrics/precision(B)' if 'metrics/precision(B)' in df.columns else 'metrics/precision'
    recall_col = 'metrics/recall(B)' if 'metrics/recall(B)' in df.columns else 'metrics/recall'
    map50_col = 'metrics/mAP50(B)' if 'metrics/mAP50(B)' in df.columns else 'metrics/mAP_0.5'
    map5095_col = 'metrics/mAP50-95(B)' if 'metrics/mAP50-95(B)' in df.columns else 'metrics/mAP_0.5:0.95'

    fig, axs = plt.subplots(2, 3, figsize=(18, 10))
    axs = axs.ravel()
    
##    axs[0].plot(epochs, df[precision_col], label='Precision', color='blue')
##    axs[0].set_title(f'{model_name} - Precision')
##    axs[0].set_xlabel('Epoch')
##    axs[0].set_ylabel('Precision')
##    axs[0].legend()
##
##    axs[1].plot(epochs, df[recall_col], label='Recall', color='green')
##    axs[1].set_title(f'{model_name} - Recall')
##    axs[1].set_xlabel('Epoch')
##    axs[1].set_ylabel('Recall')
##    axs[1].legend()
##
##    axs[2].plot(epochs, (df[precision_col] + df[recall_col])/2, label='Accuracy (Approx)', color='orange')
##    axs[2].set_title(f'{model_name} - Accuracy (Approx)')
##    axs[2].set_xlabel('Epoch')
##    axs[2].set_ylabel('Accuracy')
    axs[2].legend()

    axs[3].plot(epochs, df[map50_col], label='mAP@0.5', color='red')
    axs[3].set_title(f'{model_name} - mAP@0.5')
    axs[3].set_xlabel('Epoch')
    axs[3].set_ylabel('mAP@0.5')
    axs[3].legend()

    axs[4].plot(epochs, df[map5095_col], label='mAP@0.5:0.95', color='purple')
    axs[4].set_title(f'{model_name} - mAP@0.5:0.95')
    axs[4].set_xlabel('Epoch')
    axs[4].set_ylabel('mAP@0.5:0.95')
    axs[4].legend()

    axs[5].axis('off')  # Empty subplot

    plt.tight_layout()
    plt.savefig(f'{save_folder}/{model_name}_individual_graphs.png')
    plt.close()

# 4. Plot individual graphs for each model
for model_name, df in dfs.items():
    plot_individual_graphs(model_name, df)

# 5. Plot comparison graphs
metrics = ['Precision', 'Recall', 'Accuracy (Approx)', 'mAP@0.5', 'map']

for metric_name in metrics:
    plt.figure(figsize=(10, 6))
    
    for model_name, df in dfs.items():
        # Dynamic column selection
        #precision_col = 'metrics/precision(B)' if 'metrics/precision(B)' in df.columns else 'metrics/precision'
        #recall_col = 'metrics/recall(B)' if 'metrics/recall(B)' in df.columns else 'metrics/recall'
        #map50_col = 'metrics/mAP_0.5' if 'metrics/mAP_0.5' in df.columns else 'metrics/mAP50(B)'
        map5095_col = 'metrics/mAP50-95(B)' if 'metrics/mAP50-95(B)' in df.columns else 'metrics/mAP_0.5:0.95'
        
##        if metric_name == 'Precision':
##            plt.plot(range(len(df)), df[precision_col], label=model_name)
##        elif metric_name == 'Recall':
##            plt.plot(range(len(df)), df[recall_col], label=model_name)
##        if metric_name == 'Accuracy (Approx)':
##            plt.plot(range(len(df)), (df[precision_col] + df[recall_col])/2, label=model_name)
        #if metric_name == 'mAP@0.5':
            #plt.plot(range(len(df)), df[map50_col], label=model_name)
        if metric_name == 'map':
            plt.plot(range(len(df)), df[map5095_col], label=model_name)

    plt.title(f'Comparison - {metric_name}')
    plt.xlabel('Epoch')
    plt.ylabel(metric_name)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'{save_folder}/Comparison_{metric_name.replace(" ", "_")}.png')
    plt.close()

print("✅ All graphs generated and saved to:", save_folder)
'''


# Summary and Best Model Selection

summary = {}

for model_name, df in dfs.items():
    precision_col = 'metrics/precision(B)' if 'metrics/precision(B)' in df.columns else 'metrics/precision'
    recall_col = 'metrics/recall(B)' if 'metrics/recall(B)' in df.columns else 'metrics/recall'
    map50_col = 'metrics/mAP50(B)' if 'metrics/mAP50(B)' in df.columns else 'metrics/mAP_0.5'
    map5095_col = 'metrics/mAP50-95(B)' if 'metrics/mAP50-95(B)' in df.columns else 'metrics/mAP_0.5:0.95'

    best_epoch = df[map50_col].idxmax()
    best_row = df.loc[best_epoch]

    summary[model_name] = {
        'Best Epoch': best_epoch,
        'Precision': best_row[precision_col],
        'Recall': best_row[recall_col],
        'mAP@0.5': best_row[map50_col],
        'mAP@0.5:0.95': best_row[map5095_col]
    }

# Display nicely
print("\n📊 Summary for Each Model:")
for model, stats in summary.items():
    print(f"\n--- {model} ---")
    for key, value in stats.items():
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")

# Find the best model based on highest mAP@0.5
best_model = max(summary.items(), key=lambda x: x[1]['mAP@0.5'])[0]

print(f"\n🏆 Best Model: {best_model}")

# Save summary to text file
summary_path = os.path.join(save_folder, 'model_summary.txt')
with open(summary_path, 'w') as f:
    f.write("📊 Summary for Each Model:\n")
    for model, stats in summary.items():
        f.write(f"\n--- {model} ---\n")
        for key, value in stats.items():
            f.write(f"{key}: {value:.4f}\n" if isinstance(value, float) else f"{key}: {value}\n")
    f.write(f"\n🏆 Best Model: {best_model}\n")

print(f"\n✅ Summary saved to {summary_path}")'''

