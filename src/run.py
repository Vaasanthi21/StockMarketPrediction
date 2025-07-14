from data_loader import fetch_stock_data
import os
import sys

# Set output path
output_folder = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "data", "data_raw")
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "aapl_2022.csv")

# Fetch and print data
df = fetch_stock_data("AAPL", start="2022-01-01", end="2022-12-31")
print("✅ Data Shape:", df.shape)
print(df.head())

# Save only if DataFrame is not empty
if not df.empty:
    df.to_csv(output_path)
    print(f"✅ Data saved to {output_path}")
else:
    print("⚠ No data fetched. CSV not saved.")