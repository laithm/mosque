import tabula
import pandas as pd

# Path to your PDF
pdf_path = "Prayer & Education Centre 2025-2"

# This will extract all tables from every page into a list of DataFrames
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True, lattice=True)

# Combine all extracted tables (for all months/pages)
df_full = pd.concat(tables, ignore_index=True)

# OPTIONAL: Clean up columns (rename, drop unwanted, etc.)
# Example: If your first row is headers, uncomment this:
# df_full.columns = df_full.iloc[0]
# df_full = df_full.drop(df_full.index[0])

# Save to CSV
df_full.to_csv("prayer_timetable_2025.csv", index=False)
print("Saved full timetable to 'prayer_timetable_2025.csv'")
