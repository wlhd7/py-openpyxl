from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# delete_cols(idx, amount=1)
# Delete column or columns from col==idx
delete_cols(2,2)
# delete_rows(idx, amount=1)
# Delete row or rows from row==idx
delete_rows(2,2)
