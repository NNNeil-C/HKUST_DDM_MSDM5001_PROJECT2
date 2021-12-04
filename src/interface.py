import os

from tkinter import *
from tkinter import ttk
import pandas as pd
from data_manager import DataManager
import interface_controller


def update_search():
    text.delete(0.0, END)
    start_time, end_time, vehicle_type = interface_controller.get_content_search([list1, list2, combobox1])
    search_outcome = data_manager.search(start_time, end_time, vehicle_type).df[:]
    text.insert('end', search_outcome)  # 插入到text
    list1.delete(0, END)
    list2.delete(0, END)
    combobox1.delete(0, END)
    text.insert('end', list1.get())


def update_sort():
    text.delete(0.0, END)
    # add one more e2 to the [combobox2, e1, e2], e2 should specify the sorting key column(a number)
    number_of_entry_to_show, column_index, ascending = interface_controller.get_content_sort([combobox2, e1])
    sort_outcome = data_manager.sort(column_index, ascending).df[: number_of_entry_to_show]
    text.insert('end', sort_outcome)  # 插入到text
    combobox2.delete(0, END)
    e1.delete(0, END)


def change(*args):
    global list
    _time = mode.get()
    ind = time_list.index(_time)
    list2["value"] = time_list[ind:]


def init_data_manager(file_path):
    return DataManager(file_path)


file_path = os.getcwd() + r'{0}Traffic_data{0}TDCS_M06A_20190830_080000.csv'.format(os.sep)
print(file_path)
data_manager = init_data_manager(file_path)

# 初始化Tk()
myWindow = Tk()
# 设置标题
myWindow.title('5051 project2')
# 设置窗口大小
width = 680
height = 600
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
myWindow.geometry(alignstr)
# 设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=True, height=True)

# design mywindow
Label(myWindow, text="search", font=('Arial 8 bold'), width=10, height=2).place(rely=0.02, relx=0.01)
Label(myWindow, text="sort", font=('Arial 8 bold'), width=10, height=2).place(rely=0.32, relx=0.01)
Label(myWindow, text="start time(h:m:s)", font=('Arial 8 bold'), width=15, height=1).place(rely=0.1, relx=0.1)
Label(myWindow, text="end time(h:m:s)", font=('Arial 8 bold'), width=15, height=1).place(rely=0.1, relx=0.3)
Label(myWindow, text="Vehicle Type", font=('Arial 8 bold'), width=15, height=1).place(rely=0.1, relx=0.5)

# cimbobox for time
time_list = pd.date_range('20190830 080000', periods=38, freq='0.25H').strftime("%Y-%m-%d %H:%M:%S").to_list()

mode = StringVar()
langlist = StringVar()
list1 = ttk.Combobox(myWindow, textvariable=mode, state="readonly", width=15)
list1.bind("<<ComboboxSelected>>", change)
list1['value'] = time_list
# list1.current(0)

list2 = ttk.Combobox(myWindow, textvariable=langlist, state="readonly", width=15)
list2.config(values=[""])
# list2.current(0)s
list1.place(relx=0.1, rely=0.2)
list2.place(relx=0.3, rely=0.2)

veh_value = StringVar()
veh_values = ['5', '31', '32', '41', '42']
combobox1 = ttk.Combobox(master=myWindow, state='readonly', textvariable=veh_value, values=veh_values)
combobox1.place(relx=0.5, rely=0.2)

b1 = Button(myWindow, text='search', font=('Helvetica 10 bold'), width=8, height=1, command=update_search)
b1.place(relx=0.8, rely=0.2)
Label(myWindow, text="sort method", font=('Arial 8 bold'), width=15, height=1).place(relx=0.1, rely=0.4)
Label(myWindow, text="number of entry to show", font=('Arial 8 bold'), width=15, height=1).place(relx=0.5, rely=0.4)

sort_value = StringVar()

sort_values = ['Ascending order', 'Descending order']
combobox2 = ttk.Combobox(master=myWindow, state='readonly', textvariable=sort_value, values=sort_values)
combobox2.place(relx=0.1, rely=0.5)

e1 = Entry(myWindow, width=10)
e1.place(relx=0.5, rely=0.5)

b2 = Button(myWindow, text='sort', font=('Helvetica 10 bold'), width=8, height=1, command=update_sort)
b2.place(relx=0.7, rely=0.5)

text = Text(myWindow, font=('Helvetica 10 bold'))
text.place(relx=0.1, rely=0.6)
myWindow.mainloop()
