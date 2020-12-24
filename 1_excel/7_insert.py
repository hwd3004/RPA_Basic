from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")

ws = wb.active

# 8번째 줄에 한 줄 추가
# ws.insert_rows(8)

# 8번째 줄에 5줄 추가
# ws.insert_rows(8, 5)

# 열 추가
# ws.insert_cols(2)
ws.insert_cols(2, 3)


# wb.save("sample_insert_rows.xlsx")
wb.save("sample_insert_cols.xlsx")
