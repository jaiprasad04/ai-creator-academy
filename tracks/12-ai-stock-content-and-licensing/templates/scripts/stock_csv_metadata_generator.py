#!/usr/bin/env python3
"""
Stock Photography IPTC & CSV Metadata Generator
Generates Adobe Stock / Freepik compliant CSV metadata sheets for bulk stock asset submissions.
"""

import os
import csv

def generate_stock_csv_metadata(output_csv_path="stock_submission_metadata.csv"):
    stock_items = [
        {
            "Filename": "corporate_handshake_01.jpg",
            "Title": "Diverse Business Executives Shaking Hands in Sunlit Modern Corporate Office",
            "Keywords": "handshake; business; corporate; executive; meeting; deal; partnership; trust; agreement; office; teamwork; success; professional; copy space",
            "Category": "Business"
        },
        {
            "Filename": "future_tech_server_01.jpg",
            "Title": "High Tech Server Room Facility with Glowing Blue Fiber Optic Data Stream",
            "Keywords": "server room; technology; data center; cloud computing; cyber security; network; digital; fiber optic; infrastructure; database; copy space",
            "Category": "Technology"
        }
    ]
    
    with open(output_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Filename", "Title", "Keywords", "Category"])
        writer.writeheader()
        for item in stock_items:
            writer.writerow(item)
            
    print(f"Generated Stock Submission CSV: {output_csv_path}")
    print(f"  Total Assets Included: {len(stock_items)}")
    print("  Compatible with: Adobe Stock, Freepik, Wirestock CSV uploaders.")

if __name__ == "__main__":
    print("=== Stock Photography Metadata CSV Generator ===")
    generate_stock_csv_metadata()
