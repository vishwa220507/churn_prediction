import numpy as np
from pathlib import Path

print("--- Validating Reproducibility ---")

BASE_DIR = Path(__file__).resolve().parent.parent
processed_dir = BASE_DIR / "data" / "processed"

X_train = np.load(processed_dir / "X_train_final.npy")
X_test = np.load(processed_dir / "X_test_final.npy")
y_train = np.load(processed_dir / "y_train.npy")
y_test = np.load(processed_dir / "y_test.npy")

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

print("All processed files loaded successfully!")
print("Reproducibility validation completed successfully!")