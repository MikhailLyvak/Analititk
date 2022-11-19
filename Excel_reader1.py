import openpyxl
from GUI import filename1
from GUI import filename2


print("Excel файли успішно зчитані")

# Зичтка з Excel файла №1
book = openpyxl.open(filename1)
sheet = book.active
ListRow1 = []
for row in range(7, sheet.max_row+1):
    if sheet.row_dimensions[row].hidden == False:
        ListCell = []
        for col in range(1, 9):
            ListCell.append(sheet[row][col].value)
        ListRow1.append(ListCell)

print("Зчитка з Excel файла №1")

# Зичтка з Excel файла №2
book = openpyxl.open(filename2)
sheet = book.active
ListRow2 = []
for row in range(7, sheet.max_row+1):
    if sheet.row_dimensions[row].hidden == False:
        ListCell = []
        for col in range(1, 7):
            ListCell.append(sheet[row][col].value)
        ListRow2.append(ListCell)

print("Зчитка з Excel файла №2")

for i in ListRow2:
    print(i)

# for b in i: 
#     print(b)

