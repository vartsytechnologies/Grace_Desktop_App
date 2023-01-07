from tkinter import *
from tkinter import ttk

class membership:
    def __init__(self,master):
        self.master = master
        self.master.title("Grace Chapel")
        self.master.geometry("1400x750+0+0")
        self.master.resizable(0, 0)


        def membership():
            self.frame_4 = Frame(self.master, width=1400, height=750)
            self.frame_4.place(relx=0, rely=0)

            self.menubar = Menu(self.frame_4, background="red", fg="white")
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

            self.nav_frame_4 = Frame(self.master, width=1400, height=60, bg="#9A0033")
            self.nav_frame_4.place(relx=0, rely=0)

            self.display_btn = Button(self.nav_frame_4, text="DISPLAY", font=("times new roman", 15, "bold"), bg="#9A0033",
                                      fg="white", bd=0, command="DisplayData")
            self.display_btn.place(relx=0.85, rely=0.28)

            self.search = Entry(self.nav_frame_4, width=35, font=("times new roman", 15), textvariable="self.SEARCH")
            self.search.place(relx=0.4, rely=0.28)
            self.search_btn = Button(self.nav_frame_4, text="SEARCH", font=("times new roman", 10), bg="blue", fg="white",
                                     command="SearchRecord")
            self.search_btn.place(relx=0.65, rely=0.28)

            self.nav_frame_5 = Frame(self.master, width=1400, height=30, bg="white", relief=RAISED, bd=1)
            self.nav_frame_5.place(relx=0, rely=0.08)

            self.nav_label_1 = Label(self.nav_frame_5, text="ACTIONS", font=("times new roman", 12), bg="white", fg="black")
            self.nav_label_1.place(relx=0.1, rely=0)

            self.tree_frame = Frame(self.frame_4, width=1050, height=640)
            self.tree_frame.place(relx=0.2, rely=0.1)

            self.scrollbarx = Scrollbar(self.tree_frame, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.tree_frame, orient=VERTICAL)
            self.tree = ttk.Treeview(self.tree_frame, columns=(
                'S/N', "Membership ID", "Name", "Membership Type", "Place Of Birth", "Date Of Birth", "Gender", "Department",
                "Telephone", "Address", "Email", "Marital Status", "Occupation", "Fax", "Employer", "HomeTown", "Region",
                "Pays Tithe?", "Mode Of Visit", "Health Status", "Company Name", "Post Address", "Emerg. Contact",
                "Education Level", "Name Of Institution"),
                                     selectmode="extended", height=18, yscrollcommand=self.scrollbary.set,
                                     xscrollcommand=self.scrollbarx.set)
            # self.tree.configure(selectmode="extended")
            style = ttk.Style()
            # Pick a theme
            style.theme_use('clam')

            style.configure("Treeview.Heading", font=("times new roman", 15, "bold"), foreground='blue',
                            fieldbackground="silver")
            style.configure("Treeview", highlightthickness=4, bd=2, font=('times new roman', 15,), background="silver",
                            foreground="white"
                            , rowheight=40, fieldbackground="silver")
            style.map('Treeview', background=[('selected', 'green')])
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.place(relx=0.95, rely=0.05, height=500)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.place(relx=0.08, rely=0.9, width=900)

            self.tree.heading('S/N', text="S/N", anchor=W)
            self.tree.heading('Membership ID', text="Membership ID", anchor=W)
            self.tree.heading('Name', text="Name", anchor=W)
            self.tree.heading('Membership Type', text="Membership Type", anchor=W)
            self.tree.heading('Place Of Birth', text="Place Of Birth", anchor=W)
            self.tree.heading('Date Of Birth', text="Date Of Birth", anchor=W)
            self.tree.heading('Gender', text="Gender", anchor=W)
            self.tree.heading('Department', text="Department", anchor=W)
            self.tree.heading('Telephone', text="Telephone", anchor=W)
            self.tree.heading('Address', text="Address", anchor=W)
            self.tree.heading('Email', text="Email", anchor=W)
            self.tree.heading('Marital Status', text="Marital Status", anchor=W)
            self.tree.heading('Occupation', text="Occupation", anchor=W)
            self.tree.heading('Fax', text="Fax", anchor=W)
            self.tree.heading('Employer', text="Employer", anchor=W)
            self.tree.heading('HomeTown', text="HomeTown", anchor=W)
            self.tree.heading('Region', text="Region", anchor=W)
            self.tree.heading('Pays Tithe?', text="Pays Tithe?", anchor=W)
            self.tree.heading('Mode Of Visit', text="Mode Of Visit", anchor=W)
            self.tree.heading('Health Status', text="Health Status", anchor=W)
            self.tree.heading('Company Name', text="Company Name", anchor=W)
            self.tree.heading('Post Address', text="Post Address", anchor=W)
            self.tree.heading('Emerg. Contact', text="Emerg. Contact", anchor=W)
            self.tree.heading('Education Level', text="Education Level", anchor=W)
            self.tree.heading('Name Of Institution', text="Name Of Institution", anchor=W)

            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=150)
            self.tree.column('#2', stretch=NO, minwidth=0, width=150)
            self.tree.column('#3', stretch=NO, minwidth=0, width=150)
            self.tree.column('#4', stretch=NO, minwidth=0, width=150)
            self.tree.column('#5', stretch=NO, minwidth=0, width=150)
            self.tree.column('#6', stretch=NO, minwidth=0, width=150)
            self.tree.column('#6', stretch=NO, minwidth=0, width=150)
            self.tree.column('#7', stretch=NO, minwidth=0, width=150)
            self.tree.column('#8', stretch=NO, minwidth=0, width=150)
            self.tree.column('#9', stretch=NO, minwidth=0, width=150)
            self.tree.column('#10', stretch=NO, minwidth=0, width=150)
            self.tree.column('#11', stretch=NO, minwidth=0, width=150)
            self.tree.column('#12', stretch=NO, minwidth=0, width=150)
            self.tree.column('#13', stretch=NO, minwidth=0, width=150)
            self.tree.column('#14', stretch=NO, minwidth=0, width=150)
            self.tree.column('#15', stretch=NO, minwidth=0, width=150)
            self.tree.column('#16', stretch=NO, minwidth=0, width=150)
            self.tree.column('#17', stretch=NO, minwidth=0, width=150)
            self.tree.column('#18', stretch=NO, minwidth=0, width=150)
            self.tree.column('#19', stretch=NO, minwidth=0, width=150)
            self.tree.column('#20', stretch=NO, minwidth=0, width=150)
            self.tree.column('#21', stretch=NO, minwidth=0, width=150)
            self.tree.column('#22', stretch=NO, minwidth=0, width=150)
            self.tree.column('#23', stretch=NO, minwidth=0, width=150)
            self.tree.column('#24', stretch=NO, minwidth=0, width=150)

            self.tree.place(relx=0.08, rely=0.03, width=900, height=550)
            self.tree.tag_configure('oddrow', background='lightblue')
            self.tree.tag_configure('evenrow', background='white')
            self.tree.bind("<Double-1>", "double_tap")

            self.side_frame1 = Frame(self.frame_4, width=320, height=640, bg="white", relief="raised")
            self.side_frame1.place(relx=0, rely=0.06)

            self.btn_1 = Button(self.side_frame1, text="Add New Members", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white",
                                command="add_mem")
            self.btn_1.place(relx=0.2, rely=0.1)
            self.btn_2 = Button(self.side_frame1, text="Edit this Member", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_2.place(relx=0.2, rely=0.15)
            self.btn_3 = Button(self.side_frame1, text="Delete this member", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white",
                                command="delete")
            self.btn_3.place(relx=0.2, rely=0.2)

            self.btn_4 = Button(self.side_frame1, text="send email to this member", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_4.place(relx=0.2, rely=0.25)

            self.btn_5 = Button(self.side_frame1, text="Send mass email to view", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_5.place(relx=0.2, rely=0.3)

            self.btn_6 = Button(self.side_frame1, text="send text/sms to this person", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_6.place(relx=0.2, rely=0.35)

            self.btn_7 = Button(self.side_frame1, text="send mass text/sms to view", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_7.place(relx=0.2, rely=0.4)
            self.btn_5 = Button(self.side_frame1, text="Record Church attendance", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_5.place(relx=0.2, rely=0.45)

            self.btn_img_a = Label(self.side_frame1, bg="white")
            self.btn_img = PhotoImage(file="graphics/edit.png")
            self.btn_img_a.config(image=self.btn_img)
            self.btn_img_a.place(relx=0.1, rely=0.154)

            self.btn_img_b = Label(self.side_frame1, bg="white")
            self.btn_img_1 = PhotoImage(file="graphics/del.png")
            self.btn_img_b.config(image=self.btn_img_1)
            self.btn_img_b.place(relx=0.1, rely=0.2)

            self.btn_img_c = Label(self.side_frame1, bg="white")
            self.btn_img_2 = PhotoImage(file="graphics/mail.png")
            self.btn_img_c.config(image=self.btn_img_2)
            self.btn_img_c.place(relx=0.1, rely=0.256)

            self.btn_img_d = Label(self.side_frame1, bg="white")
            self.btn_img_3 = PhotoImage(file="graphics/mail.png")
            self.btn_img_d.config(image=self.btn_img_3)
            self.btn_img_d.place(relx=0.1, rely=0.31)

            self.btn_img_e = Label(self.side_frame1, bg="white")
            self.btn_img_4 = PhotoImage(file="graphics/sms.png")
            self.btn_img_e.config(image=self.btn_img_4)
            self.btn_img_e.place(relx=0.1, rely=0.356)

            self.btn_img_f = Label(self.side_frame1, bg="white")
            self.btn_img_5 = PhotoImage(file="graphics/sms.png")
            self.btn_img_f.config(image=self.btn_img_5)
            self.btn_img_f.place(relx=0.1, rely=0.41)

            self.btn_img_g = Label(self.side_frame1, bg="white")
            self.btn_img_6 = PhotoImage(file="graphics/attend.png")
            self.btn_img_g.config(image=self.btn_img_6)
            self.btn_img_g.place(relx=0.1, rely=0.456)

            self.btn_img_h = Label(self.side_frame1, bg="white")
            self.btn_img_7 = PhotoImage(file="graphics/new.png")
            self.btn_img_h.config(image=self.btn_img_7)
            self.btn_img_h.place(relx=0.1, rely=0.09)

            separator2 = Frame(self.side_frame1, width=300, height=2)
            separator2.place(relx=0, rely=0.55)

            self.picture_frame = Frame(self.side_frame1, width=200, height=200, bd=1, relief=SUNKEN)
            self.picture_frame.place(relx=0.18, rely=0.58)

            self.id = "GCI/ZT/25614525"
            self.member_id = Label(self.side_frame1, text="ID: " + " " + self.id, bg="white", fg="blue",
                                   font=("times new roman", 15))
            self.member_id.place(relx=0.2, rely=0.9)

            self.btn_img_id = Label(self.picture_frame, bg="white")
            self.btn_img_8 = PhotoImage(file="graphics/id.png")
            self.btn_img_id.config(image=self.btn_img_8)
            self.btn_img_id.place(relx=0, rely=0)
        membership()

master = Tk()
obj = membership(master)
master.mainloop()