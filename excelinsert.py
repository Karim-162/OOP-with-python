import openpyxl as op

wb=op.load_workbook('G:\Downloads\email.xlsx')
sh=wb.active
c=sh.cell(row=11,column=4)
#print(c.value)

c.value= "2009-07-17"
wb.save('G:\Downloads\email.xlsx')
print(c.value)