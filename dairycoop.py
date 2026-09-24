import json

# --- Configuration ---
COOPERATIVE = "Githunguri Dairy Cooperative"
MIN_LITRES = 10.0   # flag farms below this daily target

# --- Fetch ---
def fetch_farm_readings():
    # Simulated readings from morning collection
    return [
        {"farm": "Kamau wa Njoroge",  "location": "Githunguri", "litres": 22.5, "cows": 3},
        {"farm": "Koki's farm", "location": "Chimoi", "litres": 33, "cows": 10},
        {"farm": "Wanjiku Farm",      "location": "Limuru",     "litres": 18.0, "cows": 2},
        {"farm": "Mwangi Dairy",      "location": "Githunguri", "litres": 31.5, "cows": 4},
        {"farm": "Achieng Holdings",  "location": "Thika",      "litres": 11.0, "cows": 2},
        {"farm": "Kariuki Homestead", "location": "Limuru",     "litres": 26.0, "cows": 3},
    ]

# --- Process ---
def process_readings(readings, min_litres):
    total = sum(r["litres"] for r in readings)
    avg = round(total / len(readings), 1) if readings else 0
    below_target = [r for r in readings if r["litres"] < min_litres]
    top = max(readings, key=lambda r: r["litres"])
    return {
        "farms_collected": len(readings),
        "total_litres": total,
        "average_litres": avg,
        "below_target": [r["farm"] for r in below_target],
        "top_farm": top["farm"],
        "top_litres": top["litres"]
    }

# --- Output ---
def print_farm_report(cooperative, summary):
    print(f"\n{'='*50}")
    print(f"  DAILY REPORT: {cooperative.upper()}")
    print(f"{'='*50}")
    print(f"  Farms collected:   {summary['farms_collected']}")
    print(f"  Total litres:      {summary['total_litres']:.1f} L")
    print(f"  Average per farm:  {summary['average_litres']} L")
    print(f"  Top farm:          {summary['top_farm']} ({summary['top_litres']} L)")
    if summary["below_target"]:
        print(f"  Below target:      {', '.join(summary['below_target'])}")
    else:
        print("  All farms met target today.")
    print(f"{'='*50}\n")

# --- Main ---
readings = fetch_farm_readings()
summary  = process_readings(readings, MIN_LITRES)
print_farm_report(COOPERATIVE, summary)