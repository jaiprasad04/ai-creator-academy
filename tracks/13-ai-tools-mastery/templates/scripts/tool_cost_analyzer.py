#!/usr/bin/env python3
"""
AI Tool Cost Analyzer & Hardware Payback Calculator
Analyzes monthly credit spend across Cloud APIs vs Local GPU Hardware amortization.
"""

import sys

def calculate_payback_period(monthly_renders, avg_cost_per_render=0.06, gpu_cost=2500):
    monthly_api_spend = monthly_renders * avg_cost_per_render
    annual_api_spend = monthly_api_spend * 12
    
    if monthly_api_spend > 0:
        payback_months = gpu_cost / monthly_api_spend
    else:
        payback_months = float('inf')
        
    print("=== AI Infrastructure Cost Analysis ===")
    print(f"  Monthly Render Volume: {monthly_renders:,} renders")
    print(f"  Average API Cost / Render: ${avg_cost_per_render:.3f}")
    print(f"  Estimated Monthly Cloud API Spend: ${monthly_api_spend:,.2f}")
    print(f"  Estimated Annual Cloud API Spend: ${annual_api_spend:,.2f}")
    print(f"  Target Local GPU Rig Cost: ${gpu_cost:,.2f}")
    print(f"  Hardware Amortization Payback Period: {payback_months:.1f} Months")
    
    print("\nArchitectural Recommendation:")
    if monthly_renders < 1500:
        print("  [➜] STAY ON CLOUD APIs (muapi / Replicate)")
        print("      Low volume does not justify upfront GPU hardware investment.")
    elif monthly_renders <= 5000:
        print("  [➜] HYBRID MODEL (Cloud APIs + RunPod Hourly GPUs)")
        print("      Optimal balance between operational flexibility and cost control.")
    else:
        print("  [➜] BUY LOCAL GPU WORKSTATION (RTX 4090 24GB)")
        print("      High volume pays off hardware investment in under 6 months!")
        
    return payback_months

if __name__ == "__main__":
    volume = 3000
    if len(sys.argv) > 1:
        try:
            volume = int(sys.argv[1])
        except ValueError:
            pass
            
    calculate_payback_period(volume)
