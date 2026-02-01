import openpyxl as op

wb = op.load_workbook('G:/Downloads/xl.xlsx')
ws = wb.active

# User input
user_id = int(input("Enter ID: "))
user_hadith = input("Enter Hadith: ")

for row in ws.iter_rows(min_row=2):
    cell_id = row[0].value
    
    if cell_id == user_id:
        row[1].value = user_hadith
        break

wb.save('G:/Downloads/xl.xlsx')

print("Data inserted successfully!")
