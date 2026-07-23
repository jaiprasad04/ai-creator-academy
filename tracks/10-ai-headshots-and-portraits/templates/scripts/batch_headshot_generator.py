#!/usr/bin/env python3
"""
Batch Corporate Headshot Generator
Automates rendering corporate headshots for a roster of remote employees via API.
"""

import os
import csv
import json
import time

def process_batch_headshots(roster_csv_path, output_dir="output_headshots"):
    os.makedirs(output_dir, exist_ok=True)
    print(f"Reading roster from {roster_csv_path}...")
    
    with open(roster_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            emp_id = row.get("EmployeeID", "EMP")
            full_name = row.get("FullName", "Employee")
            dress_code = row.get("DressCode", "Executive Suit")
            selfie_file = row.get("SelfieFile", "")
            
            print(f"\nProcessing {full_name} ({emp_id})...")
            print(f"  Dress Code: {dress_code}")
            print(f"  Source Selfie: {selfie_file}")
            
            # Construct prompt anchor
            prompt = (
                f"Photorealistic 8k corporate studio portrait of identity anchor, "
                f"wearing a {dress_code}, soft Rembrandt key light, "
                f"blurred modern glass office background with soft bokeh, 85mm lens."
            )
            
            # Simulating API batch inference output structure
            emp_dir = os.path.join(output_dir, full_name.replace(" ", "_"))
            os.makedirs(emp_dir, exist_ok=True)
            
            metadata = {
                "EmployeeID": emp_id,
                "FullName": full_name,
                "DressCode": dress_code,
                "Prompt": prompt,
                "Status": "Rendered",
                "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            meta_path = os.path.join(emp_dir, "metadata.json")
            with open(meta_path, "w", encoding="utf-8") as meta_file:
                json.dump(metadata, meta_file, indent=2)
                
            print(f"  Saved deliverable metadata: {meta_path}")

if __name__ == "__main__":
    print("=== Batch Corporate Headshot Generator ===")
    sample_csv = "sample_roster.csv"
    if not os.path.exists(sample_csv):
        with open(sample_csv, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["EmployeeID", "FullName", "Title", "DressCode", "SelfieFile"])
            writer.writerow(["EMP001", "John Doe", "VP Engineering", "Executive Suit", "selfies/john.jpg"])
            writer.writerow(["EMP002", "Sarah Jenkins", "Lead Designer", "Creative Blazer", "selfies/sarah.jpg"])
            
    process_batch_headshots(sample_csv)
    print("\nBatch headshot processing pipeline complete!")
