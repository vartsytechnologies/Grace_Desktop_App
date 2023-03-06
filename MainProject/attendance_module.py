from tkinter import *
from tkinter import ttk
import backend_1


class Attendance:
    def __init__(self,master):
        self.master = master
        self.master.title("Grace Chapel")
        self.master.geometry("1400x750+0+0")
        self.master.resizable(0, 0)

        self.sort = StringVar()

        def attendance():
            def view_content():
                self.listbox_at.delete(0, END)
                # for row in backend_1.view():
                #     self.listbox_at.insert(END, f"{row[0]}          {row[1]}          {row[2]}", str(' '))

            self.sort.set("Sort by")
            self.masterframe = Frame(self.master, width=1400, height=750, bg="#9A0033")
            self.masterframe.place(relx=0, rely=0)
            self.sideframe = Frame(self.masterframe, width=250, height=750, bg="#9A0033")
            self.sideframe.place(relx=0, rely=0)
            self.naveframe = Frame(self.masterframe, width=1200, height=90, bg="#9A0033")
            self.naveframe.place(relx=0.1772, rely=0)
            self.main_con = Frame(self.masterframe, width=1100, height=600, bg='white')
            self.main_con.place(relx=0.17, rely=0.12)
            self.nav_label = Label(self.naveframe, text="GRACE CHAPEL ATTENDANCE SYSTEM", font=("arial", 19, "bold"),
                                   bg="#9A0033", fg="white")
            self.nav_label.place(relx=0.2, rely=0.4)

            # =============================================Manual Attendance================================

            self.manual_Frame = Frame(self.main_con, width=590, height=1000, relief=SUNKEN, bd=4)
            self.manual_Frame.place(relx=0, rely=0.0)
            self.listbox_frame = Frame(self.manual_Frame, width=570, height=200, bd=3, relief=SUNKEN)
            self.listbox_frame.place(relx=0, rely=0)
            self.scrollbarx = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.listbox_frame, orient=VERTICAL)

            self.scrollbarx.place(relx=0.08, rely=0.9, width=12000)
            self.listbox_at = Listbox(self.listbox_frame, width=86, height=10, bd=3, font=("times new roman", 13))
            self.listbox_at.place(relx=0.02, rely=0)
            self.listbox_at.bind('<<ListboxSelect>>', "StudentRec")
            self.scrollbary.config(command=self.listbox_at.yview)
            self.scrollbary.place(relx=0.98, rely=0, height=270)
            self.scrollbarx.config(command=self.listbox_at.xview)
            self.scrollbarx.place(relx=0, rely=0.87, width=1022)

            self.name_ent = Entry(self.manual_Frame, bd=2, font=("times new roman", 14), width=28)
            self.name_ent.place(relx=0.0, rely=0.25)
            self.date_entry = Entry(self.manual_Frame, bd=2, font=("times new roman", 14), width=15)
            self.date_entry.place(relx=0.45, rely=0.25)
            self.mark = ttk.Combobox(self.manual_Frame, value=("Present", "Absent"), font=("times new roman", 14),
                                     width=15)
            self.mark.place(relx=0.7, rely=0.25)

            # ===================================================Buttons========================================================
            self.get_member = Button(self.manual_Frame, text="Get Member", font=("times new roman", 14),
                                     command=view_content)
            self.get_member.place(relx=0.2, rely=0.3)

            self.submit_att = Button(self.manual_Frame, text="Submit Attendance", font=("times new roman", 14))
            self.submit_att.place(relx=0.4, rely=0.3)

            self.reset = Button(self.manual_Frame, text="Reset", font=("times new roman", 14))
            self.reset.place(relx=0.7, rely=0.3)

            self.attendance_tree = Frame(self.manual_Frame, width=550, height=200, relief=SUNKEN, bd=4)
            self.attendance_tree.place(relx=0.01, rely=0.36)

            self.tree = ttk.Treeview(self.attendance_tree, columns=(
                'S/N', "Member", "Date", "Attendance Status"),
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
            self.tree.heading('S/N', text="S/N", anchor=W)
            self.tree.heading('Member', text="Member", anchor=W)
            self.tree.heading('Date', text="Date", anchor=W)
            self.tree.heading('Attendance Status', text="Attendance Status", anchor=W)

            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=50)
            self.tree.column('#2', stretch=NO, minwidth=0, width=150)
            self.tree.column('#3', stretch=NO, minwidth=0, width=150)
            self.tree.column('#4', stretch=NO, minwidth=0, width=170)

            self.tree.place(relx=0.02, rely=0.0, width=1040, height=500)

            # ============================================Automated Attendance System==========================
            self.automated_Frame = Frame(self.main_con, width=480, height=600, relief=SUNKEN, bd=4)
            self.automated_Frame.place(relx=0.55, rely=0.0)

            self.ai_bg = Label(self.automated_Frame, bg="white")
            self.ai_bg_p = PhotoImage(file="graphics/ai11.png")
            self.ai_bg.config(image=self.ai_bg_p)
            self.ai_bg.place(relx=0, rely=0)
            self.head_label = Label(self.ai_bg, text="Face Recognition System", font=("times new roman", 23, "bold"),
                                    bg="#010912", fg="#f1f1f1")
            self.head_label.place(relx=0.12, rely=0.1)
            self.lbl = Button(self.ai_bg, text="Start Automatic Attendance System", font=("times new roman", 14),
                              bg="#010912", fg="#f1f1f1")
            self.lbl.place(relx=0.2, rely=0.8)
            view_content()

        # ===============================================AI System==============================================================================
            def Ai():
                self.window = Toplevel()
                self.window.geometry()
        attendance()


master = Tk()
obj = Attendance(master)
master.mainloop()