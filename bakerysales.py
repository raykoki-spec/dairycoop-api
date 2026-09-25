import io, csv

#Simulated CSV file

sales_data = """Date,Town,Product,Units,Unit Price
2026-09-01,Shauri Moyo,600 gr,30,80
2026-09-02,Huruma A,800 gr,20,110
2026-09-03,Huruma B,600 gr,40,80
2026-09-04,Joyland,800 gr,15,110
2026-09-05,Mwanzo,400 gr,25,60"""

reader = csv.DictReader(io.StringIO(sales_data))
below = []
above = []
minimum_revenue = 2000


next(reader)  # Skip the header row

for row in reader:
    units = int(row['Units'])
    unit_price = int(row['Unit Price'])
    total_revenue = units * unit_price

    row['Total Revenue'] = str(total_revenue)  # ensure we have this for printing

    if total_revenue < minimum_revenue:
        below.append(row)
    else:
        above.append(row)

    # formatting strings for consistent columns
header_fmt = "{:<12} | {:<10} | {:<10} | {:>5} | {:>10} | {:>13}"
row_fmt    = "{Date:<12} | {Town:<10} | {Product:<10} | {Units:>5} | {Unit Price:>10} | {Total Revenue:>13}"

# Print main heading
print("SALES REPORT")
print("-" * 75)


# BELOW MINIMUM group
print("BELOW MINIMUM REVENUE THRESHOLD")
print(header_fmt.format("Date", "Town", "Product", "Units", "Unit Price", "Total Revenue"))
print("-" * 75)
for r in below:
    print(row_fmt.format(**r))
print()  # blank line between groups

# ABOVE MINIMUM group
print("ABOVE MINIMUM REVENUE THRESHOLD")
print(header_fmt.format("Date", "Town", "Product", "Units", "Unit Price", "Total Revenue"))
print("-" * 75)
for r in above:
    print(row_fmt.format(**r))