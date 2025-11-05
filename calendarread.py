import pdfplumber
import pandas as pd
import re

pdf_path = "File.pdf"
records = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        lines = page.extract_text().split('\n')
        for i, line in enumerate(lines):
            if re.match(r"2025-\d{2}-\d{2}", line):
                try:
                    record = {
                        "Date": line.strip(),
                        "Fajr Begin": lines[i+3].strip(),
                        "Fajr Jama'ah": lines[i+4].strip(),
                        "Sunrise": lines[i+5].strip(),
                        "Zuhr Begin": lines[i+7].strip(),
                        "Zuhr Jama'ah": lines[i+8].strip(),
                        "Asr Begin": lines[i+9].strip(),
                        "Asr Jama'ah": lines[i+10].strip(),
                        "Maghrib Begin": lines[i+11].strip(),
                        "Maghrib Jama'ah": lines[i+12].strip(),
                        "Isha Begin": lines[i+13].strip(),
                        "Isha Jama'ah": lines[i+14].strip(),
                    }
                    records.append(record)
                except Exception as e:
                    print(f"Skipped a record due to indexing error at line {i}: {e}")

df = pd.DataFrame(records)
df.to_csv("prayer_timetable_2025.csv", index=False)
print("Complete CSV saved as 'prayer_timetable_2025.csv'")

