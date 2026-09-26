import io, csv
import json
from collections import defaultdict

#Simulated CSV file
sales_data = """Date,Spares,Quantity,Unit Price
2026-09-01,Brake Pads,9,8000
2026-09-01,Oil Filter,25,3500
2026-09-01,Brake Booster,5,15000
2026-09-02,Oil Filter,7,3500
2026-09-02,ATF,100,500
2026-09-02,Engine Oil,200,650
2026-09-02,Side Mirror,50,2500
2026-09-03,Belt Tensioner,25,11500
2026-09-03,Head Lamp,10,13500
2026-09-03,Brake Pads,10,15000
2026-09-03,Spark Plugs,200,500
2026-09-03,Cylinder Liner,6,22000
2026-09-04,Air Filter,13,12500
2026-09-04,Brake Pads,15,15000
2026-09-04,Brake Discs,14,15000
2026-09-05,Timing Belt,25,7500
2026-09-05,Air Filter,9,12500
2026-09-05,Brake Booster,20,15000
2026-09-05,ATF,100,500
2026-09-05,Brake Pads,10,15000
2026-09-06,Engine Oil,300,650
2026-09-06,Side Mirror,10,2500
2026-09-06,Belt Tensioner,15,11500"""

reader = csv.DictReader(io.StringIO(sales_data))
rows = []
below = []
above = []
minimum_revenue = 80000

for row in reader:
    date = row['Date'].strip()
    spares = row['Spares'].strip()
    quantity = int(row['Quantity'])
    unit_price = int(row['Unit Price'])
    total_revenue = quantity * unit_price
    row['Total Revenue'] = str(total_revenue)  # ensure we have this for printing
    rows.append(row)

    if total_revenue < minimum_revenue:
        below.append(row)
    else:
        above.append(row)

# formatting strings for consistent columns
header_fmt = "{:<12} | {:<15} | {:>8} | {:<15} | {:>13}"
row_fmt    = "{Date:<12} | {Spares:<15} | {Quantity:>8} | {Unit Price:<15} | {Total Revenue:>13}"

# Print main heading
print("AUTO SPARE SALES REPORT")
print("-" * 75)

# Print the sales data for each category
print("\nBelow Minimum Revenue:")
print(header_fmt.format("Date", "Spares", "Quantity", "Unit Price", "Total Revenue"))
print("-" * 75)
for row in below:
    print(row_fmt.format(**row))

print("\nAbove Minimum Revenue:")
print(header_fmt.format("Date", "Spares", "Quantity", "Unit Price", "Total Revenue"))
print("-" * 75)
for row in above:
    print(row_fmt.format(**row))

#Export results to JSON
with open("autosparesales_results.json", "w") as f:
    json.dump({"below": below, "above": above}, f, indent=2)