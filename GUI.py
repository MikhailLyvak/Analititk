import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from turtle import bgcolor
from tkinter import filedialog as fd
from Excel_reader1 import *
from tkinter import ttk

print("GUI")

#Оболочька программи
root = tk.Tk()
Yes_Zvit_01 = tk.IntVar()          # <-- Переменна куди записується 1 або 0 якщо Звіт №1 вибрали або ні
Yes_Zvit_02 = tk.IntVar()          # <-- Переменна куди записується 1 або 0 якщо Звіт №2 вибрали або ні
root.title('Аналітик')
root.geometry("1200x750+360+80")
root.resizable(False, False)
root.config(bg="#505575")
photo = tk.PhotoImage(file='analitic.png')
photo_1 = tk.PhotoImage(file='next.png')
photo2 = photo_1.subsample(15, 15)
root.iconphoto(False, photo)

#Данні для вибору місяця і року
month_value = ("Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень")
year_value = ("2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025")

#Поля для вибору місяця і року (Їх буде використовувати Саша при формуванні Ексель файла)
month_print = ttk.Combobox(root, values=month_value, width=12, font=('Times New Roman', 24))
year_print = ttk.Combobox(root, width=6,value=year_value, font=('Times New Roman', 24))
month_print.current(0)
year_print.current(12)




#Переменні з інформацією
filename1 = ''
filename2 = ''
filename3 = ''

#Функції кнопок
def select_file_1():                        # <-- Функція для пошуку файлу Excel(Шлях до нього)
    global filename1
    filename1 = fd.askopenfilename(
        title='Open a file'
    )

def select_file_2():                        # <-- Функція для пошуку файлу Excel(Шлях до нього)
    global filename2
    filename2 = fd.askopenfilename(
        title='Open a file'
    )

def select_file_3():                        # <-- Функція для пошуку файлу Excel(Шлях до нього)
    global filename3
    filename3 = fd.askopenfilename(
        title='Open a file'
    )

result1 = Yes_Zvit_01.get()
result2 = Yes_Zvit_02.get()

def check_n():
    global result1
    global result2
    result1 = Yes_Zvit_01.get()
    result2 = Yes_Zvit_02.get()

# current_y = year_print.get()
# current_m = month_print.get()
def show_date():
    global current_y
    global current_m
    current_y = year_print.get()
    current_m = month_print.get()

# def select_all():
#     for check in [Zvit_01, Zvit_02]:
#         check.select()


# Кнопкі вибора ексель файлів
btn1 = tk.Button(root, text='  Виберіть Excel файл №1  ', 
                        font=60, 
                        bg='#979DBF',
                        activebackground='#9ABADF',
                        command=select_file_1).place(x=220, y=150)

btn2 = tk.Button(root, text='  Виберіть Excel файл №2  ', 
                        font=60, 
                        bg='#979DBF',
                        activebackground='#9ABADF',
                        command=select_file_2).place(x=220, y=190)

btn3 = tk.Button(root, text='  Виберіть Excel файл №3  ', 
                        font=60, 
                        bg='#979DBF',
                        activebackground='#9ABADF',
                        command=select_file_3).place(x=220, y=230)

# Кнопка запуску программи
btn4 = tk.Button(root, text='  Продовжити  ', 
                        image=photo2,
                        font=('Times New Roman', 12, 'bold', 'italic'), 
                        bg='#979DBF',
                        activebackground='#9ABADF',
                        compound = LEFT
                        ).place(x=1030, y=690)

btn5 = tk.Button(root, text='Підтвердити',
                        font=('Times New Roman', 14), 
                        bg='#98B3D1',
                        activebackground='#9ABADF',
                        command=check_n).place(x=680, y=235)

btn6 = tk.Button(root, command=show_date, 
                        text="Підтвердити дату", 
                        font=('Times New Roman', 14),
                        bg='#98B3D1',
                        activebackground='#9ABADF').place(x=680, y=75)

# tk.Button(root, text='Вибрати все', command=select_all).place(x=680, y=220)

# Тексти на інтерфейсі
label_1 = tk.Label(root, text=' Введіть місяць: ',
                    bg='#979DBF',
                    font=('Times New Roman', 24)
                    ).place(x=220, y=22)

label_2 = tk.Label(root, text=' Виберіть рік: ',
                    bg='#979DBF',
                    font=('Times New Roman', 24)
                    ).place(x=679, y=22)
                        
# Флажкі (вибір бажаних звітів по галочці)
Zvit_01 = tk.Checkbutton(root, text='Віртуальний звіт №1',
                        font=60, 
                        bg='#979DBF',
                        activebackground='#9ABADF',
                        width=35,
                        anchor='w',
                        variable=Yes_Zvit_01,
                        onvalue =1,
                        offvalue=0).place(x=680, y=150, height=34)


Zvit_02 = tk.Checkbutton(root, text='Віртуальний тетстетс звіт №2',
                        font=60, 
                        bg='#979DBF',
                        activebackground='#9ABADF',
                        width=35,
                        anchor='w',
                        variable=Yes_Zvit_02,
                        onvalue =1,
                        offvalue=0).place(x=680, y=190, height=34)

# Активація кнопок
# btn1.pack()
# btn2.pack()
# btn3.pack()
month_print.place(x=458, y=22, height=41)
year_print.place(x=888, y=22, height=41)






root.mainloop()
print(result1, result2)
print("Ви вибрали {} рік і {} місяць для формування звіту".format(current_y, current_m))    

