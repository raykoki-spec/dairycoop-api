import io, csv
import json

#Simulated CSV file
sales_data = """Date,Spares,Quantity,Unit Price
2026-09-01,Brake Pads,50,1200
2026-09-02,Oil Filter,100,800
2026-09-03,Spark Plugs,200,500
2026-09-04,Air Filter,80,1500
2026-09-05,Timing Belt,30,2500
2026-09-06,Brake Discs,40,3000"""

reader = csv.DictReader(io.StringIO(sales_data))
below = []
above = []
minimum_revenue = 50000

for row in reader:
    quantity = int(row['Quantity'])
    unit_price = int(row['Unit Price'])
    total_revenue = quantity * unit_price
    row['Total Revenue'] = str(total_revenue)  # ensure we have this for printing

    if total_revenue < minimum_revenue:
        below.append(row)
    else:
        above.append(row)

# formatting strings for consistent columns
header_fmt = "{:<12} | {:<15} | {:>8} | {:<15}"
row_fmt    = "{Date:<12} | {Spares:<15} | {Quantity:>8} | {Unit Price:<15}"

# Print main heading
print("AUTO SPARE SALES REPORT")
print("-" * 60)

# Print the sales data for each category
print("\nBelow Minimum Revenue:")
print(header_fmt.format("Date", "Spares", "Quantity", "Unit Price"))
for row in below:
    print(row_fmt.format(**row))

print("\nAbove Minimum Revenue:")
print(header_fmt.format("Date", "Spares", "Quantity", "Unit Price"))
for row in above:
    print(row_fmt.format(**row))

#Export results to JSON
with open("autosparesales_results.json", "w") as f:
    json.dump({"below": below, "above": above}, f, indent=2)