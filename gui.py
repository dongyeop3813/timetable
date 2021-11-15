from tkinter import ttk
from tkinter import *

from data import DataManager

from variable import *


class GUI:
    def __init__(self, root):
        # data manager init
        self.dm = DataManager()

        # root frame setting
        self.root = root
        root.title("Convinient Time Table")
        root.geometry("800x600")
        root.resizable(False, False)

        # frame for check box
        frm = ttk.Frame(root, padding=30)
        frm.grid(row=0, column=0)

        self.departments_checkbox = []
        self.isChecked = []
        for i in range(len(departments)):
            depart = departments[i]
            depart_kr = departments_kr[i]

            temp_var = BooleanVar()
            temp_var.set(False)
            self.isChecked.append(temp_var)

            temp_btn = ttk.Checkbutton(
                frm,
                text=depart_kr,
                variable=temp_var,
                command=self.make_cb_event(i, depart)
            )
            temp_btn.grid(column=0, row=i, sticky="w")
            self.departments_checkbox.append(temp_btn)

        # frame for time table
        time_table = ttk.Frame(root, padding=(0, 50), width=600)
        time_table.grid(row=0, column=1)

        # day label
        for (i, day) in enumerate(days):
            ttk.Label(time_table, text=day, width=10).grid(column=i+1, row=0)

        # time label
        for (i, time) in enumerate(times):
            ttk.Label(
                time_table, text=time, padding=(20, 10)
                ).grid(column=0, row=i+1)

        self.time_table_btn = {}
        for (i, day) in enumerate(days):
            temp = {}
            for (j, time) in enumerate(times):
                temp_btn = ttk.Button(
                    time_table, width=10
                )
                temp_btn.grid(column=i+1, row=j+1)
                temp_btn.bind(
                    "<ButtonPress-1>",
                    self.make_btn_event(day, time)
                    )
                temp[time] = temp_btn
            self.time_table_btn[day] = temp

    def make_cb_event(self, num, depart):
        def event():
            self.checkbox_event(num, self.isChecked[num].get())
        return event

    def make_btn_event(self, day, time):
        def event(e):
            self.button_event(day, time)
        return event

    def checkbox_event(self, num, val: bool):
        if val:
            self.dm.add_depart(num)
        else:
            self.dm.del_depart(num)

    def button_event(self, day, time):
        ret = self.dm.find_by_daytime(day, time)
        select_box(self, ret)

    def select_new_lecture(self, lecture):
        self.dm.add_lecture(lecture['name'])

        lec_day = []
        for day in days:
            if day_kr(day) in lecture['time']:
                lec_day.append(day)
        for time in times:
            if time in lecture['time']:
                lec_time = time

        for day in lec_day:
            temp_btn = self.time_table_btn[day][lec_time]
            temp_btn['text'] = lecture['name']


class select_box:
    def __init__(self, parent, lec_list):
        self.lec_list = lec_list
        self.parent = parent

        self.t = Toplevel(parent.root)

        self.lb = Listbox(self.t, selectmode='extended', width=70)
        for i, lec in enumerate(lec_list):
            temp = lec['id'] + "    " + lec['name'] + '    by ' + lec['prof']
            self.lb.insert(i, temp)

        self.lb.grid()

        self.select_btn = ttk.Button(self.t, text='select', width=10)
        self.select_btn.grid()
        self.select_btn.bind("<ButtonPress-1>", self.button_event)

    def button_event(self, e):
        selection = self.lb.curselection()
        if len(selection) == 0:
            return

        lecture = self.lec_list[selection[0]]
        self.parent.select_new_lecture(lecture)
        self.t.destroy()
        return
