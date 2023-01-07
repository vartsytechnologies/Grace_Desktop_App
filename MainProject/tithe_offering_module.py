from tkinter import *
from tkinter import ttk
import datetime
import tithe_backend
from tkinter.ttk import Notebook,Style
from tkinter import messagebox


class Tithe:
    def __init__(self,master):
        self.master = master
        self.master = master
        self.master.title("Grace Chapel")
        self.master.geometry("1400x750+0+0")
        self.master.resizable(0, 0)

        self.date = StringVar()

        def tithe():
            self.tframe = Frame(self.master, width=1400, height=720, )
            self.tframe.place(relx=0, rely=0)
            self.menubar = Menu(self.tframe, background="red", fg="white")
            master.config(menu=self.menubar)
            self.file_menu = Menu(self.menubar, tearoff=0)
            self.file_menu.add_command(label='Add Members')
            self.file_menu.add_command(label='Open...')
            self.file_menu.add_command(label='Close', command=master.destroy)
            self.file_menu.add_command(label='Settings')
            self.file_menu.add_separator()

            self.give_menu = Menu(self.menubar, tearoff=0)
            self.give_menu.add_command(label='Tithes')
            self.give_menu.add_command(label='Offering')
            self.give_menu.add_command(label='Pledges')
            self.give_menu.add_command(label='Send Reminders')
            self.file_menu.add_command(label='Dashboard', command="main")
            self.menubar.add_cascade(label='Add Members', menu=self.file_menu, font=("arial", 20), command="add_mem")
            self.menubar.add_cascade(label='Tithes and Offering', menu=self.give_menu)
            self.menubar.add_cascade(label='Attendance', menu=self.file_menu)
            self.menubar.add_cascade(label='Settings', menu=self.file_menu)
            self.sideframe = Frame(self.tframe, width=1400, height=670, bg="#9A0033", bd=2, )
            self.sideframe.place(relx=0, rely=0.07)

            self.con_frame = Frame(self.tframe, width=1400, height=700)
            self.con_frame.place(relx=0.2, rely=0)
            self.nav_frame = Frame(self.tframe, width=1400, height=55, bg="#9A0033", bd=2, relief=SUNKEN)
            self.nav_frame.place(relx=0, rely=0)
            self.tnav_label = Label(self.nav_frame, text="GRACE CHAPEL TITHE AND OFFERING DATA",
                                    font=("arial", 18, "bold"), fg="white", bg="#9A0033")
            self.tnav_label.place(relx=0.3, rely=0.36)

            """def StudentRec2(event):
                try:
                    global selected_tuple

                    index = self.listbox_tithe.curselection()[0]
                    selected_tuple = self.listbox_tithe.get(index)

                    self.mem_id.delete(0, END)
                    self.mem_id.insert(END, selected_tuple[1])
                    self.name1.delete(0, END)
                    self.name1.insert(END, selected_tuple[2])
                    self.month.delete(0, END)
                    self.month.insert(END, selected_tuple[3])
                    self.amount.delete(0, END)
                    self.amount.insert(END, selected_tuple[4])
                    self.date.delete(0, END)
                    self.date.insert(END, selected_tuple[5])

                except IndexError:
                    pass"""

            def Send():
                if (len(self.mem_id.get()) != 0):
                    tithe_backend.Insert(self.mem_id.get(), self.name1.get(), self.month.get(), self.amount.get(),
                                         self.date.get()
                                         )

                else:
                    messagebox.showwarning("Input Error", "Please Fill the form before submission")

            Mysky = "#DCF0F2"
            Myyellow = "#F2C84B"

            style = Style()

            """style.theme_create("dummy", parent="alt", settings={
                "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
                "TNotebook.Tab": {
                    "configure": {"padding": [5, 1], "background": Mysky},
                    "map": {"background": [("selected", Myyellow)],
                            "expand": [("selected", [1, 1, 1, 0])]}}})"""

            # style.theme_use("dummy")

            self.tabcontrol = ttk.Notebook(self.con_frame, width=1300, height=700)
            self.offer = Frame(self.tabcontrol)
            self.tithe = Frame(self.tabcontrol)
            self.pledge = Frame(self.tabcontrol)
            self.t_db = Frame(self.tabcontrol)
            self.tabcontrol.add(self.offer, text="OFFECTORY")
            self.tabcontrol.add(self.tithe, text="TITHE")
            self.tabcontrol.add(self.pledge, text="PLEDGE")
            self.tabcontrol.add(self.t_db, text="TITHE DATABASE")
            self.tabcontrol.place(relx=0, rely=0.08)
            self.entry_frame = Frame(self.tithe, width=700, height=250, bd=3, relief=SUNKEN)
            self.entry_frame.place(relx=0, rely=0)
            self.btn_frame = Frame(self.tithe, width=200, height=250, bd=3, relief=SUNKEN)
            self.btn_frame.place(relx=.65, rely=0)

            self.bt_1 = Button(self.btn_frame, text="SAVE DATA", font=("times new roman", 14), width=15, command=Send)
            self.bt_1.place(relx=0.04, rely=0.02)
            self.bt_1 = Button(self.btn_frame, text="UPDATE TITHER", font=("times new roman", 14), width=15,
                               command="Update")
            self.bt_1.place(relx=0.04, rely=0.25)
            self.bt_1 = Button(self.btn_frame, text="DELETE TITHER", font=("times new roman", 14), width=15,
                               command="delkey")
            self.bt_1.place(relx=0.04, rely=0.48)
            self.bt_1 = Button(self.btn_frame, text="DISPLAY TITHER", font=("times new roman", 14), width=15,
                               command="Display1")
            self.bt_1.place(relx=0.04, rely=0.71)

            self.btn_frame2 = Frame(self.tithe, width=140, height=250, bd=2, relief=SUNKEN, )
            self.btn_frame2.place(relx=0.55, rely=0.0)
            self.bt_1 = Button(self.btn_frame2, text="IMPORT", font=("times new roman", 14), width=12, command="Display")
            self.bt_1.place(relx=0.04, rely=0.02)
            self.bt_1 = Button(self.btn_frame2, text="ADD", font=("times new roman", 14), width=12, command="add_mem")
            self.bt_1.place(relx=0.04, rely=0.25)
            self.bt_1 = Button(self.btn_frame2, text="RESET", font=("times new roman", 14), width=12, command="reset1")
            self.bt_1.place(relx=0.04, rely=0.48)
            self.bt_1 = Button(self.btn_frame2, text="CLOSE", font=("times new roman", 14), width=12, )
            self.bt_1.place(relx=0.04, rely=0.71)

            self.lbl1 = Label(self.entry_frame, text="Member ID", font=("times new roman", 14))
            self.lbl1.place(relx=0.05, rely=0.0)
            self.entry1 = Entry(self.entry_frame, font=("times new roman", 14), width=25, textvariable="self.mem_id")
            self.entry1.place(relx=0.25, rely=0.0)
            self.lbl2 = Label(self.entry_frame, text="Name", font=("times new roman", 14))
            self.lbl2.place(relx=0.05, rely=0.2)
            self.entry2 = Entry(self.entry_frame, font=("times new roman", 14), width=25, textvariable="self.name1")
            self.entry2.place(relx=0.25, rely=0.2)
            self.lbl3 = Label(self.entry_frame, text="Month", font=("times new roman", 14))
            self.lbl3.place(relx=0.05, rely=0.4)
            self.entry3 = ttk.Combobox(self.entry_frame, font=("times new roman", 14), width=25,
                                       textvariable="self.month", value=(
                "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"))
            self.entry3.place(relx=0.25, rely=0.4)
            self.lbl4 = Label(self.entry_frame, text="Amount Paid", font=("times new roman", 14))
            self.lbl4.place(relx=0.05, rely=0.6)
            self.entry4 = Entry(self.entry_frame, font=("times new roman", 14), width=25, textvariable="self.amount")
            self.entry4.place(relx=0.25, rely=0.6)
            self.lbl5 = Label(self.entry_frame, text="Date Paid", font=("times new roman", 14))
            self.lbl5.place(relx=0.05, rely=0.8)

            def gen_date():
                # self.entry6.config()
                self.time_today = datetime.datetime.now()
                self.date.set(f" {self.time_today}")

            self.entry6 = Entry(self.entry_frame, font=("times new roman", 14), width=25, textvariable=self.date)
            self.entry6.place(relx=0.25, rely=0.8)
            gen_date()

            self.picture_frame_1 = Frame(self.entry_frame, width=200, height=200, bd=2, relief=SUNKEN)
            self.picture_frame_1.place(relx=0.7, rely=0.05)
            # ======================================Tither Id ===========================================

            self.btn_img_id_1 = Label(self.picture_frame_1, bg="white")
            self.btn_img_tithe = PhotoImage(file="graphics/id.png")
            self.btn_img_id_1.config(image=self.btn_img_tithe)
            self.btn_img_id_1.place(relx=0, rely=0)

            self.listbox_frame = Frame(self.tithe, width=1050, height=300, bd=3, relief=SUNKEN)
            self.listbox_frame.place(relx=0, rely=0.45)
            self.scrollbarx = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.listbox_frame, orient=VERTICAL)

            self.scrollbarx.place(relx=0.08, rely=0.9, width=12000)
            self.listbox = Listbox(self.listbox_frame, width=170, height=15, bd=3)
            self.listbox.place(relx=0, rely=0)
            self.listbox.bind('<<ListboxSelect>>', "StudentRec")

            self.scrollbary.config(command=self.listbox.yview)
            self.scrollbary.place(relx=0.98, rely=0, height=270)
            self.scrollbarx.config(command=self.listbox.xview)
            self.scrollbarx.place(relx=0, rely=0.87, width=1022)

            """self.scrollbarx_tithe = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
            self.scrollbary_tithe = Scrollbar(self.listbox_frame, orient=VERTICAL)
            self.listbox_tithe = Listbox(self.listbox_frame, width=83, height=15, bd=2)
            self.listbox_tithe.place(relx=0.5, rely=0)
            self.listbox_tithe.bind('<<ListboxSelect>>', StudentRec2)
            self.scrollbary_tithe.config(command=self.listbox_tithe.yview)
            self.scrollbary_tithe.place(relx=0.98, rely=0, height=270)
            self.scrollbarx_tithe.config(command=self.listbox_tithe.xview)
            self.scrollbarx_tithe.place(relx=0.5, rely=0.87, width=430)"""

            self.search1 = Entry(self.tithe, width=26, font=("times new roman", 15), textvariable="look")
            self.search1.place(relx=0.02, rely=0.4)
            self.search_btn1 = Button(self.tithe, text="SEARCH", font=("times new roman", 10),
                                      bd=2)
            self.search_btn1.place(relx=0.22, rely=0.4)

            """self.search2 = Entry(self.tithe, width=26, font=("times new roman", 15), textvariable="say")
            self.search2.place(relx=0.45, rely=0.4)
            self.search_btn2 = Button(self.tithe, text="SEARCH", font=("times new roman", 10),command = Search_payee,
                                      bd=2)
            self.search_btn2.place(relx=0.65, rely=0.4)"""

            def Reset_tithe():
                self.amount.set("GHC")

            def search_win():
                self.search_win = Toplevel()
                self.search_win.geometry("400x200+500+300")
                self.search_win.resizable(0, 0)
                self.search_win.title("Search Tithers")



                self.search_L = Label(self.search_win, text="SEARCH TITHE PAYER", font=("times new roman", 12))
                self.search_L.place(relx=0.08, rely=0.2)

                self.search_entry = Entry(self.search_win, width=30, font=("times new roman", 15), fg="purple")
                self.search_entry.place(relx=0.1, rely=0.34)

                self.search_LBtn = Button(self.search_win, text="SEARCH", font=("times new roman", 13), width=23,
                                          command="SearchRecord_tithe")
                self.search_LBtn.place(relx=0.2, rely=0.54)




            self.scrollbarx = Scrollbar(self.t_db, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.t_db, orient=VERTICAL)
            self.tree = ttk.Treeview(self.t_db, columns=(
                'S/N', "Membership ID", "Name", "Month Of Payment", "Amount Paid", "Date Of Payment"),
                                     selectmode="extended", height=13, yscrollcommand=self.scrollbary.set,
                                     xscrollcommand=self.scrollbarx.set)
            # self.tree.configure(selectmode="extended")
            style = Style()
            style.configure("Treeview.Heading", font=("times new roman", 15, "bold"), foreground='purple')
            style.configure("Treeview", highlightthickness=4, bd=2, font=('times new roman', 14,), foreground='purple')
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.place(relx=0.94, rely=0.0, height=510)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.place(relx=0.02, rely=0.74, width=900)

            self.tree.heading('S/N', text="S/N", anchor=W)
            self.tree.heading('Membership ID', text="Membership ID", anchor=W)
            self.tree.heading('Name', text="Name", anchor=W)
            self.tree.heading('Month Of Payment', text="Month Of Payment", anchor=W)
            self.tree.heading('Amount Paid', text="Amount Paid", anchor=W)
            self.tree.heading('Date Of Payment', text="Date Of Payment", anchor=W)

            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=150)
            self.tree.column('#2', stretch=NO, minwidth=0, width=150)
            self.tree.column('#3', stretch=NO, minwidth=0, width=150)
            self.tree.column('#4', stretch=NO, minwidth=0, width=150)
            self.tree.column('#5', stretch=NO, minwidth=0, width=150)
            self.tree.column('#6', stretch=NO, minwidth=0, width=150)

            self.tree.place(relx=0.02, rely=0.0, width=1040, height=500)

            self.a_btn_Frame = Frame(self.t_db, width=900, height=50, bd=2, relief=SUNKEN)
            self.a_btn_Frame.place(relx=0.03, rely=0.78)
            self.display_btn = Button(self.a_btn_Frame, text="DISPLAY", font=("times new roman", 14),
                                      command="DisplayData_tithe")
            self.display_btn.place(relx=0.02, rely=0.1)
            self.export_btn = Button(self.a_btn_Frame, text="EXPORT TO EXCEL", font=("times new roman", 14))
            self.export_btn.place(relx=0.15, rely=0.1)
            self.delete_btn = Button(self.a_btn_Frame, text="DELETE RECORD", font=("times new roman", 14),
                                     command="delete_tithe")
            self.delete_btn.place(relx=0.4, rely=0.1)
            self.delete_btn = Button(self.a_btn_Frame, text="SEARCH RECORDS", font=("times new roman", 14),
                                     command=search_win)

            self.delete_btn.place(relx=0.6, rely=0.1)
            self.delete_btn = Button(self.a_btn_Frame, text="CLEAR DATA", font=("times new roman", 14),
                                     command="delete_tithe")
            self.delete_btn.place(relx=0.82, rely=0.1)
        tithe()

master = Tk()
obj = Tithe(master)
master.mainloop()