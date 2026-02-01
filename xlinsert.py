import openpyxl as op

wb = op.load_workbook('G:/Downloads/xl.xlsx')
ws = wb.active

data = {
    1: "Actions are judged by intentions.",
    3: "The best among you are those with the best manners."
}

for row in ws.iter_rows(min_row=2):
    cell_id = row[0].value
    
    if cell_id in data:
        row[1].value = data[cell_id]

wb.save('G:/Downloads/xl.xlsx')


print("Data inserted successfully!")
