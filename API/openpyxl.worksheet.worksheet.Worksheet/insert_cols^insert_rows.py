from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# insert_rows(idx, amount=1)
# insert row or rows before row==idx
ws.insert_rows(2,2)
# insert_cols(idx, amount=1)
# insert column or columns before col==cols
ws.insert_cols(3,3)
