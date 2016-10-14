import openpyxl
import csv

wb = openpyxl.Workbook()
wb.guess_types = True
sheet = wb.active

with open("test_data.csv") as f:
    reader = csv.reader(f)
    sheet['A2'].number_format = '#,##0'
    # Convert to currency format
    # Change cell column to red if number is negative
    sheet['B2'].number_format = '$#,##0.00_);[Red]($#,##0.00)'
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            try:
                col = float(col)
            except ValueError:
                if col.startswith('$'):
                    col = float(col[1:])

            sheet.cell(row=r + 1, column=c + 1).value = col

wb.save("test_data.xlsx")
