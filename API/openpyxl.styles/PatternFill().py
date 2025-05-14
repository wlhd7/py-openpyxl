from openpyxl import Workbook
from openpyxl.styles import PatternFill

wb = Workbook()
ws = wb.active

ws['A2'].fill = PatternFill(
  start_color = 'FFFF00', 
  end_color = 'FFFF00',
  fill_type = 'solid')

wb.save('new.xlsx')

