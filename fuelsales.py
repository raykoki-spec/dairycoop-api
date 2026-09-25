import csv, io
sales_data = """Date,Product,Quantity,Unit Price
2026-09-01,Petrol,500,221
2026-09-02,Diesel,300,230
2026-09-03,Kerosine,400,205"""

reader = csv.DictReader(io.StringIO(sales_data))
below = []
above = []
minimum_revenue = 80000
next(reader)  # Skip the header row


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

header_fmt = "{:<12} | {:<10} | {:>8} | {:>10} | {:>13}"
row_fmt    = "{Date:<12} | {Product:<10} | {Quantity:>8} | {Unit Price:>10} | {Total Revenue:>13}"

# Print main heading
print("FUEL SALES REPORT")

for r in below:
    print(row_fmt.format(**r))

for r in above:
    print(row_fmt.format(**r))

#Below minimum group
print("BELOW MINIMUM REVENUE THRESHOLD")
print(header_fmt.format("Date", "Product", "Quantity", "Unit Price", "Total Revenue"))
print("-" * 75)
for r in below:
    print(row_fmt.format(**r))

#Above minimum group
print("ABOVE MINIMUM REVENUE THRESHOLD")
print(header_fmt.format("Date", "Product", "Quantity", "Unit Price", "Total Revenue"))
print("-" * 75)
for r in above:
    print(row_fmt.format(**r))