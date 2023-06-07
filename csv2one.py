import csv

# Input file paths
input_files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]
output_file = "output.csv"

# Create a list to store the rows
rows = []

# Process each input file
for file in input_files:
    with open(file, "r") as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip the header row

        # Iterate through each row
        for row in reader:
            product = row[0]
            price = float(row[1].replace("$", ""))  # Remove the dollar sign
            quantity = float(row[2])
            date = row[3]
            region = row[4]

            # Filter rows by product
            if product != "pink morsel":
                continue

            # Calculate sales
            sales = quantity * price

            # Add the row to the list
            rows.append([sales, date, region])

# Sort the rows by region
rows.sort(key=lambda x: x[2])  # Sort based on the third element (region)

# Write the sorted rows to the output file
with open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Sales", "Date", "Region"])  # Write the header row
    writer.writerows(rows)

print("Conversion success.")