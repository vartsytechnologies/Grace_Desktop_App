from tkinter import *
from tkinter import ttk
import time

class Mainpage:
    def __init__(self,master):
        self.master = master
        self.master.title("Grace Chapel")
        self.master.geometry("1400x750+0+0")
        self.master.resizable(0, 0)

#======================================================text variables============================================
        self.card_ent1 = StringVar()
        self.card_ent2 = StringVar()
        self.card_ent3 = StringVar()

        def welcome():
            self.frame_1 = Frame(self.master, width=1400, height=750, bg="white")
            self.frame_1.place(relx=0, rely=0)
            self.frame_1_1 = Frame(self.master, width=1400, height=400, bg="#9A0033")
            self.frame_1_1.place(relx=0, rely=0.3)
            self.church_logo = Label(self.frame_1_1, bg="#9A0033")
            self.img_1_1 = PhotoImage(file="graphics/church.png")
            self.church_logo.config(image=self.img_1_1)
            self.church_logo.place(relx=0.8, rely=0.1)
            self.label = "GRACE CHAPEL INTERNATIONAL\n(2022)"
            self.lbl_1 = Label(self.frame_1, text=self.label, bg="white", fg="blue",
                               font=("times new romans", 35, "bold"))
            self.lbl_1.place(relx=0.26, rely=0.08)
            self.label2 = "Powered by VARTSY"
            self.lbl_2 = Label(self.frame_1, text=self.label2, bg="white", fg="blue",
                               font=("times new romans", 12, "bold"))
            self.lbl_2.place(relx=0.47, rely=0.85)
            # =================================================phot logo ======================================================
            self.image_lbl = Label(self.frame_1)
            self.logo = PhotoImage(file="graphics/lmis.png")
            self.image_lbl.config(image=self.logo, bg="white")
            self.image_lbl.place(relx=0.08, rely=0)

            self.msg = "For God So loved the world that he gave his only begotten son \n that whosoever believes in him should not perish but \n have everlasting life\n (Ephesians 6:1)"
            self.msg_lbl = Label(self.frame_1_1, text=self.msg, font=("times new romans", 20), bg="#9A0033", fg="white")
            self.msg_lbl.place(relx=0.2, rely=0.3)
            # ==================================================get started============================================================
            self.btn = Button(self.frame_1_1, command=get)
            self.img2 = PhotoImage(file="graphics/get.png")
            self.btn.config(image=self.img2, bg="#9A0033", bd=0)
            self.btn.place(relx=0.45, rely=0.75)
            self.lbl_3 = Label(self.frame_1_1, text="GET STARTED", font=("times new romans", 12, "bold"), bg="white",
                               fg="purple")
            self.lbl_3.place(relx=0.48, rely=0.82)

        def Sign():
            self.frame_2 = Frame(self.master, width=1400, height=750, )
            self.frame_2.place(relx=0, rely=0)

            def Time():
                hour = time.strftime("%I")
                min = time.strftime("%M")
                sec = time.strftime("%S")
                am_pm = time.strftime("%p")

                self.Time.config(text=hour + " : " + min + " : " + sec + " " + am_pm)
                self.Time.after(1000, Time)

            self.Time = Label(self.frame_2, font=("times new romans", 20, "bold"), fg="blue")
            self.Time.place(relx=0.8, rely=0.02)
            Time()

            self.log_frame_1 = Frame(self.frame_2, width=400, height=600, bg="white", bd=1, relief=RAISED)
            self.log_frame_1.place(relx=0.16, rely=0.1)

            self.avatar = Label(self.log_frame_1, bg="white")
            self.avat = PhotoImage(file="graphics/avatar.png")
            self.avatar.config(image=self.avat)
            self.avatar.place(relx=0.26, rely=0.09)
            # =================================================credentials ============================================================
            self.user = Label(self.log_frame_1, text="Username", font=("aquawax", 15), bg="white", fg="blue")
            self.user.place(relx=0.18, rely=0.4)
            self.entimg1 = Label(self.log_frame_1, bg="white")
            self.ent_1_image = PhotoImage(file="graphics/entry.png")
            self.entimg1.config(image=self.ent_1_image)
            self.entimg1.place(relx=0.18, rely=0.6)
            self.entry_2 = Entry(self.log_frame_1, show="*", width=40, bd=0)
            self.entry_2.place(relx=0.2, rely=0.612)

            self.passw = Label(self.log_frame_1, text="Password", font=("aquawax", 15), bg="white", fg="blue")
            self.passw.place(relx=0.18, rely=0.54)
            self.entimg2 = Label(self.log_frame_1, bg="white")
            self.ent_2_image = PhotoImage(file="graphics/entry.png")
            self.entimg2.config(image=self.ent_1_image)
            self.entimg2.place(relx=0.18, rely=0.47)

            self.entry_1 = Entry(self.log_frame_1, width=40, bd=0)
            self.entry_1.place(relx=0.2, rely=0.482)

            self.btn = Button(self.log_frame_1, command=login)
            self.img2 = PhotoImage(file="graphics/loginbtn.png")
            self.btn.config(image=self.img2, bg="white", bd=0)
            self.btn.place(relx=0.3, rely=0.7)

            self.log_frame_2 = Frame(self.frame_2, width=500, height=600, bg="#9A0033", bd=1, relief=RAISED)
            self.log_frame_2.place(relx=0.43, rely=0.1)
            self.txt = "WELCOME BACK\n\nLogin to have full access to this software Now\n"
            self.wel = Label(self.log_frame_2, text=self.txt, font=("times new romans", 15, "bold"), fg="white",
                             bg="#9A0033")
            self.wel.place(relx=0.02, rely=0.4)

            """self.bg = Label(self.log_frame_2, )
            self.back = PhotoImage(file="graphics/f2.png")
            self.bg.config(image=self.back)
            self.bg.place(relx=0, rely=0)"""

        def main():
            self.frame_3 = Frame(self.master, width=1400, height=750)
            self.frame_3.place(relx=0, rely=0)
            self.nav_frame_1 = Frame(self.frame_3, width=1400, height=40, bg="#9A0033")
            self.nav_frame_1.place(relx=0, rely=0)
            self.nav_label = Label(self.nav_frame_1, text="GRACE CHAPEL INTERNATIONAL DATABASE SYSTEM ",
                                   font=("times new romans", 15, "bold"), bg="#9A0033", fg="white")
            self.nav_label.place(relx=0.3, rely=0.3)
            self.menubar = Menu(self.frame_3, background="red", fg="white")
            master.config(menu=self.menubar)
            self.file_menu = Menu(self.menubar, tearoff=0)
            self.file_menu.add_command(label='Add Members')
            self.file_menu.add_command(label='Open...')
            self.file_menu.add_command(label='Close', command=master.destroy)
            self.file_menu.add_command(label='Settings')
            self.file_menu.add_separator()

            self.give_menu = Menu(self.menubar, tearoff=0)
            self.give_menu.add_command(label='Tithes', command="tithe")
            self.give_menu.add_command(label='Offering', command="tithe")
            self.give_menu.add_command(label='Send Reminders')
            self.file_menu.add_command(label='Logout', command=logout)
            self.menubar.add_cascade(label='Add Members', menu=self.file_menu, font=("arial", 20))
            self.menubar.add_cascade(label='Tithes and Offering', menu=self.give_menu)
            self.menubar.add_cascade(label='Attendance', menu=self.file_menu, command="attendance")
            self.menubar.add_cascade(label='Settings', menu=self.file_menu)

            # ======================logo frame===========================
            self.side_frame = Frame(self.frame_3, width=340, height=660, bg="white", relief="raised")
            self.side_frame.place(relx=0, rely=0.0522)

            self.content_frame = LabelFrame(self.frame_3, width=1030, height=680, )
            self.content_frame.place(relx=0.232, rely=0.0522)

            # ===================================cards===============================================
            """def count():
                self.entry_card.config(state="disable", disabledbackground="#9A0033", disabledforeground="white")
                conn = sqlite3.connect("grace1.db")
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM member1")
                result = cur.fetchone()[0]
                self.card_ent1.set(result)"""

            self.card_1 = Frame(self.content_frame, width=200, height=120, relief=RAISED, bd=2, bg="#9A0033")
            self.card_1.place(relx=0.02, rely=0.1)
            self.entry_card = Entry(self.card_1, bg="#9A0033", fg="white", bd=0,
                                    font=("franklin gothic", 42, "bold"), textvariable=self.card_ent1 )
            self.entry_card.place(relx=0.25, rely=0.13)
            #count()
            self.card_1_label = Label(self.card_1, text="Total Members", font=("franklin gothic", 12, "bold"),
                                      bg="#9A0033", fg="white")
            self.card_1_label.place(relx=0.05, rely=0.7)

            self.card_2 = Frame(self.content_frame, width=200, height=120, relief=RAISED, bd=2, bg="#9A0033")
            self.card_2.place(relx=0.23, rely=0.1)
            self.entry_card_2 = Entry(self.card_2, bg="#9A0033", fg="white", bd=0,
                                      font=("franklin gothic", 35, "bold"),
                                      textvariable=self.card_ent2, state="disable", disabledbackground="#9A0033",
                                      disabledforeground="white")
            self.entry_card_2.place(relx=0.25, rely=0.13)

            self.card_2_label = Label(self.card_2, text="Total Present ", font=("franklin gothic", 12, "bold"),
                                      bg="#9A0033", fg="white")
            self.card_2_label.place(relx=0.05, rely=0.7)

            self.card_3 = Frame(self.content_frame, width=200, height=120, relief=RAISED, bd=2, bg="#9A0033")
            self.card_3.place(relx=0.44, rely=0.1)

            self.entry_card_3 = Entry(self.card_3, bg="#9A0033", fg="white", bd=0,
                                      font=("franklin gothic", 35, "bold"),
                                      textvariable=self.card_ent3, state="disable", disabledbackground="#9A0033",
                                      disabledforeground="white")
            self.entry_card_3.place(relx=0.25, rely=0.13)

            self.card_3_label = Label(self.card_3, text="New Members ", font=("franklin gothic", 12, "bold"),
                                      bg="#9A0033", fg="white")
            self.card_3_label.place(relx=0.05, rely=0.7)

            self.graph_frame = Frame(self.content_frame, width=630, height=200, bg="white", relief=RAISED, bd=2)
            self.graph_frame.place(relx=0.02, rely=0.33)

            self.new_frame = Frame(self.content_frame, width=630, height=200, relief=FLAT, bg="white")
            self.new_frame.place(relx=0.02, rely=0.68)

            self.label_mem = Frame(self.new_frame, width=630, height=40, bg="#9A0033")
            self.label_mem.place(relx=0, rely=0)

            self.event_frame = Frame(self.content_frame, width=260, height=300, relief=FLAT, bg="white")
            self.event_frame.place(relx=0.7, rely=0.1)
            self.label_event = Frame(self.event_frame, width=260, height=40, bg="#9A0033")
            self.label_event.place(relx=0, rely=0)

            self.btn_img_12 = Label(self.content_frame, )
            self.btn_img12 = PhotoImage(file="graphics/graph2.png")
            self.btn_img_12.config(image=self.btn_img12)
            self.btn_img_12.place(relx=0.69, rely=0.575)

            # ========================================side_bar ============================

            self.btn_img_1 = Label(self.side_frame, bg="white")
            self.btn_img = PhotoImage(file="graphics/lmis.png")
            self.btn_img_1.config(image=self.btn_img)
            self.btn_img_1.place(relx=0.12, rely=0.01)

            separator1 = Frame(self.side_frame, width=300, height=2)
            separator1.place(relx=0, rely=0.37)

            # ==================================side__bar__buttons============================
            self.btn_1 = Button(self.side_frame, text="Membership", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white",
                                command="member")
            self.btn_1.place(relx=0.2, rely=0.4)
            self.btn_2 = Button(self.side_frame, text="Add New Members", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white",
                                command="add_mem")
            self.btn_2.place(relx=0.2, rely=0.47)
            self.btn_3 = Button(self.side_frame, text="Tithes and Offering", bd=0, fg="blue", bg="white",
                                command="tithe",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_3.place(relx=0.2, rely=0.54)

            self.btn_4 = Button(self.side_frame, text="Ai Attendance System", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white",
                                command="attendance")
            self.btn_4.place(relx=0.2, rely=0.61)

            self.btn_5 = Button(self.side_frame, text="Departments", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_5.place(relx=0.2, rely=0.68)

            separator = Frame(self.side_frame, width=300, height=2)
            separator.place(relx=0, rely=0.75)

            self.btn_6 = Button(self.side_frame, text="Log out", bd=0, fg="blue", bg="white", command=logout,
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_6.place(relx=0.2, rely=0.78)

            self.btn_7 = Button(self.side_frame, text="Settings", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_7.place(relx=0.2, rely=0.85)
            self.btn_5 = Button(self.side_frame, text="Developers", bd=0, fg="blue", bg="white",
                                font=(" times new romans", 14), activeforeground="red", activebackground="white")
            self.btn_5.place(relx=0.2, rely=0.92)

            # =============================================icons==================================================
            self.icon_1 = Label(self.side_frame, bg="white")
            self.icon = PhotoImage(file="graphics/membership.png")
            self.icon_1.config(image=self.icon)
            self.icon_1.place(relx=0.05, rely=0.4)

            self.icon_2 = Label(self.side_frame, bg="white")
            self.icon_a = PhotoImage(file="graphics/offer.png")
            self.icon_2.config(image=self.icon_a)
            self.icon_2.place(relx=0.05, rely=0.54)

            self.icon_3 = Label(self.side_frame, bg="white")
            self.icon_b = PhotoImage(file="graphics/ai.png")
            self.icon_3.config(image=self.icon_b)
            self.icon_3.place(relx=0.06, rely=0.61)

            self.icon_4 = Label(self.side_frame, bg="white")
            self.icon_c = PhotoImage(file="graphics/logout.png")
            self.icon_4.config(image=self.icon_c)
            self.icon_4.place(relx=0.065, rely=0.78)

            self.icon_5 = Label(self.side_frame, bg="white")
            self.icon_d = PhotoImage(file="graphics/dev.png")
            self.icon_5.config(image=self.icon_d)
            self.icon_5.place(relx=0.06, rely=0.92)

            self.icon_6 = Label(self.side_frame, bg="white")
            self.icon_e = PhotoImage(file="graphics/set.png")
            self.icon_6.config(image=self.icon_e)
            self.icon_6.place(relx=0.06, rely=0.85)

            self.icon_7 = Label(self.side_frame, bg="white")
            self.icon_f = PhotoImage(file="graphics/de.png")
            self.icon_7.config(image=self.icon_f)
            self.icon_7.place(relx=0.06, rely=0.68)

            self.icon_9 = Label(self.side_frame, bg="white")
            self.icon_g = PhotoImage(file="graphics/add.png")
            self.icon_9.config(image=self.icon_g)
            self.icon_9.place(relx=0.06, rely=0.47)

        def get():
            self.frame_1.destroy()
            Sign()

        def login():
            self.frame_2.destroy()
            main()
            self.card_ent2.set(3)
            self.card_ent3.set(0)
            """graph()"""

        def logout():
            self.frame_3.destroy()
            Sign()

        welcome()

master = Tk()
obj = Mainpage(master)
master.mainloop()