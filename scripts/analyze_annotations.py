#!/usr/bin/env python3
import argparse, os
import pandas as pd
from sklearn.model_selection import train_test_split

BASIC_BEHAVIORS = ["Sit","Down","Recall","Stay","Release"]
SUBJECTS = ["Dog","Owner"]
REQUIRED = ["video_id","file_name","subject","behavior","start_time_sec","end_time_sec","result","feedback_type"]

def load_annotations(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Annotations CSV not found: {path}")
    df = pd.read_csv(path)
    missing = set(REQUIRED) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in CSV: {missing}")
    return df

def summarize(df, title="Summary"):
    print(f"\n=== {title} ===")
    print("Rows:", len(df))
    for col in ["behavior","subject","result","feedback_type"]:
        if col in df.columns:
            print(f"\n{col} distribution:\n{df[col].value_counts()}")

def make_splits(df, out_dir="splits", test_size=0.2, val_size=0.1, seed=42):
    os.makedirs(out_dir, exist_ok=True)
    train_val, test = train_test_split(df, test_size=test_size, random_state=seed, stratify=df["behavior"])
    val_fraction = val_size / (1.0 - test_size)
    train, val = train_test_split(train_val, test_size=val_fraction, random_state=seed, stratify=train_val["behavior"])
    train.to_csv(os.path.join(out_dir, "train.csv"), index=False)
    val.to_csv(os.path.join(out_dir, "val.csv"), index=False)
    test.to_csv(os.path.join(out_dir, "test.csv"), index=False)
    print(f"✅ Saved splits to: {os.path.abspath(out_dir)}")

def main():
    csv_path = os.environ.get("DOGSENSE_CSV", "").strip()
    if not csv_path or not os.path.exists(csv_path):
        # Fallbacks:
        if os.path.exists("annotations.csv"):
            csv_path = "annotations.csv"
        elif os.path.exists("sample_annotations.csv"):
            csv_path = "sample_annotations.csv"
            print("⚠️ Using sample_annotations.csv (place your own 'annotations.csv' at repo root to override).")
        else:
            raise SystemExit("❌ No CSV found. Provide 'annotations.csv' at repo root or set DOGSENSE_CSV=/path/to.csv")
    df = load_annotations(csv_path)
    summarize(df, "Full dataset")
    df = df[df["behavior"].isin(BASIC_BEHAVIORS)].copy()
    df = df[df["subject"].isin(SUBJECTS)].copy()
    summarize(df, "Filtered dataset")
    if len(df) < 10:
        print("⚠️ Very few rows after filtering; splits may be unstable.")
    make_splits(df, out_dir="splits")

if __name__ == "__main__":
    main()
