import os
from tkinter import *
from tkinter import ttk
import pandas as pd
from data_manager import DataManager
import interface_controller


def update_search():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.configure(state='disabled')
    if list1.get() == "" or list2.get() == "" or combobox1.get() == "":
        text.configure(state='normal')
        text.insert('end', "Please specify all conditions.")
        text.configure(state='disabled')
        return
    start_time, end_time, vehicle_type = interface_controller.get_content_search([list1, list2, combobox1])
    search_outcome = data_manager.search(start_time, end_time, vehicle_type).df[:]
    text.configure(state='normal')
    if search_outcome.empty:
        text.insert('end', "Sorry, here is no matched record.")
    else:
        text.insert('end', search_outcome)  # 插入到text
    text.configure(state='disabled')
    list1.set('')
    list2.set('')
    combobox1.set('')



def update_sort():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.configure(state='disabled')
    if str(e1.get()).isdigit()==False or combobox2.get() == "" or combobox3.get() == "":
        text.configure(state='normal')
        text.insert('end', 'Your input is illegal')
        text.configure(state='disabled')
    else:
        ascending, column_index, number_of_entry_to_show = interface_controller.get_content_sort([combobox2, combobox3, e1])
        sort_outcome = data_manager.sort(column_index, ascending).df[: number_of_entry_to_show]
        text.configure(state='normal')
        text.insert('end', sort_outcome)  # 插入到text
        text.configure(state='disabled')
        combobox3.set('')
        combobox2.set('')
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
width = 800
height = 600
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
myWindow.geometry(alignstr)
# 设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=True, height=True)

# design mywindow
Label(myWindow, text="search", font=('Arial 16 bold'), width=10, height=2).place(rely=0.02, relx=0.01)
Label(myWindow, text="start time(h:m:s)", font=('Arial 12 bold'), width=15, height=1).place(rely=0.1, relx=0.1)
Label(myWindow, text="end time(h:m:s)", font=('Arial 12 bold'), width=15, height=1).place(rely=0.1, relx=0.3)
Label(myWindow, text="Vehicle Type", font=('Arial 12 bold'), width=15, height=1).place(rely=0.1, relx=0.5)

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
# list2.current(0)
list1.place(relx=0.1, rely=0.15)
list2.place(relx=0.3, rely=0.15)

veh_value = StringVar()
veh_values = ['5', '31', '32', '41', '42']
combobox1 = ttk.Combobox(master=myWindow, state='readonly', textvariable=veh_value, values=veh_values,width=15)
combobox1.place(relx=0.5, rely=0.15)

b1 = Button(myWindow, text='search', font=('Helvetica 10 bold'), width=8, height=1, command=update_search)
b1.place(relx=0.75, rely=0.15)

#sort part
Label(myWindow, text="sort", font=('Arial 16 bold'), width=10, height=2).place(rely=0.22, relx=0.01)
Label(myWindow, text="sort method", font=('Arial 12 bold'), width=15, height=1).place(relx=0.1, rely=0.3)
Label(myWindow, text="sorting column", font=('Arial 12 bold'), width=15, height=1).place(relx=0.3, rely=0.3)
Label(myWindow, text="number of entry to show", font=('Arial 12 bold'), width=20, height=1).place(relx=0.5, rely=0.3)

sort_value = StringVar()
sort_values = ['Ascending order', 'Descending order']
combobox2 = ttk.Combobox(master=myWindow, state='readonly', textvariable=sort_value, values=sort_values,width=15)
combobox2.place(relx=0.1, rely=0.35)

sort_column=StringVar()
sort_columns=[1,2,3,4,5,6,7,8]
combobox3 = ttk.Combobox(master=myWindow, state='readonly', textvariable=sort_column, values=data_manager.column_names,width=15)
combobox3.place(relx=0.3, rely=0.35)

e1 = Entry(myWindow, width=15)
e1.place(relx=0.5, rely=0.35)

b2 = Button(myWindow, text='sort', font=('Helvetica 10 bold'), width=8, height=1, command=update_sort)
b2.place(relx=0.75, rely=0.35)

# Show text
frame = Frame(myWindow,height =50,width = 52)
frame.place(relx=0.05, rely=0.4)
s_y = Scrollbar(frame)
s_y.pack(side=RIGHT, fill=Y)
s_x = Scrollbar(frame, orient=HORIZONTAL)
s_x.pack(side=BOTTOM, fill=X)
# text = Text(master=frame, font=('Helvetica 10 bold'),yscrollcommand=s_y.set, xscrollcommand=s_x.set,)
text = Text(
            master=frame,  # 父容器
            bg='white',  # 背景颜色
            fg='black',  # 文本颜色
            relief='sunken',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 10),  # 字体
            wrap='none',  # 字数够width后是否换行 char, none,  word
            yscrollcommand=s_y.set,  # 滚动条
            xscrollcommand=s_x.set,  # 滚动条
            )
s_y.config(command=text.yview)
s_x.config(command=text.xview)
text.configure(state='disabled')
text.pack()
myWindow.mainloop()
