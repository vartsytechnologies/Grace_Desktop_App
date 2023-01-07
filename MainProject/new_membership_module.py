from tkinter import *
from tkinter import ttk
import random

class Add_Member():
    def __init__(self,master):
        self.master = master
        self.master.title("Grace Chapel")
        self.master.geometry("1400x750+0+0")
        self.master.resizable(0, 0)

        def add_mem():

            self.fm = Frame(self.master, height=720, width=1300)
            self.fm.place(relx=0, rely=0.09)
            self.frame1 = Frame(self.master, height=60, width=1400, bg="#9A0033")
            self.frame1.place(relx=0, rely=0)
            self.sublbl = Label(self.frame1, text="NEW MEMBERS ENTRY FORM", bg="#9A0033", fg="white",
                                font=("arial", 18, "bold"))
            self.sublbl.place(relx=0.3, rely=0.2)

            # ==============================functions===================================
            self.id = StringVar()
            self.name = StringVar()

            # =========================================frames ================================================
            self.con_frame_1 = LabelFrame(self.fm, text="PERSONAL DETAILS", width=1200, height=300, bg="white")
            self.con_frame_1.place(relx=0.03, rely=0.02)

            def gen_id():
                self.data_a_1.config(state='disabled', disabledbackground="#9A0033", disabledforeground="white")
                self.rand_id = random.randint(10000000, 20000000)
                self.conv_id = ('GCI/ZT/' + str(self.rand_id))
                self.id.set(self.conv_id)

            self.data_a = Label(self.con_frame_1, text="Member ID", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_a.place(relx=0.01, rely=0.01)
            self.data_a_1 = Entry(self.con_frame_1, width=30, bg="white", fg="blue", font=("times new roman", 14),
                                  textvariable=self.id)
            self.data_a_1.place(relx=0.2, rely=0.01)

            gen_id()

            self.data_b = Label(self.con_frame_1, text="Member Name", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_b.place(relx=0.01, rely=0.16)
            self.data_b_1 = Entry(self.con_frame_1, width=30, bg="white", fg="blue", font=("times new roman", 14),
                                  textvariable=self.name)
            self.data_b_1.place(relx=0.2, rely=0.16)

            self.data_c = Label(self.con_frame_1, text="Membership Type", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_c.place(relx=0.01, rely=0.31)
            self.data_c_1 = ttk.Combobox(self.con_frame_1, width=28, textvariable="self.type", value=(
            "Pastor", "Usher", "Deacon/Deaconess", "Departmental Head", "Instrumentalist", "Singer"),
                                         font=("times new roman", 14))
            self.data_c_1.place(relx=0.2, rely=0.31)

            self.data_d = Label(self.con_frame_1, text="Place Of Birth", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_d.place(relx=0.01, rely=0.46)
            self.data_d_1 = Entry(self.con_frame_1, width=30, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.place_of_birth")
            self.data_d_1.place(relx=0.2, rely=0.46)

            self.data_e = Label(self.con_frame_1, text="Date Of Birth", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_e.place(relx=0.01, rely=0.61)
            self.data_e_1 = Entry(self.con_frame_1, width=30, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.date_of_birth")
            self.data_e_1.place(relx=0.2, rely=0.61)

            self.data_f = Label(self.con_frame_1, text="Gender", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_f.place(relx=0.01, rely=0.76)
            self.data_f_1 = ttk.Combobox(self.con_frame_1, width=28, value=("Male", "Female", "Others"),
                                         font=("times new roman", 14), textvariable="self.gender")
            self.data_f_1.place(relx=0.2, rely=0.76)

            self.data_g = Label(self.con_frame_1, text="Department", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_g.place(relx=0.5, rely=0.01)
            self.data_g_1 = ttk.Combobox(self.con_frame_1, width=20, value=(
                "Church Board", "Men", "Youth", "Women", "Children", "Music", "Intercessors", "Evangelism", "Ushering"),
                                         font=("times new roman", 14), textvariable="self.department")
            self.data_g_1.place(relx=0.6, rely=0.01)

            self.data_i = Label(self.con_frame_1, text="Telephone", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_i.place(relx=0.5, rely=0.16)
            self.data_i_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.phone")
            self.data_i_1.place(relx=0.6, rely=0.16)

            self.data_j = Label(self.con_frame_1, text="Address", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_j.place(relx=0.5, rely=0.31)
            self.data_j_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.address")
            self.data_j_1.place(relx=0.6, rely=0.31)

            self.data_k = Label(self.con_frame_1, text="Email", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_k.place(relx=0.5, rely=0.46)
            self.data_k_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.email")
            self.data_k_1.place(relx=0.6, rely=0.46)

            self.data_l = Label(self.con_frame_1, text="Marital Status", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_l.place(relx=0.5, rely=0.61)
            self.data_l_1 = ttk.Combobox(self.con_frame_1, width=20, value=(
                "Married", "Single", "Separated", "Window/Widower", "Others"),
                                         font=("times new roman", 14), textvariable="self.status")
            self.data_l_1.place(relx=0.6, rely=0.61)

            self.data_m = Label(self.con_frame_1, text="Occupation", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_m.place(relx=0.5, rely=0.76)
            self.data_m_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.occupation")
            self.data_m_1.place(relx=0.6, rely=0.76)

            self.upload_btn = Button(self.con_frame_1, text="Upload Photo", font=("times new roman ", 14), width=18,
                                     bg="#9A0033", fg="white", command="take_photo")
            self.upload_btn.place(relx=0.79, rely=0.76)

            self.picture_frame = Frame(self.fm, width=200, height=200, bd=1, relief=SUNKEN)
            self.picture_frame.place(relx=0.18, rely=0.58)

            self.btn_img_id = Label(self.con_frame_1, bg="white")
            self.btn_img_8_A = PhotoImage(file="graphics/id_1.png")
            self.btn_img_id.config(image=self.btn_img_8_A)
            self.btn_img_id.place(relx=0.8, rely=0)

            self.con_frame_2 = LabelFrame(self.fm, width=1000, height=300, bg="white")
            self.con_frame_2.place(relx=0.03, rely=0.46)

            self.data_1 = Label(self.con_frame_2, text="Fax", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_1.place(relx=0.01, rely=0.01)
            self.data_1_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.fax")
            self.data_1_1.place(relx=0.2, rely=0.01)

            self.data_2 = Label(self.con_frame_2, text="Employer", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_2.place(relx=0.01, rely=0.16)
            self.data_2_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.emloyer")
            self.data_2_1.place(relx=0.2, rely=0.16)

            self.data_1 = Label(self.con_frame_2, text="Hometown", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_1.place(relx=0.01, rely=0.31)
            self.data_1_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.hometown")
            self.data_1_1.place(relx=0.2, rely=0.31)

            self.data_l = Label(self.con_frame_2, text="Region", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_l.place(relx=0.01, rely=0.46)
            self.data_l_1 = ttk.Combobox(self.con_frame_2, width=23, value=(
                "Greater Accra", "Oti", "Bono East", "Central", "Eastern", "Upper East", "Upper West", "Savana",
                "Volta", "North East", "Bono", "Ahafo", "Western North", "Northern", "Ashanti", "Westerm"),
                                         font=("times new roman", 14), textvariable="self.region")
            self.data_l_1.place(relx=0.2, rely=0.46)

            self.data_l = Label(self.con_frame_2, text="Tither", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_l.place(relx=0.01, rely=0.61)
            self.data_l_1 = ttk.Combobox(self.con_frame_2, width=23, value=(
                "Yes", "No",),
                                         font=("times new roman", 14), textvariable="self.Tithe")
            self.data_l_1.place(relx=0.2, rely=0.61)

            self.data_1 = Label(self.con_frame_2, text="Heath Status", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_1.place(relx=0.01, rely=0.76)
            self.data_1_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.health")
            self.data_1_1.place(relx=0.2, rely=0.76)

            self.data_g = Label(self.con_frame_2, text="Department", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_g.place(relx=0.5, rely=0.01)
            self.data_g_1 = ttk.Combobox(self.con_frame_2, width=28, value=(
                "Church Board", "Men", "Youth", "Women", "Children", "Music", "Intercessors", "Evangelism", "Ushering"),
                                         font=("times new roman", 14), textvariable="self.how")
            self.data_g_1.place(relx=0.65, rely=0.01)

            self.data_i = Label(self.con_frame_2, text="Company Name", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_i.place(relx=0.5, rely=0.16)
            self.data_i_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.company")
            self.data_i_1.place(relx=0.65, rely=0.16)

            self.data_j = Label(self.con_frame_2, text="Post Address", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_j.place(relx=0.5, rely=0.31)
            self.data_j_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.pst_address")
            self.data_j_1.place(relx=0.65, rely=0.31)

            self.data_k = Label(self.con_frame_2, text="Emerg. Contact", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_k.place(relx=0.5, rely=0.46)
            self.data_k_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.contact")
            self.data_k_1.place(relx=0.65, rely=0.46)

            self.data_l = Label(self.con_frame_2, text="Edu. Level", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_l.place(relx=0.5, rely=0.61)
            self.data_l_1 = ttk.Combobox(self.con_frame_2, width=28, value=(
                "University", "SHS", "JHS", "Training college", "N/A"),
                                         font=("times new roman", 14), textvariable="self.level")
            self.data_l_1.place(relx=0.65, rely=0.61)

            self.data_m = Label(self.con_frame_2, text="Year", font=("times new roman", 15), bg="white",
                                fg="black")
            self.data_m.place(relx=0.5, rely=0.76)
            self.data_m_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),
                                  textvariable="self.edu_instution")
            self.data_m_1.place(relx=0.65, rely=0.76)

            # ==================================================commands register buttons ==================================

            self.btn_frame = LabelFrame(self.fm, width=200, height=300, bg="white")
            self.btn_frame.place(relx=0.8, rely=0.46)

            self.upload_btn = Button(self.btn_frame, text="SUBMIT", font=("times new roman ", 14), width=14,
                                     command="Submit", bg="#9A0033", fg="white")
            self.upload_btn.place(relx=0.05, rely=0.01)

            self.upload_btn = Button(self.btn_frame, text="RESET", font=("times new roman ", 14), width=14,
                                     command="Reset", bg="#9A0033", fg="white")
            self.upload_btn.place(relx=0.05, rely=0.21)

            self.upload_btn = Button(self.btn_frame, text="EXIT", font=("times new roman ", 14), width=14,
                                     command="self.add_mem.destroy", bg="#9A0033", fg="white")
            self.upload_btn.place(relx=0.05, rely=0.41)
            self.upload_btn = Button(self.btn_frame, text="UPDATE", font=("times new roman ", 14), width=14,
                                     bg="#9A0033", fg="white")
            self.upload_btn.place(relx=0.05, rely=0.61)

        add_mem()

master = Tk()
obj = Add_Member(master)
master.mainloop()