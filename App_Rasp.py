from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sqlite3
from tkinter import font
from PIL import Image, ImageTk
from requests import Session
import zeep
from zeep import Client
from zeep.transports import Transport
import urllib3
import datetime
import time
import threading
import os, sys, subprocess
import tempfile





class Invoice(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[PageOne].setStartPageRef(self.frames[StartPage])
        self.frames[PageTwo].setStartPageRef2(self.frames[StartPage])
        self.frames[PageThree].setStartPageRef3(self.frames[StartPage])
        self.frames[StartPage].setStartPageRef4(self.frames[PageFour])
        self.frames[PageOne].setStartPageRef5(self.frames[PageThree])
        self.frames[PageThree].setStartPageRef6(self.frames[PageFour])
        self.frames[StartPage].setStartPageRef7(self.frames[PageFive])

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):  # Calculate Price

    db_name = 'MyDatabase.db'

    def setStartPageRef4(self, startPageRef):
        self.startPageRef = startPageRef

    def setStartPageRef7(self, startPageRef):
        self.startPageRef2 = startPageRef

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        AFont = font.Font(family='Calibri', size=12, weight='bold')
        BFont = font.Font(family='Calibri', size=11, )
        self.on_color = 'red'
        self.off_color = 'black'

        frame = ttk.LabelFrame(self, text='สินค้า',)
        frame.grid(row=1, column=0, sticky=W)
        frame7 = ttk.LabelFrame(self, text='พนักงาน')
        frame7.place(x = 550 , y = 51)
        frame8 = ttk.LabelFrame(self, text='ชุดคำสั่ง')
        frame8.grid(row=0, column=0, sticky=NW)
        frame9 = ttk.LabelFrame(self, text="คำนวณเงิน")
        frame9.grid(row = 2 ,sticky = E)
        frame10 = ttk.LabelFrame(self, text="ผู้ซื้อ")
        frame10.grid(row=3, column=0, sticky=W)
        frame11 = ttk.LabelFrame(self, text="รหัสประจำตัวผู้เสียภาษีล่าสุด")
        frame11.place(x= 600, y =340)
        frame12 = ttk.LabelFrame(self, text="ค้นหา")
        frame12.grid(row=2, sticky=SW)
        frame14 = ttk.LabelFrame(self, text = "ทะเบียนรถ")
        frame14.grid(row = 2 , columnspan = 2,sticky = S)




        self.chk1 = BooleanVar()
        self.chk2 = BooleanVar()
        self.chk3 = BooleanVar()
        self.chk4 = BooleanVar()
        self.chk5 = BooleanVar()
        self.chk6 = BooleanVar()

        self.image1 = Image.open("Gasohol95.jpg")
        self.image1 = self.image1.resize((150, 40), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.G95_button = tk.Button(frame, image=self.photo1, height=40, width=150, command=self.checkG95)
        self.G95_button.grid(row=0)
        self.Product1 = Checkbutton(frame, text="Supreme Gasohol 95", font=AFont, variable=self.chk1, fg=self.off_color,)
        self.Product1.grid(row=1, column=0)
        Label(frame, text = "ราคาต่อหน่วย:", font=BFont).grid(row=2, sticky = W)
        self.G95_price = Entry(frame, width=6, justify='right')
        self.G95_price.grid(row=2, column=0, sticky = E)

        self.image2 = Image.open("Gasohol95_Plus.jpg")
        self.image2 = self.image2.resize((150, 40), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.GP95_button = tk.Button(frame, image=self.photo2, height=40, width=150, command=self.checkGP95)
        self.GP95_button.grid(row=0, column=1)
        self.Product2 = Checkbutton(frame, text="Supreme Plus Gasohol 95", font=AFont, variable=self.chk2,
                                    fg=self.off_color)
        self.Product2.grid(row=1, column=1)
        Label(frame, text="ราคาต่อหน่วย:", font=BFont).grid(row=2,column = 1, sticky=W)
        self.GP95_price = Entry(frame, width=6, justify='right')
        self.GP95_price.grid(row=2, column=1, sticky=E)

        self.image3 = Image.open("Gasohol_E20.jpg")
        self.image3 = self.image3.resize((150, 40), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.E20_button = tk.Button(frame, image=self.photo3, height=40, width=150, command=self.checkE20)
        self.E20_button.grid(row=0, column=2)
        self.Product3 = Checkbutton(frame, text="Supreme E20               ", font=AFont, variable=self.chk3, fg=self.off_color)
        self.Product3.grid(row=1, column=2)
        Label(frame, text="ราคาต่อหน่วย:", font=BFont).grid(row=2, column=2, sticky=W)
        self.E20_price = Entry(frame, width=6, justify='right')
        self.E20_price.grid(row=2, column=2, sticky=E)


        self.image4 = Image.open("Gasohol_91.jpg")
        self.image4 = self.image4.resize((150, 40), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.G91_button = tk.Button(frame, image=self.photo4, height=40, width=150, command=self.checkG91)
        self.G91_button.grid(row=3, column=0)
        self.Product4 = Checkbutton(frame, text="Supreme Gasohol 91", font=AFont, variable=self.chk4, fg=self.off_color)
        self.Product4.grid(row=4, column=0)
        Label(frame, text="ราคาต่อหน่วย:", font=BFont).grid(row=5, column=0, sticky=W)
        self.G91_price = Entry(frame, width=6, justify='right')
        self.G91_price.grid(row=5, column=0, sticky=E)


        self.image5 = Image.open("Diesel_Plus.jpg")
        self.image5 = self.image5.resize((150, 40), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.DSP_button = tk.Button(frame, image=self.photo5, height=40, width=150, command=self.checkDSP)
        self.DSP_button.grid(row=3, column=1)
        self.Product5 = Checkbutton(frame, text="Supreme Plus Diesel", font=AFont, variable=self.chk5,
                                    fg=self.off_color)
        self.Product5.grid(row=4, column=1)
        Label(frame, text="ราคาต่อหน่วย:", font=BFont).grid(row=5, column=1, sticky=W)
        self.DSP_price = Entry(frame, width=6, justify='right')
        self.DSP_price.grid(row=5, column=1, sticky=E)

        self.image6 = Image.open("Diesel.jpg")
        self.image6 = self.image6.resize((150, 40), Image.ANTIALIAS)
        self.photo6 = ImageTk.PhotoImage(self.image6)
        self.DS_button = tk.Button(frame, image=self.photo6, height=40, width=150, command=self.checkDS)
        self.DS_button.grid(row=3, column=2)
        self.Product6 = Checkbutton(frame, text="Supreme Diesel", font=AFont, variable=self.chk6, fg=self.off_color)
        self.Product6.grid(row=4, column=2)
        Label(frame, text="ราคาต่อหน่วย:", font=BFont).grid(row=5, column=2, sticky=W)
        self.DS_price = Entry(frame, width=6, justify='right')
        self.DS_price.grid(row=5, column=2, sticky=E)


        Label(frame9, text='จำนวนลิตร', font=BFont).grid(row=0, column=0)
        Label(frame9, text='ลิตร', font=BFont).grid(row=0, column=2)
        self.product_liter = Entry(frame9, justify='right',width = 15)
        self.product_liter.bind("<KeyRelease>", self.livePriceCal)
        self.product_liter.grid(row=0, column=1)
        Label(frame9, text='ยอดทั้งหมด', font=BFont).grid(row=1, column=0)
        Label(frame9, text='บาท', font=BFont).grid(row=1, column=2)
        self.total_price = Entry(frame9, justify='right', width = 15)
        self.total_price.bind("<KeyRelease>", self.liveLiterCal)
        self.total_price.grid(row=1, column=1)
        self.print = tk.Button(self , text = "พิมพ์",font=('Calibri', '20'),width = 5, command =self.print_confirmation)
        self.print.place(x = 590 , y = 230)


        Label(frame7, text = "รหัสพนักงาน").grid(row=0)
        self.staff_id = Entry(frame7, justify = 'right', width = 14)
        self.staff_id.bind('<KP_Enter>', self.staff_login)
        self.staff_id.grid(row = 0 , column = 1)
        self.staff_id.bind('<Return>', self.staff_login)
        Label(frame7, text = "-----------------------").grid(row = 1, columnspan = 2)
        Label(frame7, text = "ชื่อพนักงาน").grid(row = 2, columnspan = 2)
        self.staff_name = Entry(frame7 , width = 21, justify = 'center')
        self.staff_name.grid(row = 3, columnspan = 2)
        Label(frame7, text = "เวลาเข้ากะ").grid(row = 4, columnspan = 2)
        self.shift_time = Entry(frame7, justify = 'center')
        self.shift_time.grid(row = 5, columnspan = 2)
        logout_button = Button(frame7, text = "ออกกะ", width = 10, command = self.log_out_confirmation)
        logout_button.grid(row = 6, columnspan = 2)


        Label(frame12, text="ชื่อบริษัท", font=BFont).grid(row=1, column=0, sticky=E)
        self.search_comp_name = Entry(frame12, justify='right', width=18)
        self.search_comp_name.bind('<KP_Enter>', self.searchCompName)
        self.search_comp_name.grid(row=1, column=1, sticky=W)
        self.search_comp_name.bind('<Return>', self.searchCompName)
        Label(frame12, text= "รหัสภาษี", font = BFont).grid(row = 2 , column = 0 , sticky = E)
        self.search_tax_id = Entry(frame12, justify = 'right', width = 18)
        self.search_tax_id.bind('<KP_Enter>', self.searchTaxId)
        self.search_tax_id.grid(row = 2, column = 1, sticky = W)
        self.search_tax_id.bind('<Return>', self.searchTaxId)

        Label(frame14, text = "ทะเบียนรถ", font = BFont).grid(row=0, sticky = E)
        self.car_plate = Entry(frame14, justify = 'right', width = 10)
        self.car_plate.grid(row = 0, column = 1)

        Label(frame10, text="ชื่อบริษัท",font=('Times New Roman', 10)).grid(row=1, column=0, sticky=E)
        self.comp_name = Entry(frame10, justify='right', width=14)
        self.comp_name.grid(row=1, column=1, sticky=W)
        Label(frame10, text="สาขา").grid(row=1, column=2, sticky=E)
        self.branch_num = Entry(frame10, justify='right', width=8)
        self.branch_num.grid(row=1, column=3, sticky=W)
        Label(frame10, text="ชื่อตึก").grid(row=1, column=4, sticky=E)
        self.building_name = Entry(frame10, justify='right', width=14)
        self.building_name.grid(row=1, column=5, sticky=W)
        Label(frame10, text="ชั้น").grid(row=1, column=6, sticky=E)
        self.branch_floor = Entry(frame10, justify='right', width=8)
        self.branch_floor.grid(row=1, column=7, sticky=W)
        Label(frame10, text="หมู่บ้าน").grid(row=2, column=0, sticky=E)
        self.village_name = Entry(frame10, justify='right', width=14)
        self.village_name.grid(row=2, column=1, sticky=W)
        Label(frame10, text="เลขห้อง").grid(row=2, column=2, sticky=E)
        self.room_no = Entry(frame10, justify='right', width=9)
        self.room_no.grid(row=2, column=3, sticky=W)
        Label(frame10, text="เลขที่บ้าน").grid(row=2, column=4, sticky=E)
        self.house_no = Entry(frame10, justify='right', width=14)
        self.house_no.grid(row=2, column=5, sticky=W)
        Label(frame10, text="หมู่").grid(row=2, column=6, sticky=E)
        self.Moo_no = Entry(frame10, justify='right', width=8)
        self.Moo_no.grid(row=2, column=7, sticky=W)
        Label(frame10, text="ซอย").grid(row=3, column=0, sticky=E)
        self.Soi_no = Entry(frame10, justify='right', width=14)
        self.Soi_no.grid(row=3, column=1, sticky=W)
        Label(frame10, text="ถนน").grid(row=3, column=2, sticky=E)
        self.Stree_name = Entry(frame10, justify='right', width=9)
        self.Stree_name.grid(row=3, column=3, sticky=W)
        Label(frame10, text="ตำบล").grid(row=3, column=4, sticky=E)
        self.Thumbon_name = Entry(frame10, justify='right', width=14)
        self.Thumbon_name.grid(row=3, column=5, sticky=W)
        Label(frame10, text="อำเภอ").grid(row=3, column=6, sticky=E)
        self.Aumper_name = Entry(frame10, justify='right', width=8)
        self.Aumper_name.grid(row=3, column=7, sticky=W)
        Label(frame10, text="จังหวัด").grid(row=4, column=0, sticky=E)
        self.Province_name = Entry(frame10, justify='right', width=14)
        self.Province_name.grid(row=4, column=1, sticky=W)
        Label(frame10, text="รหัสไปษณีย์").grid(row=4, column=2, sticky=E)
        self.Postcode = Entry(frame10, justify='right', width=9)
        self.Postcode.grid(row=4, column=3, sticky=W)
        Label(frame10, text = "เลขประจำผู้เสียภาษีผู้ซื้อ").place(x = 310 , y= 61)
        self.Cus_tax_num = Entry(frame10, justify = 'right', width = 15)
        self.Cus_tax_num.place(x= 440, y = 60)



        self.cus_list = Listbox(frame11, height=5 , width = 16, selectmode=SINGLE)
        self.cus_list.bind('<Double-Button-1>', self.show_data)
        vsb = ttk.Scrollbar(frame11, orient="vertical", command = self.cus_list.yview)
        vsb.grid(row = 1 ,column = 1 , sticky = 'ns')
        self.cus_list.grid(row=1)
        self.cus_list.config(yscrollcommand = vsb.set)
        self.show_tax_data = tk.Button(self, text = "ดูข้อมูลอีกครั้ง", command = self.show_tax_list)
        self.show_tax_data.place(x = 610 , y= 440)

        button3 = ttk.Button(frame8, text="ขายสินค้ารายการเดียว", command=lambda: controller.show_frame(StartPage),
                             width=14)
        button3.grid(row=0, column=0, )
        button3 = ttk.Button(frame8, text="ขายสินค้าหลายรายการ", command=lambda: controller.show_frame(PageThree),
                             width=14)
        button3.grid(row=0, column=1, )
        button3 = ttk.Button(frame8, text="ข้อมูลสินค้า", command=lambda: controller.show_frame(PageOne),
                             width=11)
        button3.grid(row=0, column=2, )
        button3 = ttk.Button(frame8, text="ข้อมูลลูกค้า", command=lambda: controller.show_frame(PageTwo),
                             width=11)
        button3.grid(row=0, column=3, )
        button6 = ttk.Button(frame8, text="ประวัติ", command=lambda: controller.show_frame(PageFour),
                             width=11)
        button6.grid(row=0, column=4)
        button6 = ttk.Button(frame8, text="พนักงาน", command=lambda: controller.show_frame(PageFive),
                             width=11)
        button6.grid(row=0, column=5)

        self.show_tax_list()
        self.update_lastest_record()
        self.record_number = 1
        self.Show_gas_price()
        self.G95_price.config(state='readonly')
        self.GP95_price.config(state='readonly')
        self.E20_price.config(state='readonly')
        self.G91_price.config(state='readonly')
        self.E20_price.config(state='readonly')
        self.DS_price.config(state='readonly')
        self.DSP_price.config(state='readonly')
        self.staff_name.config(state='readonly')
        self.shift_time.config(state='readonly')
        self.staff_id.config(state = 'normal')

    def update_lastest_record(self):
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute(' SELECT Record_ID FROM Record ORDER BY Record_ID DESC LIMIT 1')
        self.lastest_record = str(cur.fetchone()).replace('INV-','').replace('(', '').replace(')', '').replace("'", '').replace(",", '')
        self.lastest_record_number = int(self.lastest_record)

    def print_receipt(self):
        now = datetime.datetime.now()
        try:
            record_id = "INV-{0:07}".format(self.lastest_record_number + 1)
            record_total_price = self.total_price.get()
            recrod_car_plate = self.car_plate.get()
            record_staff_name = self.staff_name.get()
            record_date = now.strftime("%d" + "/" + "%m" + "/" + "%Y")
            record_comp_name = self.comp_name.get()
            Record_list = [record_date,
                           record_id,
                           record_comp_name,
                           record_total_price,
                           record_staff_name,
                           recrod_car_plate]

            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute(
                ' INSERT INTO Record(Record_Date, Record_ID, Company_Name, Total_Price,Staff_Name, Car_Plate) VALUES(?,?,?,?,?,?)',
                Record_list)
            con.commit()
            self.startPageRef.viewing_record()
            if self.chk1.get() == True:
                record_product_name = "Supreme Gasohol 95"
                record_litter = self.product_liter.get()
                cur2 = con.cursor()
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, record_product_name, record_litter))
                con.commit()
            if self.chk2.get() == True:
                record_product_name = "Supreme Plus Gasohol 95"
                record_litter = self.product_liter.get()
                cur2 = con.cursor()
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, record_product_name, record_litter))
                con.commit()
            if self.chk3.get() == True:
                record_product_name = "Supreme E20"
                record_litter = self.product_liter.get()
                cur2 = con.cursor()
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, record_product_name, record_litter))
                con.commit()
            if self.chk4.get() == True:
                record_product_name = "Supreme Gasohol 91"
                record_litter = self.product_liter.get()
                cur2 = con.cursor()
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, record_product_name, record_litter))
                con.commit()
            if self.chk5.get() == True:
                record_product_name = "Supreme Plus Diesel"
                record_litter = self.product_liter.get()
                cur2 = con.cursor()
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, record_product_name, record_litter))
                con.commit()
            if self.chk6.get() == True:
                record_product_name = "Supreme Diesel"
                record_litter = self.product_liter.get()
                cur2 = con.cursor()
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, record_product_name, record_litter))
                con.commit()

        except:
            messagebox.showerror("เกิดข้อผิดพลาด","ข้อมูลไม่ถูกต้อง")
            self.confirmation.destroy()
        else:
            record_id = "INV-{0:07}".format(self.lastest_record_number + 1)
            tax_id = '0203556007965'
            tempfiles = tempfile.mktemp(".text")
            receipt = open(tempfiles, "wt", encoding="utf-8")
            receipt.write("\t       ใบเสร็จรับเงิน/ใบกำกับภาษี(ต้นฉบับ)\n")
            receipt.write(
                "หจก.เดอะวันปิโตเลียม\n9/7 หมู่ 3 ถ.สุขุมวิท ต.ห้วยกะปิ\nอ.เมืองชลบุรี จ.ชลบุรี 20000\nTel. 086-4069062 FAX: 02-9030080 ต่อ 7811\n")
            receipt.write("Tax ID:" + tax_id + '\n')
            receipt.write("สาขาที่ออกใบกำกับภาษี: สำนักงานใหญ่\n")
            receipt.write("เลขที่: " + record_id + "\n")
            receipt.write("วันที่: " + now.strftime("%d" + "/" + "%m" + "/" + "%Y") + " " + now.strftime(
                "%H" + ":" + "%M") + "\n")
            receipt.write("ชื่อ: " + self.comp_name.get() + "\n")
            receipt.write("ที่อยู่: " + self.house_no.get() + " ")
            if self.Moo_no.get() is not '-':
                receipt.write("หมู่ " + self.Moo_no.get() + " ")
            if self.Soi_no.get() is not '-':
                receipt.write("ซ." + self.Soi_no.get() + " ")
            if self.Stree_name.get() is not '-':
                receipt.write("ถ." + self.Stree_name.get() + " ")
            if self.Thumbon_name.get() is not '-':
                receipt.write("ต." + self.Thumbon_name.get() + " ")
            receipt.write("\n")
            if self.Aumper_name.get() is not '-':
                receipt.write("        อ." + self.Aumper_name.get() + " ")
            if self.Province_name.get() is not '-':
                receipt.write("จ." + self.Province_name.get() + " ")
            if self.Postcode.get() is not '-':
                receipt.write(" " + self.Postcode.get() + " ")
            receipt.write("\n")
            receipt.write("เลขประจำผู้เสียภาษีผู้ซื้อ: " + self.Cus_tax_num.get() + "\n")
            receipt.write("ทะเบียนรถ: " + self.car_plate.get())
            receipt.write("\n")
            receipt.write("รายการ\t\t\tราคา    ปริมาณ\t  จำนวนเงิน\n")
            receipt.write("========================================\n")
            if self.chk1.get() == True:
                receipt.write("Supreme\nGasohol 95")
                receipt.write("\t\t" + self.G95_price.get())
                receipt.write("\t\t" + self.product_liter.get())
                receipt.write("\t\t" + self.total_price.get())
            if self.chk2.get() == True:
                receipt.write("Supreme Plus\nGasohol 95")
                receipt.write("\t\t" + self.GP95_price.get())
                receipt.write("\t\t" + self.product_liter.get())
                receipt.write("\t\t" + self.total_price.get())
            if self.chk3.get() == True:
                receipt.write("Supreme E20")
                receipt.write("\t" + self.E20_price.get())
                receipt.write("\t\t" + self.product_liter.get())
                receipt.write("\t\t" + self.total_price.get())
            if self.chk4.get() == True:
                receipt.write("Supreme\nGasohol 91")
                receipt.write("\t\t" + self.G91_price.get())
                receipt.write("\t\t" + self.product_liter.get())
                receipt.write("\t\t" + self.total_price.get())
            if self.chk5.get() == True:
                receipt.write("Supreme Plus\nDiesel")
                receipt.write("\t\t\t" + self.DSP_price.get())
                receipt.write("\t\t" + self.product_liter.get())
                receipt.write("\t\t" + self.total_price.get())
            if self.chk6.get() == True:
                receipt.write("Supreme Diesel")
                receipt.write("\t" + self.DS_price.get())
                receipt.write("\t\t" + self.product_liter.get())
                receipt.write("\t\t" + self.total_price.get())
            receipt.write("\n\n")
            receipt.write("มูลค่าสินค้า:")
            receipt.write("\t\t\t\t\t\t" + self.total_price.get() + "\n")
            receipt.write("ภาษีมูลค่าเพิ่ม(VAT 7%)")
            vat = float(self.total_price.get()) / 107
            receipt.write("\t\t\t" + str(round(vat, 2)) + "\n")
            total = float(self.total_price.get()) - vat
            receipt.write("รวมเป็นเงิน:")
            receipt.write("\t\t\t\t\t\t" + str(round(total, 0)))
            receipt.write("\n\n\nได้รับสินค้าตามรายการบนนี้ไว้ถูกต้อง\nและในสภาพเรียบร้อยทุกประการ")
            receipt.write("\n\n\nลงชื่อผู้รับเงิน _________________________________")
            receipt.write("\n\n\t         *****ขอบคุณที่ใช้บริการ*****")
            self.update_lastest_record()
            self.comp_name.delete(0, 'end')
            self.branch_num.delete(0, 'end')
            self.branch_floor.delete(0, 'end')
            self.building_name.delete(0, 'end')
            self.village_name.delete(0, 'end')
            self.house_no.delete(0, 'end')
            self.Moo_no.delete(0, 'end')
            self.Soi_no.delete(0, 'end')
            self.Stree_name.delete(0, 'end')
            self.Thumbon_name.delete(0, 'end')
            self.Aumper_name.delete(0, 'end')
            self.Province_name.delete(0, 'end')
            self.Postcode.delete(0, 'end')
            self.Cus_tax_num.delete(0, 'end')
            self.total_price.delete(0,'end')
            self.product_liter.delete(0,'end')
            self.car_plate.delete(0,'end')
            self.chk1.set(False)
            self.chk2.set(False)
            self.chk3.set(False)
            self.chk4.set(False)
            self.chk5.set(False)
            self.chk6.set(False)
            self.Product1["fg"] = self.off_color
            self.Product2["fg"] = self.off_color
            self.Product3["fg"] = self.off_color
            self.Product4["fg"] = self.off_color
            self.Product5["fg"] = self.off_color
            self.Product6["fg"] = self.off_color

            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, tempfiles])
            self.confirmation.destroy()



    def print_confirmation(self):



        self.confirmation = Toplevel()
        self.confirmation.title("ยืนยันหรือไม่")
        self.confirmation.geometry("%dx%d+%d+%d" % (270, 90, 300, 250))
        Label(self.confirmation, text = "ยืนยันการสั่งพิมพ์หรือไม่?", font=("Helvetica", 20)).grid(row=0,columnspan = 2)
        self.confirm_button = Button(self.confirmation, text = "ยืนยัน", font=("Helvetica", 14), width = 5, command = self.print_receipt)
        self.confirm_button.grid(row=1)
        self.cancel_button = Button(self.confirmation, text = "ยกเลิก", font=("Helvetica", 14), width = 5 , command = self.confirmation.destroy)
        self.cancel_button.grid(row=1, column = 1)
        self.confirmation.focus_set()
        self.confirmation.grab_set()
        self.confirmation.mainloop()

    def staff_login(self,event):
        now = datetime.datetime.now()
        try:
            self.staff_name.config(state = 'normal')
            self.shift_time.config(state=  'normal')
            self.staff_name.delete(0,END)
            self.shift_time.delete(0,END)

            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute('SELECT Staff_Name FROM Staff WHERE Staff_ID = ?', self.staff_id.get())
            self.staff_name.insert(END, str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))
            self.shift_time.insert(END, now.strftime("%H" + ":" + "%M"))
            self.staff_id.config(state = 'readonly')
            self.staff_name.config(state='readonly')
            self.shift_time.config(state='readonly')
        except:
            messagebox.showwarning("เกิดข้อผิดพลาด","ไม่พบข้อมูลพนักงาน กรุณาใส่เลขใหม่")
            self.staff_name.config(state='readonly')
            self.shift_time.config(state='readonly')


    def log_out_confirmation(self):
        self.confirmation = Toplevel()
        self.confirmation.title("ยืนยันหรือไม่")
        self.confirmation.geometry("%dx%d+%d+%d" % (270, 90, 300, 250))
        Label(self.confirmation, text = "ยืนยันการออกกะหรือไม่??", font=("Helvetica", 20)).grid(row=0,columnspan = 2)
        self.confirm_button = Button(self.confirmation, text = "ยืนยัน", font=("Helvetica", 14), width = 5, command = self.staff_shift_record)
        self.confirm_button.grid(row=1)
        self.cancel_button = Button(self.confirmation, text = "ยกเลิก", font=("Helvetica", 14), width = 5 , command = self.confirmation.destroy)
        self.cancel_button.grid(row=1, column = 1)
        self.confirmation.focus_set()
        self.confirmation.grab_set()
        self.confirmation.mainloop()

    def staff_shift_record(self):
        try:
            now = datetime.datetime.now()
            staff_id = self.staff_id.get()
            staff_name = self.staff_name.get()
            start_time = self.shift_time.get()
            end_time = now.strftime("%H" + ":" + "%M")
            record_date = now.strftime("%d" + "/" + "%m" + "/" + "%Y")
            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute('INSERT INTO Staff_Record(Staff_ID, Staff_Name,Date,Start_Time,End_Time) VALUES(?,?,?,?,?)' , (staff_id,staff_name,record_date,start_time,end_time))
            con.commit()
        except:
            messagebox.showerror("เกิดข้อผิดพลาด","ข้อมูลไม่ถูกต้อง")
        else:
            self.staff_name.config(state='normal')
            self.shift_time.config(state='normal')
            self.staff_id.config(state='normal')
            self.staff_name.delete(0, END)
            self.shift_time.delete(0, END)
            self.staff_id.delete(0, END)
            self.staff_name.config(state='readonly')
            self.shift_time.config(state='readonly')
            self.startPageRef2.show_staff_record()
            self.confirmation.destroy()

    def show_tax_list(self):

        self.cus_list.delete(0,END)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Tax_ID FROM Customer ORDER BY Tax_ID DESC LIMIT 5')
        for row in cur.fetchall():
            self.cus_list.insert(END, row)

    def searchCompName(self, event):
        try:
            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute('SELECT Name FROM Customer WHERE Name like ?', ('%' + self.search_comp_name.get() + '%',))
            self.tax_list = Toplevel()
            self.tax_list.title("Result")
            self.tax_list.geometry("500x200")
            Label(self.tax_list, text="รายชื่อบริษัท").grid(row=0)
            self.tax = Listbox(self.tax_list, height=10, width=40, selectmode=SINGLE)
            self.tax.bind("<Double-Button>", self.show_tax_id)
            self.tax.grid(row=1)
            for row in cur.fetchall():
                self.tax.insert(END, row)
            Label(self.tax_list, text="รหัสภาษี").grid(row=0, column=1)
            self.tax_id = Listbox(self.tax_list, height=10, width=40, selectmode=SINGLE)
            self.tax_id.bind('<Double-Button>', self.show_data2)
            self.tax_id.grid(row=1, column=1)

            self.tax_list.focus_set()
            self.tax_list.grab_set()
            self.tax_list.mainloop()
        except:
            messagebox.showwarning("เกิดข้อผิดพลาด", "ไม่พบข้อมูล")
            self.tax_list.destroy()


    def searchTaxId(self, event):
        try:
            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute("SELECT Name FROM Customer WHERE Tax_ID like ?", ('%' + self.search_tax_id.get() + '%',))
            self.tax_list = Toplevel()
            self.tax_list.title("Result")
            self.tax_list.geometry("500x200")
            Label(self.tax_list, text="รายชื่อบริษัท").grid(row=0)
            self.tax = Listbox(self.tax_list, height=10, width=40, selectmode=SINGLE)
            self.tax.bind("<Double-Button>", self.show_data3)
            self.tax.grid(row=1)
            for row in cur.fetchall():
                self.tax.insert(END, row)

            self.tax_list.focus_set()
            self.tax_list.grab_set()
            self.tax_list.mainloop()
        except:
            messagebox.showwarning("เกิดข้อผิดพลาด","ไม่พบข้อมูล")
            self.tax_list.destroy()


    def show_tax_id(self, event):

        self.tax_id.delete(0, 'end')
        self.get_tax_value = self.tax.get(self.tax.curselection())
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Tax_ID FROM Customer WHERE Name = ? ', (self.get_tax_value))
        for row in cur.fetchall():
            self.tax_id.insert(END, row)

    def livePriceCal(self, event):
        try:
            self.checkbox_controller = [str(self.chk1.get()),
                                          str(self.chk2.get()),
                                          str(self.chk3.get()),
                                          str(self.chk4.get()),
                                          str(self.chk5.get()),
                                          str(self.chk6.get()) ]
            self.count = self.checkbox_controller.count('True')


            if self.count >= 2:
                messagebox.showwarning("ข้อผิดพลาด","กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
                self.total_price.delete(0, 'end')
                self.product_liter.delete(0, 'end')

            if self.chk1.get() == True:
                self.total_price.delete(0, 'end')
                price = float(self.product_liter.get()) * float(self.G95_price.get())
                self.total_price.insert(END, round(price, 3))

            if self.chk2.get() == True:
                self.total_price.delete(0, 'end')
                price = float(self.product_liter.get()) * float(self.GP95_price.get())
                self.total_price.insert(END, round(price, 3))

            if self.chk3.get() == True:
                self.total_price.delete(0, 'end')
                price = float(self.product_liter.get()) * float(self.E20_price.get())
                self.total_price.insert(END, round(price, 3))

            if self.chk4.get() == True:
                self.total_price.delete(0, 'end')
                price = float(self.product_liter.get()) * float(self.G91_price.get())
                self.total_price.insert(END, round(price, 3))

            if self.chk5.get() == True:
                self.total_price.delete(0, 'end')
                price = float(self.product_liter.get()) * float(self.DSP_price.get())
                self.total_price.insert(END, round(price, 3))

            if self.chk6.get() == True:
                self.total_price.delete(0, 'end')
                price = float(self.product_liter.get()) * float(self.DS_price.get())
                self.total_price.insert(END, round(price, 3))
        except:
            messagebox.showerror("เกิดข้อผิดพลาด","กรุณาใส่ตัวเลขเท่านั้น")
            self.product_liter.delete(0,'end')
            self.product_liter.delete(0, 'end')

    def liveLiterCal(self, event):
        try:
            if self.chk1.get() == True:
                self.product_liter.delete(0, 'end')
                liter = float(self.total_price.get()) / float(self.G95_price.get())
                self.product_liter.insert(END, round(liter, 3))

            if self.chk2.get() == True:
                self.product_liter.delete(0, 'end')
                liter = float(self.total_price.get()) / float(self.GP95_price.get())
                self.product_liter.insert(END, round(liter, 3))
            if self.chk3.get() == True:
                self.product_liter.delete(0, 'end')
                liter = float(self.total_price.get()) / float(self.E20_price.get())
                self.product_liter.insert(END, round(liter, 3))
            if self.chk4.get() == True:
                self.product_liter.delete(0, 'end')
                liter = float(self.total_price.get()) / float(self.G91_price.get())
                self.product_liter.insert(END, round(liter, 3))
            if self.chk5.get() == True:
                self.product_liter.delete(0, 'end')
                liter = float(self.total_price.get()) / float(self.DSP_price.get())
                self.product_liter.insert(END, round(liter, 3))
            if self.chk6.get() == True:
                self.product_liter.delete(0, 'end')
                liter = float(self.total_price.get()) / float(self.DS_price.get())
                self.product_liter.insert(END, round(liter, 3))
        except:
            print("ERROR")


    def show_data(self, event):

        self.comp_name.delete(0, 'end')
        self.branch_num.delete(0, 'end')
        self.branch_floor.delete(0, 'end')
        self.building_name.delete(0, 'end')
        self.village_name.delete(0, 'end')
        self.house_no.delete(0, 'end')
        self.Moo_no.delete(0, 'end')
        self.Soi_no.delete(0, 'end')
        self.Stree_name.delete(0, 'end')
        self.Thumbon_name.delete(0, 'end')
        self.Aumper_name.delete(0, 'end')
        self.Province_name.delete(0, 'end')
        self.Postcode.delete(0, 'end')
        self.Cus_tax_num.delete(0, 'end')

        self.get_selecte_value = self.cus_list.get(self.cus_list.curselection())


        self.Cus_tax_num.insert(END, self.get_selecte_value)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Name FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.comp_name.insert(END,
                              str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur2 = con.cursor()
        cur2.execute('SELECT BranchNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.branch_num.insert(END, cur2.fetchone())

        cur3 = con.cursor()
        cur3.execute('SELECT BuildingName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.building_name.insert(END,
                                  str(cur3.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",",
                                                                                                                  ''))

        cur4 = con.cursor()
        cur4.execute('SELECT FloorNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.branch_floor.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT VillageName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.village_name.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT HouseNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.house_no.insert(END, cur6.fetchall())

        cur7 = con.cursor()
        cur7.execute('SELECT MooNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Moo_no.insert(END, cur7.fetchall())

        cur8 = con.cursor()
        cur8.execute('SELECT SoiName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Soi_no.insert(END,
                           str(cur8.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur9 = con.cursor()
        cur9.execute('SELECT StreetName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Stree_name.insert(END, cur9.fetchall())

        cur10 = con.cursor()
        cur10.execute('SELECT Thambol FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Thumbon_name.insert(END, cur10.fetchall())

        cur11 = con.cursor()
        cur11.execute('SELECT Amphur FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Aumper_name.insert(END, cur11.fetchall())

        cur12 = con.cursor()
        cur12.execute('SELECT Province FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Province_name.insert(END, cur12.fetchall())

        cur13 = con.cursor()
        cur13.execute('SELECT PostCode FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Postcode.insert(END, cur13.fetchall())

    def show_data2(self, event):

        self.comp_name.delete(0, 'end')
        self.branch_num.delete(0, 'end')
        self.branch_floor.delete(0, 'end')
        self.building_name.delete(0, 'end')
        self.village_name.delete(0, 'end')
        self.house_no.delete(0, 'end')
        self.Moo_no.delete(0, 'end')
        self.Soi_no.delete(0, 'end')
        self.Stree_name.delete(0, 'end')
        self.Thumbon_name.delete(0, 'end')
        self.Aumper_name.delete(0, 'end')
        self.Province_name.delete(0, 'end')
        self.Postcode.delete(0, 'end')
        self.Cus_tax_num.delete(0 , 'end')
        self.get_value = self.tax_id.get(self.tax_id.curselection())

        self.Cus_tax_num.insert(END, self.get_value)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Name FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.comp_name.insert(END,
                              str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur2 = con.cursor()
        cur2.execute('SELECT BranchNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.branch_num.insert(END, cur2.fetchone())

        cur3 = con.cursor()
        cur3.execute('SELECT BuildingName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.building_name.insert(END,
                                  str(cur3.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",",
                                                                                                                  ''))

        cur4 = con.cursor()
        cur4.execute('SELECT FloorNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.branch_floor.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT VillageName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.village_name.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT HouseNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.house_no.insert(END, cur6.fetchall())

        cur7 = con.cursor()
        cur7.execute('SELECT MooNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Moo_no.insert(END, cur7.fetchall())

        cur8 = con.cursor()
        cur8.execute('SELECT SoiName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Soi_no.insert(END,
                           str(cur8.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur9 = con.cursor()
        cur9.execute('SELECT StreetName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Stree_name.insert(END, cur9.fetchall())

        cur10 = con.cursor()
        cur10.execute('SELECT Thambol FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Thumbon_name.insert(END, cur10.fetchall())

        cur11 = con.cursor()
        cur11.execute('SELECT Amphur FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Aumper_name.insert(END, cur11.fetchall())

        cur12 = con.cursor()
        cur12.execute('SELECT Province FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Province_name.insert(END, cur12.fetchall())

        cur13 = con.cursor()
        cur13.execute('SELECT PostCode FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Postcode.insert(END, cur13.fetchall())

        self.tax_list.destroy()

    def show_data3(self, event):

        self.comp_name.delete(0, 'end')
        self.branch_num.delete(0, 'end')
        self.branch_floor.delete(0, 'end')
        self.building_name.delete(0, 'end')
        self.village_name.delete(0, 'end')
        self.house_no.delete(0, 'end')
        self.Moo_no.delete(0, 'end')
        self.Soi_no.delete(0, 'end')
        self.Stree_name.delete(0, 'end')
        self.Thumbon_name.delete(0, 'end')
        self.Aumper_name.delete(0, 'end')
        self.Province_name.delete(0, 'end')
        self.Postcode.delete(0, 'end')
        self.Cus_tax_num.delete(0, 'end')
        self.get_selecte_value = self.tax.get(self.tax.curselection())



        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Name FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.comp_name.insert(END,
                              str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur2 = con.cursor()
        cur2.execute('SELECT BranchNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.branch_num.insert(END, cur2.fetchone())

        cur3 = con.cursor()
        cur3.execute('SELECT BuildingName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.building_name.insert(END,
                                  str(cur3.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",",
                                                                                                                  ''))

        cur4 = con.cursor()
        cur4.execute('SELECT FloorNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.branch_floor.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT VillageName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.village_name.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT HouseNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.house_no.insert(END, cur6.fetchall())

        cur7 = con.cursor()
        cur7.execute('SELECT MooNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Moo_no.insert(END, cur7.fetchall())

        cur8 = con.cursor()
        cur8.execute('SELECT SoiName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Soi_no.insert(END,
                           str(cur8.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur9 = con.cursor()
        cur9.execute('SELECT StreetName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Stree_name.insert(END, cur9.fetchall())

        cur10 = con.cursor()
        cur10.execute('SELECT Thambol FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Thumbon_name.insert(END, cur10.fetchall())

        cur11 = con.cursor()
        cur11.execute('SELECT Amphur FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Aumper_name.insert(END, cur11.fetchall())

        cur12 = con.cursor()
        cur12.execute('SELECT Province FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Province_name.insert(END, cur12.fetchall())

        cur13 = con.cursor()
        cur13.execute('SELECT PostCode FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Postcode.insert(END, cur13.fetchall())

        cur14 = con.cursor()
        cur14.execute('SELECT Tax_ID FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Cus_tax_num.insert(END, cur14.fetchall())

        self.tax_list.destroy()
    def Show_gas_price(self):
        self.G95_price.config(state='normal')
        self.GP95_price.config(state='normal')
        self.E20_price.config(state='normal')
        self.G91_price.config(state='normal')
        self.E20_price.config(state='normal')
        self.DS_price.config(state='normal')
        self.DSP_price.config(state='normal')
        self.G95_price.delete(0, END)
        self.GP95_price.delete(0, END)
        self.E20_price.delete(0, END)
        self.G91_price.delete(0, END)
        self.DS_price.delete(0, END)
        self.DSP_price.delete(0, END)

        con = sqlite3.connect('MyDatabase.db')
        cur1 = con.cursor()
        cur1.execute('SELECT Product_Price FROM Product WHERE Product_ID = 1')
        self.G95_price.insert(END, cur1.fetchall())

        cur2 = con.cursor()
        cur2.execute('SELECT Product_Price FROM Product WHERE Product_ID = 26')
        self.GP95_price.insert(END, cur2.fetchall())

        cur3 = con.cursor()
        cur3.execute('SELECT Product_Price FROM Product WHERE Product_ID = 27')
        self.E20_price.insert(END, cur3.fetchall())

        cur4 = con.cursor()
        cur4.execute('SELECT Product_Price FROM Product WHERE Product_ID = 28')
        self.G91_price.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT Product_Price FROM Product WHERE Product_ID = 29')
        self.DS_price.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT Product_Price FROM Product WHERE Product_ID = 30')
        self.DSP_price.insert(END, cur6.fetchall())

        self.G95_price.config(state='readonly')
        self.GP95_price.config(state='readonly')
        self.E20_price.config(state='readonly')
        self.G91_price.config(state='readonly')
        self.E20_price.config(state='readonly')
        self.DS_price.config(state='readonly')
        self.DSP_price.config(state='readonly')

    def checkG95(self):

        if self.chk1.get() == False:
            self.chk1.set(True)
            self.Product1["fg"] = self.on_color
        else:
            self.chk1.set(False)
            self.Product1["fg"] = self.off_color

        self.checkbox_controller = [str(self.chk1.get()),
                                    str(self.chk2.get()),
                                    str(self.chk3.get()),
                                    str(self.chk4.get()),
                                    str(self.chk5.get()),
                                    str(self.chk6.get())]
        self.count = self.checkbox_controller.count('True')

        if self.count >= 2:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
            self.chk1.set(False)
            self.Product1["fg"] = self.off_color


    def checkGP95(self):

        if self.chk2.get() == False:
            self.chk2.set(True)
            self.Product2["fg"] = self.on_color
        else:
            self.chk2.set(False)
            self.Product2["fg"] = self.off_color

        self.checkbox_controller = [str(self.chk1.get()),
                                    str(self.chk2.get()),
                                    str(self.chk3.get()),
                                    str(self.chk4.get()),
                                    str(self.chk5.get()),
                                    str(self.chk6.get())]
        self.count = self.checkbox_controller.count('True')

        if self.count >= 2:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
            self.chk2.set(False)
            self.Product2["fg"] = self.off_color

    def checkE20(self):
        if self.chk3.get() == False:
            self.chk3.set(True)
            self.Product3["fg"] = self.on_color
        else:
            self.chk3.set(False)
            self.Product3["fg"] = self.off_color
        self.checkbox_controller = [str(self.chk1.get()),
                                    str(self.chk2.get()),
                                    str(self.chk3.get()),
                                    str(self.chk4.get()),
                                    str(self.chk5.get()),
                                    str(self.chk6.get())]
        self.count = self.checkbox_controller.count('True')

        if self.count >= 2:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
            self.chk3.set(False)
            self.Product3["fg"] = self.off_color

    def checkG91(self):
        if self.chk4.get() == False:
            self.chk4.set(True)
            self.Product4["fg"] = self.on_color
        else:
            self.chk4.set(False)
            self.Product4["fg"] = self.off_color

        self.checkbox_controller = [str(self.chk1.get()),
                                    str(self.chk2.get()),
                                    str(self.chk3.get()),
                                    str(self.chk4.get()),
                                    str(self.chk5.get()),
                                    str(self.chk6.get())]
        self.count = self.checkbox_controller.count('True')

        if self.count >= 2:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
            self.chk4.set(False)
            self.Product4["fg"] = self.off_color

    def checkDSP(self):
        if self.chk5.get() == False:
            self.chk5.set(True)
            self.Product5["fg"] = self.on_color
        else:
            self.chk5.set(False)
            self.Product5["fg"] = self.off_color

        self.checkbox_controller = [str(self.chk1.get()),
                                    str(self.chk2.get()),
                                    str(self.chk3.get()),
                                    str(self.chk4.get()),
                                    str(self.chk5.get()),
                                    str(self.chk6.get())]
        self.count = self.checkbox_controller.count('True')

        if self.count >= 2:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
            self.chk5.set(False)
            self.Product5["fg"] = self.off_color

    def checkDS(self):
        if self.chk6.get() == False:
            self.chk6.set(True)
            self.Product6["fg"] = self.on_color
        else:
            self.chk6.set(False)
            self.Product6["fg"] = self.off_color

        self.checkbox_controller = [str(self.chk1.get()),
                                    str(self.chk2.get()),
                                    str(self.chk3.get()),
                                    str(self.chk4.get()),
                                    str(self.chk5.get()),
                                    str(self.chk6.get())]
        self.count = self.checkbox_controller.count('True')

        if self.count >= 2:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกสินค้าเพียงชนิดเดียวเท่านั้น!")
            self.chk6.set(False)
            self.Product6["fg"] = self.off_color

    def list_customer(self):
        db = sqlite3.connect('MyDatabase.db')
        cursor = db.execute('SELECT Tax_ID FROM Customer ORDER BY Tax_ID ASC')

        for row in cursor.fetchall():
            self.cus_list.insert(END, row)


class PageOne(tk.Frame):  # Product Page

    db_name = 'MyDatabase.db'

    def setStartPageRef(self, startPageRef):
        self.startPageRef = startPageRef

    def setStartPageRef5(self, startPageRef):
        self.startPageRef5 = startPageRef


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = ttk.LabelFrame(self, text='เพิ่มสินค้า')
        frame.grid(row=1, column=0, sticky=NW)

        style = ttk.Style(self)
        style.configure("TButton", font=('wasy10', 12))

        Label(frame, text='ชื่อสินค้า').grid(row=1, column=0,sticky = E)
        self.name = Entry(frame, width = 13)
        self.name.grid(row=1, column=1)

        Label(frame, text='ประเภทสินค้า').grid(row=1, column=2,sticky = E)
        self.type = Entry(frame, justify='right', width = 13)
        self.type.grid(row=1, column=3)

        Label(frame, text='ราคา').grid(row=1, column=4,sticky = E)
        self.price = Entry(frame, justify='right', width = 13)
        self.price.grid(row=1, column=5)

        ttk.Button(frame, text='เพิ่มข้อมูล', command=self.adding).grid(row=1, column=6)
        button1 = ttk.Button(frame, text='ลบข้อมูล', command=self.deleting)
        button1.grid(row=1, column=7)

        frame3 = LabelFrame(self)
        frame3.grid(row = 2,sticky = W)

        self.tree = ttk.Treeview(frame3, height=17, column=("2", "3"))
        self.tree.grid(row=0, column=0)
        self.tree.heading('#0', text='ชื่อสินค้า', anchor=W)
        self.tree.heading(0, text='ประเภทสินค้า', anchor=W)
        self.tree.heading(1, text='ราคา', anchor=W)
        self.tree.column('#0', width = 300)
        self.tree.column('0', width = 90)
        self.tree.bind('<Double-Button>', self.editing)
        vsb = ttk.Scrollbar(frame3, orient='vertical', command=self.tree.yview)
        self.tree.grid(row=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=vsb.set)

        frame2 = LabelFrame(self, text='ชุดคำสั่ง')
        frame2.grid(row=0, column=0, sticky=W)


        button3 = ttk.Button(frame2, text="ขายสินค้ารายการเดียว", command=lambda: controller.show_frame(StartPage),
                             width=14)
        button3.grid(row=0, column=0, )
        button3 = ttk.Button(frame2, text="ขายสินค้าหลายรายการ", command=lambda: controller.show_frame(PageThree),
                             width=14)
        button3.grid(row=0, column=1, )
        button3 = ttk.Button(frame2, text="ข้อมูลสินค้า", command=lambda: controller.show_frame(PageOne),
                             width=11)
        button3.grid(row=0, column=2, )
        button3 = ttk.Button(frame2, text="ข้อมูลลูกค้า", command=lambda: controller.show_frame(PageTwo),
                             width=11)
        button3.grid(row=0, column=3, )
        button6 = ttk.Button(frame2, text="ประวัติ", command=lambda: controller.show_frame(PageFour),
                             width=11)
        button6.grid(row=0, column=4)
        button6 = ttk.Button(frame2, text="พนักงาน", command=lambda: controller.show_frame(PageFive),
                             width=11)
        button6.grid(row=0, column=5)

        self.viewing_record()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def viewing_record(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM Product ORDER BY Product_ID ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=(row[2], row[3]))

    def validation(self):
        return len(self.name.get()) != 0 and len(self.type.get()) != 0 and len(self.price.get()) != 0

    def adding(self):

        query = 'INSERT INTO Product VALUES (NULL, ?, ?,?)'
        parameters = (self.name.get(), self.type.get(), self.price.get())
        self.run_query(query, parameters)
        self.name.delete(0, END)
        self.type.delete(0, END)
        self.price.delete(0, END)
        self.viewing_record()
        self.startPageRef5.combo_product()


    def deleting(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            messagebox.showwarning("เกิดข้อผิดพลาด","กรุณาเลือกสินค้า")
            return

        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM Product WHERE Product_Name = ?'
        self.run_query(query, (name,))
        self.viewing_record()
        self.startPageRef5.combo_product()

    def editing(self,event):
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            messagebox.showwarning("เกิดข้อผิดพลาด", "กรุณาเลือกสินค้า")
            return

        name = self.tree.item( self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][1]

        self.edit_main = Toplevel()
        self.edit_main.title('แก้ไขข้อมูลสินค้า')
        self.edit_main.geometry('500x300')

        Label( self.edit_main,text = 'ชื่อสินค้าเก่า' ,font=("Helvetica", 16)).grid( row = 0,column = 1 )
        Pre_Name = Label( self.edit_main,textvariable = StringVar( self.edit_main,value = name ),font=("Helvetica", 16))
        Pre_Name.grid(row = 0,column = 2 )
        Label( self.edit_main,text = 'ชื่อสินค้าใหม่',font=("Helvetica", 16)).grid( row = 1,column = 1 )
        new_name = Text( self.edit_main, height =1,width = 30,font=("Helvetica", 15))
        new_name.grid( row = 1,column = 2 )
        new_name['wrap'] = 'none'
        new_name.insert(END,name)

        Label(self.edit_main, text='ราคาเก่า',font=("Helvetica", 16)).grid(row=2, column=1)
        Pre_Price = Label(self.edit_main, textvariable=StringVar(self.edit_main, value=old_price), font=("Helvetica", 16))
        Pre_Price.grid(row=2, column=2)
        Label(self.edit_main, text='ราคาใหม่',font=("Helvetica", 16)).grid(row=3, column=1)
        new_price = Text( self.edit_main, height =1,width = 30,font=("Helvetica", 15))
        new_price.grid(row=3, column=2)

        Button(self.edit_main, text='ตกลง',font=("Helvetica", 14),width = 8,height=1,
               command=lambda: self.edit_record(new_price.get(1.0,'end-1c'), new_name.get(1.0,'end-1c') ,old_price, name)).grid(row=4, column=2,)
        Button(self.edit_main, text ="ยกเลิก",font=("Helvetica", 14),width = 8,height=1,command = self.edit_main.destroy).grid(row=5,column =2)

        self.edit_main.focus_set()
        self.edit_main.grab_set()
        self.edit_main.mainloop()

    def edit_record(self, new_price,new_name, old_price, old_name):
        query = 'UPDATE Product SET Product_Price = ? , Product_Name = ? WHERE Product_Price = ? AND Product_Name = ?'
        paremeters = (new_price, new_name ,old_price,old_name)
        self.run_query(query, paremeters)
        self.edit_main.destroy()
        self.viewing_record()
        self.startPageRef.Show_gas_price()
        self.startPageRef5.combo_product()


class PageTwo(tk.Frame):  # Customer Page

    db_name = 'MyDatabase.db'

    def setStartPageRef2(self, startPageRef):
        self.startPageRef = startPageRef

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        AFont = font.Font(family='Calibri', size=10, weight='bold')
        BFont = font.Font(family='Calibri', size=9, )
        frame = LabelFrame(self, text="ค้นหา")
        frame.grid(row=1, sticky=NW)

        default = StringVar(self, value=0)
        Label(frame, text="เลขประจำตัวผู้เสียภาษีอากร (13 หลัก)", font=BFont).grid(row=0)
        Label(frame, text="สาขาที่", font=BFont).grid(row=1, sticky=E)
        self.tax_enter = Entry(frame)
        self.tax_enter.bind('<KP_Enter>', self.tax_search)
        self.tax_enter.grid(row=0, column=1, sticky=W)
        self.tax_enter.bind('<Return>', self.tax_search)
        self.branch_enter = Entry(frame, textvariable=default)
        self.branch_enter.grid(row=1, column=1, sticky=W)
        self.button2 = Button(frame, text='บันทึก', font=AFont, height=1, width=10, command=self.save_data)
        self.button2.grid(row=2, column = 1)

        frame3 = LabelFrame(self, text = "ผลลัพธ์")
        frame3.place(x= 350 , y = 51)
        self.tree = ttk.Treeview(frame3, height=15, column=("1"))
        self.tree.heading('#0', text="ประเภท")
        self.tree.heading(0, text="ผลลัพธ์")
        self.tree.grid(row=0)
        vsb = ttk.Scrollbar(frame3, orient='vertical', command=self.tree.yview)
        self.tree.grid(row=0, sticky = 'nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=vsb.set)

        frame2 = LabelFrame(self, text="ชุดคำสั่ง")
        frame2.grid(row=0)

        self.my_list = []


        button3 = ttk.Button(frame2, text="ขายสินค้ารายการเดียว", command=lambda: controller.show_frame(StartPage),
                             width=14)
        button3.grid(row=0, column=0, )
        button3 = ttk.Button(frame2, text="ขายสินค้าหลายรายการ", command=lambda: controller.show_frame(PageThree),
                             width=14)
        button3.grid(row=0, column=1, )
        button3 = ttk.Button(frame2, text="ข้อมูลสินค้า", command=lambda: controller.show_frame(PageOne),
                             width=11)
        button3.grid(row=0, column=2, )
        button3 = ttk.Button(frame2, text="ข้อมูลลูกค้า", command=lambda: controller.show_frame(PageTwo),
                             width=11)
        button3.grid(row=0, column=3, )
        button6 = ttk.Button(frame2, text="ประวัติ", command=lambda: controller.show_frame(PageFour),
                             width=11)
        button6.grid(row=0, column=4)
        button6 = ttk.Button(frame2, text="พนักงาน", command=lambda: controller.show_frame(PageFive),
                             width=11)
        button6.grid(row=0, column=5)



    def tax_search(self,event):

        check = True
        count = 0
        while check:
            try:
                for i in self.tree.get_children():
                    self.tree.delete(i)
                self.my_list.clear()
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                session = Session()
                session.verify = False
                transport = Transport(session=session)

                client = Client('https://rdws.rd.go.th/serviceRD3/vatserviceRD3.asmx?wsdl',
                                transport=transport)
                result = client.service.Service(
                    username='anonymous',
                    password='anonymous',
                    TIN=self.tax_enter.get(),
                    ProvinceCode=0,
                    BranchNumber=self.branch_enter.get(),
                    AmphurCode=0
                )

                # Convert Zeep Response object (in this case Service) to Python dict.
                result = zeep.helpers.serialize_object(result)

                for k in result.keys():
                    if result[k] is not None:
                        v = result[k].get('anyType', None)[0]
                        self.tree.insert('', 'end', text=k, value=v)
                        self.my_list.append(v)
            except:
                count = count + 1
                print(count)
            else:
                check = False
                messagebox.showinfo("ค้นหาข้อมูล", "ค้นหาเสร็จสิ้น")

    def save_data(self):
        try:
            conn = sqlite3.connect('MyDatabase.db')
            c = conn.cursor()
            c.execute('INSERT INTO Customer VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', self.my_list)
            conn.commit()
        except:
            messagebox.showwarning("คำเตือน!", "ข้อมูลนี้มีอยู่ในระบบแล้ว")

class PageThree(tk.Frame):  # CalPrice


    def setStartPageRef3(self, startPageRef):
        self.startPageRef = startPageRef

    def setStartPageRef6(self, startPageRef):
        self.startPageRef2 = startPageRef

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.now = datetime.datetime.now()
        AFont = font.Font(family='Calibri', size=12, weight='bold')
        BFont = font.Font(family='Calibri', size=11, )

        frame = ttk.LabelFrame(self, text='สินค้าทั้งหมด')
        frame.grid(row=1, column=0, sticky=NW)
        frame2 = ttk.LabelFrame(self, text='คำนวณราคา')
        frame2.place(x = 530, y = 50)
        frame3 = ttk.LabelFrame(self, text="ชุดคำสั่ง")
        frame3.grid(row=0, column=0, sticky=NW)
        frame10 = ttk.LabelFrame(self, text = "ผู้ซื้อ")
        frame10.grid(row=3,sticky = W)
        frame11 = ttk.LabelFrame(self, text = "เลขภาษี")
        frame11.place(x = 600 , y = 310)
        frame12 = ttk.LabelFrame(self, text = "ค้นหา")
        frame12.grid(row=2,column = 0,sticky = W)
        frame14 = ttk.LabelFrame(self, text = "ค้นหา")
        frame14.grid(row=2,column = 0,sticky = S)



        Label(frame, text="ชื่อสินค้า", font=("Helvetica", 10)).grid(row=1, sticky=W)
        self.product_name = ttk.Combobox(frame,width=25, justify='right', font=("Helvetica", 15), state='readonly')
        self.product_name.bind("<<ComboboxSelected>>", self.show_price)
        self.product_name.grid(row=2, column=0)

        self.product_name2 = ttk.Combobox(frame, width=25, justify='right', font=("Helvetica", 15), state='readonly')
        self.product_name2.bind("<<ComboboxSelected>>", self.show_price)
        self.product_name2.grid(row=3, column=0)

        self.product_name3 = ttk.Combobox(frame, width=25, justify='right', font=("Helvetica", 15), state='readonly')
        self.product_name3.bind("<<ComboboxSelected>>", self.show_price)
        self.product_name3.grid(row=4, column=0)

        self.product_name4 = ttk.Combobox(frame, width=25, justify='right', font=("Helvetica", 15), state='readonly')
        self.product_name4.bind("<<ComboboxSelected>>", self.show_price)
        self.product_name4.grid(row=5, column=0)

        self.product_name5 = ttk.Combobox(frame, width=25, justify='right', font=("Helvetica", 15), state='readonly')
        self.product_name5.bind("<<ComboboxSelected>>", self.show_price)
        self.product_name5.grid(row=6, column=0)

        self.product_name6 = ttk.Combobox(frame, width=25, justify='right', font=("Helvetica", 15), state='readonly')
        self.product_name6.bind("<<ComboboxSelected>>", self.show_price)
        self.product_name6.grid(row=7, column=0)

        self.combo_product()

        Label(frame12, text="ชื่อบริษัท", font=BFont).grid(row=1, column=0, sticky=E)
        self.search_comp_name = Entry(frame12, justify='right', width=17)
        self.search_comp_name.bind('<Return>', self.searchCompName)
        self.search_comp_name.grid(row=1, column=1, sticky=W)
        Label(frame12, text="รหัสภาษี", font=BFont).grid(row=2, column=0, sticky=E)
        self.search_tax_id = Entry(frame12, justify='right', width=17)
        self.search_tax_id.bind('<Return>', self.searchTaxId)
        self.search_tax_id.grid(row=2, column=1, sticky=W)

        Label(frame, text="ราคา(บาท)", font=("Helvetica", 10)).grid(row=1, column=1, sticky=W)
        self.product_price = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_price.grid(row=2, column=1)
        self.product_price2 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_price2.grid(row=3, column=1)
        self.product_price3 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_price3.grid(row=4, column=1)
        self.product_price4 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_price4.grid(row=5, column=1)
        self.product_price5 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_price5.grid(row=6, column=1)
        self.product_price6 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_price6.grid(row=7, column=1)

        Label(frame, text="จำนวน", font=("Helvetica", 10)).grid(row=1, column=2, sticky=W)
        self.product_number = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_number.bind("<KeyRelease>", self.LiveCal)
        self.product_number.grid(row=2, column=2)
        self.product_number2 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_number2.bind("<KeyRelease>", self.LiveCal2)
        self.product_number2.grid(row=3, column=2)
        self.product_number3 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_number3.bind("<KeyRelease>", self.LiveCal3)
        self.product_number3.grid(row=4, column=2)
        self.product_number4 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_number4.bind("<KeyRelease>", self.LiveCal4)
        self.product_number4.grid(row=5, column=2)
        self.product_number5 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_number5.bind("<KeyRelease>", self.LiveCa15)
        self.product_number5.grid(row=6, column=2)
        self.product_number6 = Text(frame, height=1, width=5, font=("Helvetica", 15))
        self.product_number6.bind("<KeyRelease>", self.LiveCa16)
        self.product_number6.grid(row=7, column=2)

        Label(frame, text="ราคาทั้งหมด", font=("Helvetica", 10)).grid(row=1, column=3, sticky=W)
        self.product_total = Text(frame, height=1, width=8, font=("Helvetica", 15))
        self.product_total.grid(row=2, column=3)
        self.product_total2 = Text(frame, height=1, width=8, font=("Helvetica", 15))
        self.product_total2.grid(row=3, column=3)
        self.product_total3 = Text(frame, height=1, width=8, font=("Helvetica", 15))
        self.product_total3.grid(row=4, column=3)
        self.product_total4 = Text(frame, height=1, width=8, font=("Helvetica", 15))
        self.product_total4.grid(row=5, column=3)
        self.product_total5 = Text(frame, height=1, width=8, font=("Helvetica", 15))
        self.product_total5.grid(row=6, column=3)
        self.product_total6 = Text(frame, height=1, width=8, font=("Helvetica", 15))
        self.product_total6.grid(row=7, column=3)

        self.cus_list = Listbox(frame11, height=5, selectmode=SINGLE)
        self.cus_list.bind('<Double-Button-1>', self.show_data)
        vsb = ttk.Scrollbar(frame11, orient="vertical", command = self.cus_list.yview)
        vsb.grid(row = 1 ,column = 1 , sticky = 'ns')
        self.cus_list.grid(row=1)
        self.cus_list.config(yscrollcommand = vsb.set)
        self.show_tax_data = tk.Button(self, text = "Reload data", command = self.show_tax_list)
        self.show_tax_data.place(x = 600 , y= 410)

        Label(frame10, text="ชื่อบริษัท", font=('Times New Roman', 10)).grid(row=1, column=0, sticky=E)
        self.comp_name = Entry(frame10, justify='right', width=14)
        self.comp_name.grid(row=1, column=1, sticky=W)
        Label(frame10, text="สาขา").grid(row=1, column=2, sticky=E)
        self.branch_num = Entry(frame10, justify='right', width=8)
        self.branch_num.grid(row=1, column=3, sticky=W)
        Label(frame10, text="ชื่อตึก").grid(row=1, column=4, sticky=E)
        self.building_name = Entry(frame10, justify='right', width=14)
        self.building_name.grid(row=1, column=5, sticky=W)
        Label(frame10, text="ชั้น").grid(row=1, column=6, sticky=E)
        self.branch_floor = Entry(frame10, justify='right', width=8)
        self.branch_floor.grid(row=1, column=7, sticky=W)
        Label(frame10, text="หมู่บ้าน").grid(row=2, column=0, sticky=E)
        self.village_name = Entry(frame10, justify='right', width=14)
        self.village_name.grid(row=2, column=1, sticky=W)
        Label(frame10, text="เลขห้อง").grid(row=2, column=2, sticky=E)
        self.room_no = Entry(frame10, justify='right', width=9)
        self.room_no.grid(row=2, column=3, sticky=W)
        Label(frame10, text="เลขที่บ้าน").grid(row=2, column=4, sticky=E)
        self.house_no = Entry(frame10, justify='right', width=14)
        self.house_no.grid(row=2, column=5, sticky=W)
        Label(frame10, text="หมู่").grid(row=2, column=6, sticky=E)
        self.Moo_no = Entry(frame10, justify='right', width=8)
        self.Moo_no.grid(row=2, column=7, sticky=W)
        Label(frame10, text="ซอย").grid(row=3, column=0, sticky=E)
        self.Soi_no = Entry(frame10, justify='right', width=14)
        self.Soi_no.grid(row=3, column=1, sticky=W)
        Label(frame10, text="ถนน").grid(row=3, column=2, sticky=E)
        self.Stree_name = Entry(frame10, justify='right', width=9)
        self.Stree_name.grid(row=3, column=3, sticky=W)
        Label(frame10, text="ตำบล").grid(row=3, column=4, sticky=E)
        self.Thumbon_name = Entry(frame10, justify='right', width=14)
        self.Thumbon_name.grid(row=3, column=5, sticky=W)
        Label(frame10, text="อำเภอ").grid(row=3, column=6, sticky=E)
        self.Aumper_name = Entry(frame10, justify='right', width=8)
        self.Aumper_name.grid(row=3, column=7, sticky=W)
        Label(frame10, text="จังหวัด").grid(row=4, column=0, sticky=E)
        self.Province_name = Entry(frame10, justify='right', width=14)
        self.Province_name.grid(row=4, column=1, sticky=W)
        Label(frame10, text="รหัสไปษณีย์").grid(row=4, column=2, sticky=E)
        self.Postcode = Entry(frame10, justify='right', width=9)
        self.Postcode.grid(row=4, column=3, sticky=W)
        Label(frame10, text="เลขประจำผู้เสียภาษีผู้ซื้อ").place(x=310, y=61)
        self.Cus_tax_num = Entry(frame10, justify='right', width=15)
        self.Cus_tax_num.place(x=440, y=60)

        Label(frame14, text = "ทะเบียนรถ", font = BFont).grid(row=0, sticky = E)
        self.car_plate = Entry(frame14, justify = 'right', width = 15)
        self.car_plate.grid(row = 0, column = 1)

        self.print = tk.Button(self , text = "พิมพ์",font=('Calibri', '20'),width = 5, command =self.print_confirmation)
        self.print.place(x = 570 , y = 230)


        Label(frame2, text="ราคารวมทั้งหมด", font=("Helvetica", 15)).grid(row=0, column=0)
        self.product_grand_total = Text(frame2, height=1, width=10, font=("Helvetica", 25))
        self.product_grand_total.grid(row=1, column=0)
        button1 = ttk.Button(frame2, text='คำนวณสินค้าทั้งหมด', command=self.CalProduct, width=15)
        button1.grid(row=2, columnspan=2)
        button2 = ttk.Button(frame2, text='ล้างข้อมูล', width=15, command=self.clear_data)
        button2.grid(row=3, columnspan=2)


        button3 = ttk.Button(frame3, text="ขายสินค้ารายการเดียว", command=lambda: controller.show_frame(StartPage),
                             width=14)
        button3.grid(row=0, column=0, )
        button3 = ttk.Button(frame3, text="ขายสินค้าหลายรายการ", command=lambda: controller.show_frame(PageThree),
                             width=14)
        button3.grid(row=0, column=1, )
        button3 = ttk.Button(frame3, text="ข้อมูลสินค้า", command=lambda: controller.show_frame(PageOne),
                             width=11)
        button3.grid(row=0, column=2, )
        button3 = ttk.Button(frame3, text="ข้อมูลลูกค้า", command=lambda: controller.show_frame(PageTwo),
                             width=11)
        button3.grid(row=0, column=3, )
        button6 = ttk.Button(frame3, text="ประวัติ", command=lambda: controller.show_frame(PageFour),
                             width=11)
        button6.grid(row=0, column=4)
        button6 = ttk.Button(frame3, text="พนักงาน", command=lambda: controller.show_frame(PageFive),
                             width=11)
        button6.grid(row=0, column=5)

        self.update_lastest_record()
        self.show_tax_list()

    def get_value(self):

        record_id = "INV-{0:07}".format(self.lastest_record_number + 1)
        record_total_price = self.product_grand_total.get("1.0", 'end-1c')
        recrod_car_plate = self.car_plate.get()
        record_staff_name = self.startPageRef.staff_name.get()
        record_date = self.now.strftime("%d" + "/" + "%m" + "/" + "%Y")
        record_comp_name = self.comp_name.get()
        Record_list = [record_date,
                       record_id,
                       record_comp_name,
                       record_total_price,
                       record_staff_name,
                       recrod_car_plate]

        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute(
            ' INSERT INTO Record(Record_Date, Record_ID, Company_Name, Total_Price,Staff_Name, Car_Plate) VALUES(?,?,?,?,?,?)',
            Record_list)
        con.commit()
        self.startPageRef2.viewing_record()
        self.product_list = [self.product_name.get(),
                             self.product_name2.get(),
                             self.product_name3.get(),
                             self.product_name4.get(),
                             self.product_name5.get(),
                             self.product_name6.get()]
        self.product_num_list = [self.product_number.get("1.0", 'end-1c'),
                                 self.product_number2.get("1.0", 'end-1c'),
                                 self.product_number3.get("1.0", 'end-1c'),
                                 self.product_number4.get("1.0", 'end-1c'),
                                 self.product_number5.get("1.0", 'end-1c'),
                                 self.product_number6.get("1.0", 'end-1c')]
        self.product_list = list(filter(None, self.product_list))
        self.product_num_list = list(filter(None, self.product_num_list))
        cur2 = con.cursor()
        for item_name,item_num in zip(self.product_list, self.product_num_list):
            cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)', (record_id, item_name, item_num))
        con.commit()



    def update_lastest_record(self):
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute(' SELECT Record_ID FROM Record ORDER BY Record_ID DESC LIMIT 1')
        self.lastest_record = str(cur.fetchone()).replace('INV-','').replace('(', '').replace(')', '').replace("'", '').replace(",", '')
        self.lastest_record_number = int(self.lastest_record)

    def print_receipt(self):

        try:
            record_id = "INV-{0:07}".format(self.lastest_record_number + 1)
            record_total_price = self.product_grand_total.get("1.0", 'end-1c')
            recrod_car_plate = self.car_plate.get()
            record_staff_name = self.startPageRef.staff_name.get()
            record_date = self.now.strftime("%d" + "/" + "%m" + "/" + "%Y")
            record_comp_name = self.comp_name.get()
            Record_list = [record_date,
                           record_id,
                           record_comp_name,
                           record_total_price,
                           record_staff_name,
                           recrod_car_plate]

            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute(
                ' INSERT INTO Record(Record_Date, Record_ID, Company_Name, Total_Price,Staff_Name, Car_Plate) VALUES(?,?,?,?,?,?)',
                Record_list)
            con.commit()
            self.startPageRef2.viewing_record()
            self.product_list = [self.product_name.get(),
                                 self.product_name2.get(),
                                 self.product_name3.get(),
                                 self.product_name4.get(),
                                 self.product_name5.get(),
                                 self.product_name6.get()]
            self.product_num_list = [self.product_number.get("1.0", 'end-1c'),
                                     self.product_number2.get("1.0", 'end-1c'),
                                     self.product_number3.get("1.0", 'end-1c'),
                                     self.product_number4.get("1.0", 'end-1c'),
                                     self.product_number5.get("1.0", 'end-1c'),
                                     self.product_number6.get("1.0", 'end-1c')]
            self.product_list = list(filter(None, self.product_list))
            self.product_num_list = list(filter(None, self.product_num_list))
            cur2 = con.cursor()
            for item_name, item_num in zip(self.product_list, self.product_num_list):
                cur2.execute('INSERT INTO Record_Product(Record_ID, Product_Name, Product_Number) VALUES(?,?,?)',
                             (record_id, item_name, item_num))
            con.commit()

        except:
            messagebox.showerror("เกิดข้อผิดพลาด","ข้อมูลไม่ถูกต้อง")
            self.confirmation.destroy()
        else:
            self.product_list = [self.product_name.get(),
                                 self.product_name2.get(),
                                 self.product_name3.get(),
                                 self.product_name4.get(),
                                 self.product_name5.get(),
                                 self.product_name6.get()]
            self.product_price_list = [self.product_price.get("1.0", 'end-1c'),
                                       self.product_price2.get("1.0", 'end-1c'),
                                       self.product_price3.get("1.0", 'end-1c'),
                                       self.product_price4.get("1.0", 'end-1c'),
                                       self.product_price5.get("1.0", 'end-1c'),
                                       self.product_price6.get("1.0", 'end-1c')]
            self.product_num_list = [self.product_number.get("1.0", 'end-1c'),
                                     self.product_number2.get("1.0", 'end-1c'),
                                     self.product_number3.get("1.0", 'end-1c'),
                                     self.product_number4.get("1.0", 'end-1c'),
                                     self.product_number5.get("1.0", 'end-1c'),
                                     self.product_number6.get("1.0", 'end-1c')]
            self.product_total_list = [self.product_total.get("1.0", 'end-1c'),
                                       self.product_total2.get("1.0", 'end-1c'),
                                       self.product_total3.get("1.0", 'end-1c'),
                                       self.product_total4.get("1.0", 'end-1c'),
                                       self.product_total5.get("1.0", 'end-1c'),
                                       self.product_total6.get("1.0", 'end-1c')]
            self.product_list = list(filter(None, self.product_list))
            self.product_price_list = list(filter(None, self.product_price_list))
            self.product_num_list = list(filter(None, self.product_num_list))
            self.product_total_list = list(filter(None, self.product_total_list))

            record_id = "INV-{0:07}".format(self.lastest_record_number + 1)
            tax_id = '0203556007965'
            tempfiles = tempfile.mktemp(".txt")
            receipt = open(tempfiles, "wt", encoding="utf-8")
            receipt.write("\t       ใบเสร็จรับเงิน/ใบกำกับภาษี(ต้นฉบับ)\n")
            receipt.write(
                "หจก.เดอะวันปิโตเลียม\n9/7 หมู่ 3 ถ.สุขุมวิท ต.ห้วยกะปิ\nอ.เมืองชลบุรี จ.ชลบุรี 20000\nTel. 086-4069062 FAX: 02-9030080 ต่อ 7811\n")
            receipt.write("Tax ID:" + tax_id + '\n')
            receipt.write("สาขาที่ออกใบกำกับภาษี: สำนักงานใหญ่\n")
            receipt.write("เลขที่: " + record_id + "\n")
            receipt.write("วันที่: " + self.now.strftime("%d" + "/" + "%m" + "/" + "%Y") + " " + self.now.strftime(
                "%H" + ":" + "%M") + "\n")
            receipt.write("ชื่อ: " + self.comp_name.get() + "\n")
            receipt.write("ที่อยู่: " + self.house_no.get() + " ")
            if self.Moo_no.get() is not '-':
                receipt.write("หมู่ " + self.Moo_no.get() + " ")
            if self.Soi_no.get() is not '-':
                receipt.write("ซ." + self.Soi_no.get() + " ")
            if self.Stree_name.get() is not '-':
                receipt.write("ถ." + self.Stree_name.get() + " ")
            if self.Thumbon_name.get() is not '-':
                receipt.write("ต." + self.Thumbon_name.get() + " ")
            receipt.write("\n")
            if self.Aumper_name.get() is not '-':
                receipt.write("        อ." + self.Aumper_name.get() + " ")
            if self.Province_name.get() is not '-':
                receipt.write("จ." + self.Province_name.get() + " ")
            if self.Postcode.get() is not '-':
                receipt.write(" " + self.Postcode.get() + " ")
            receipt.write("\n")
            receipt.write("เลขประจำผู้เสียภาษีผู้ซื้อ: " + self.Cus_tax_num.get() + "\n")
            receipt.write("ทะเบียนรถ: " + self.car_plate.get())
            receipt.write("\n")
            receipt.write("รายการ\t\t\tราคา\t\tปริมาณ\t\tจำนวนเงิน\n")
            receipt.write("========================================\n")

            for i in range(0, len(self.product_list)):
                receipt.write(self.product_list[i] + "\t   ")
                receipt.write(self.product_price_list[i] + "\t        ")
                receipt.write(self.product_num_list[i] + "\t")
                receipt.write(self.product_total_list[i] + "\n")

            receipt.write("\n\n")
            receipt.write("มูลค่าสินค้า:")
            receipt.write("\t\t" + self.product_grand_total.get("1.0", 'end-1c') + "\n")
            receipt.write("ภาษีมูลค่าเพิ่ม(VAT 7%)  ")
            vat = float(self.product_grand_total.get("1.0", 'end-1c')) / 107
            receipt.write("\t" + str(round(vat, 2)) + "\n")
            total = float(self.product_grand_total.get("1.0", 'end-1c')) - vat
            receipt.write("รวมเป็นเงิน:")
            receipt.write("'\t\t" + str(round(total, 0)))
            receipt.write("\n\n\nได้รับสินค้าตามรายการบนนี้ไว้ถูกต้อง\nและในสภาพเรียบร้อยทุกประการ")
            receipt.write("\n\n\nลงชื่อผู้รับเงิน _________________________________")
            receipt.write("\n\n\t         *****ขอบคุณที่ใช้บริการ*****")

            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, tempfiles])

            self.update_lastest_record()
            self.comp_name.delete(0, 'end')
            self.branch_num.delete(0, 'end')
            self.branch_floor.delete(0, 'end')
            self.building_name.delete(0, 'end')
            self.village_name.delete(0, 'end')
            self.house_no.delete(0, 'end')
            self.Moo_no.delete(0, 'end')
            self.Soi_no.delete(0, 'end')
            self.Stree_name.delete(0, 'end')
            self.Thumbon_name.delete(0, 'end')
            self.Aumper_name.delete(0, 'end')
            self.Province_name.delete(0, 'end')
            self.Postcode.delete(0, 'end')
            self.Cus_tax_num.delete(0, 'end')
            self.car_plate.delete(0,'end')

            self.confirmation.destroy()


    def print_confirmation(self):



        self.confirmation = Toplevel()
        self.confirmation.title("ยืนยันหรือไม่")
        self.confirmation.geometry("%dx%d+%d+%d" % (270, 90, 300, 250))
        Label(self.confirmation, text = "ยืนยันการสั่งพิมพ์หรือไม่?", font=("Helvetica", 20)).grid(row=0,columnspan = 2)
        self.confirm_button = Button(self.confirmation, text = "ยืนยัน", font=("Helvetica", 14), width = 5, command = self.print_receipt)
        self.confirm_button.grid(row=1)
        self.cancel_button = Button(self.confirmation, text = "ยกเลิก", font=("Helvetica", 14), width = 5 , command = self.confirmation.destroy)
        self.cancel_button.grid(row=1, column = 1)
        self.confirmation.focus_set()
        self.confirmation.grab_set()
        self.confirmation.mainloop()


    def show_tax_list(self):

        self.cus_list.delete(0,END)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Tax_ID FROM Customer ORDER BY Tax_ID DESC LIMIT 5')
        for row in cur.fetchall():
            self.cus_list.insert(END, row)

    def searchCompName(self, event):
        try:
            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute('SELECT Name FROM Customer WHERE Name like ?', ('%' + self.search_comp_name.get() + '%',))
            self.tax_list = Toplevel()
            self.tax_list.title("Result")
            self.tax_list.geometry("500x200")
            Label(self.tax_list, text="รายชื่อบริษัท").grid(row=0)
            self.tax = Listbox(self.tax_list, height=10, width=40, selectmode=SINGLE)
            self.tax.bind("<Double-Button>", self.show_tax_id)
            self.tax.grid(row=1)
            for row in cur.fetchall():
                self.tax.insert(END, row)
            Label(self.tax_list, text="รหัสภาษี").grid(row=0, column=1)
            self.tax_id = Listbox(self.tax_list, height=10, width=40, selectmode=SINGLE)
            self.tax_id.bind('<Double-Button>', self.show_data2)
            self.tax_id.grid(row=1, column=1)

            self.tax_list.focus_set()
            self.tax_list.grab_set()
            self.tax_list.mainloop()
        except:
            messagebox.showwarning("เกิดข้อผิดพลาด", "ไม่พบข้อมูล")
            self.tax_list.destroy()


    def searchTaxId(self, event):
        try:
            con = sqlite3.connect('MyDatabase.db')
            cur = con.cursor()
            cur.execute("SELECT Name FROM Customer WHERE Tax_ID like ?", ('%' + self.search_tax_id.get() + '%',))
            self.tax_list = Toplevel()
            self.tax_list.title("Result")
            self.tax_list.geometry("500x200")
            Label(self.tax_list, text="รายชื่อบริษัท").grid(row=0)
            self.tax = Listbox(self.tax_list, height=10, width=40, selectmode=SINGLE)
            self.tax.bind("<Double-Button>", self.show_data3)
            self.tax.grid(row=1)
            for row in cur.fetchall():
                self.tax.insert(END, row)

            self.tax_list.focus_set()
            self.tax_list.grab_set()
            self.tax_list.mainloop()
        except:
            messagebox.showwarning("เกิดข้อผิดพลาด","ไม่พบข้อมูล")
            self.tax_list.destroy()

    def show_tax_id(self, event):

        self.tax_id.delete(0, 'end')
        self.get_tax_value = self.tax.get(self.tax.curselection())
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Tax_ID FROM Customer WHERE Name = ? ', (self.get_tax_value))
        for row in cur.fetchall():
            self.tax_id.insert(END, row)

    def show_data(self, event):

        self.comp_name.delete(0, 'end')
        self.branch_num.delete(0, 'end')
        self.branch_floor.delete(0, 'end')
        self.building_name.delete(0, 'end')
        self.village_name.delete(0, 'end')
        self.house_no.delete(0, 'end')
        self.Moo_no.delete(0, 'end')
        self.Soi_no.delete(0, 'end')
        self.Stree_name.delete(0, 'end')
        self.Thumbon_name.delete(0, 'end')
        self.Aumper_name.delete(0, 'end')
        self.Province_name.delete(0, 'end')
        self.Postcode.delete(0, 'end')
        self.Cus_tax_num.delete(0, 'end')

        self.get_selecte_value = self.cus_list.get(self.cus_list.curselection())


        self.Cus_tax_num.insert(END, self.get_selecte_value)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Name FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.comp_name.insert(END,
                              str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur2 = con.cursor()
        cur2.execute('SELECT BranchNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.branch_num.insert(END, cur2.fetchone())

        cur3 = con.cursor()
        cur3.execute('SELECT BuildingName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.building_name.insert(END,
                                  str(cur3.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",",
                                                                                                                  ''))

        cur4 = con.cursor()
        cur4.execute('SELECT FloorNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.branch_floor.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT VillageName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.village_name.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT HouseNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.house_no.insert(END, cur6.fetchall())

        cur7 = con.cursor()
        cur7.execute('SELECT MooNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Moo_no.insert(END, cur7.fetchall())

        cur8 = con.cursor()
        cur8.execute('SELECT SoiName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Soi_no.insert(END,
                           str(cur8.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur9 = con.cursor()
        cur9.execute('SELECT StreetName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Stree_name.insert(END, cur9.fetchall())

        cur10 = con.cursor()
        cur10.execute('SELECT Thambol FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Thumbon_name.insert(END, cur10.fetchall())

        cur11 = con.cursor()
        cur11.execute('SELECT Amphur FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Aumper_name.insert(END, cur11.fetchall())

        cur12 = con.cursor()
        cur12.execute('SELECT Province FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Province_name.insert(END, cur12.fetchall())

        cur13 = con.cursor()
        cur13.execute('SELECT PostCode FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
        self.Postcode.insert(END, cur13.fetchall())

    def show_data2(self, event):

        self.comp_name.delete(0, 'end')
        self.branch_num.delete(0, 'end')
        self.branch_floor.delete(0, 'end')
        self.building_name.delete(0, 'end')
        self.village_name.delete(0, 'end')
        self.house_no.delete(0, 'end')
        self.Moo_no.delete(0, 'end')
        self.Soi_no.delete(0, 'end')
        self.Stree_name.delete(0, 'end')
        self.Thumbon_name.delete(0, 'end')
        self.Aumper_name.delete(0, 'end')
        self.Province_name.delete(0, 'end')
        self.Postcode.delete(0, 'end')
        self.Cus_tax_num.delete(0, 'end')
        self.get_value = self.tax_id.get(self.tax_id.curselection())

        self.Cus_tax_num.insert(END, self.get_value)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Name FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.comp_name.insert(END,
                              str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur2 = con.cursor()
        cur2.execute('SELECT BranchNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.branch_num.insert(END, cur2.fetchone())

        cur3 = con.cursor()
        cur3.execute('SELECT BuildingName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.building_name.insert(END,
                                  str(cur3.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",",
                                                                                                                  ''))

        cur4 = con.cursor()
        cur4.execute('SELECT FloorNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.branch_floor.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT VillageName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.village_name.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT HouseNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.house_no.insert(END, cur6.fetchall())

        cur7 = con.cursor()
        cur7.execute('SELECT MooNumber FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Moo_no.insert(END, cur7.fetchall())

        cur8 = con.cursor()
        cur8.execute('SELECT SoiName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Soi_no.insert(END,
                           str(cur8.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur9 = con.cursor()
        cur9.execute('SELECT StreetName FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Stree_name.insert(END, cur9.fetchall())

        cur10 = con.cursor()
        cur10.execute('SELECT Thambol FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Thumbon_name.insert(END, cur10.fetchall())

        cur11 = con.cursor()
        cur11.execute('SELECT Amphur FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Aumper_name.insert(END, cur11.fetchall())

        cur12 = con.cursor()
        cur12.execute('SELECT Province FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Province_name.insert(END, cur12.fetchall())

        cur13 = con.cursor()
        cur13.execute('SELECT PostCode FROM Customer WHERE Tax_ID = ?', (self.get_value))
        self.Postcode.insert(END, cur13.fetchall())

        self.tax_list.destroy()

    def show_data3(self, event):

        self.comp_name.delete(0, 'end')
        self.branch_num.delete(0, 'end')
        self.branch_floor.delete(0, 'end')
        self.building_name.delete(0, 'end')
        self.village_name.delete(0, 'end')
        self.house_no.delete(0, 'end')
        self.Moo_no.delete(0, 'end')
        self.Soi_no.delete(0, 'end')
        self.Stree_name.delete(0, 'end')
        self.Thumbon_name.delete(0, 'end')
        self.Aumper_name.delete(0, 'end')
        self.Province_name.delete(0, 'end')
        self.Postcode.delete(0, 'end')
        self.Cus_tax_num.delete(0, 'end')
        self.get_selecte_value = self.tax.get(self.tax.curselection())

        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Name FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.comp_name.insert(END,
                              str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur2 = con.cursor()
        cur2.execute('SELECT BranchNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.branch_num.insert(END, cur2.fetchone())

        cur3 = con.cursor()
        cur3.execute('SELECT BuildingName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.building_name.insert(END,
                                  str(cur3.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",",
                                                                                                                  ''))

        cur4 = con.cursor()
        cur4.execute('SELECT FloorNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.branch_floor.insert(END, cur4.fetchall())

        cur5 = con.cursor()
        cur5.execute('SELECT VillageName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.village_name.insert(END, cur5.fetchall())

        cur6 = con.cursor()
        cur6.execute('SELECT HouseNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.house_no.insert(END, cur6.fetchall())

        cur7 = con.cursor()
        cur7.execute('SELECT MooNumber FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Moo_no.insert(END, cur7.fetchall())

        cur8 = con.cursor()
        cur8.execute('SELECT SoiName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Soi_no.insert(END,
                           str(cur8.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

        cur9 = con.cursor()
        cur9.execute('SELECT StreetName FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Stree_name.insert(END, cur9.fetchall())

        cur10 = con.cursor()
        cur10.execute('SELECT Thambol FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Thumbon_name.insert(END, cur10.fetchall())

        cur11 = con.cursor()
        cur11.execute('SELECT Amphur FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Aumper_name.insert(END, cur11.fetchall())

        cur12 = con.cursor()
        cur12.execute('SELECT Province FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Province_name.insert(END, cur12.fetchall())

        cur13 = con.cursor()
        cur13.execute('SELECT PostCode FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Postcode.insert(END, cur13.fetchall())

        cur14 = con.cursor()
        cur14.execute('SELECT Tax_ID FROM Customer WHERE Name = ?', (self.get_selecte_value))
        self.Cus_tax_num.insert(END, cur14.fetchall())

        self.tax_list.destroy()

    def CalProduct(self):

        self.product_grand_total.delete(1.0,'end')
        price_total = [
            self.product_total.get("1.0", 'end-1c'),
            self.product_total2.get("1.0", 'end-1c'),
            self.product_total3.get("1.0", 'end-1c'),
            self.product_total4.get("1.0", 'end-1c'),
            self.product_total5.get("1.0", 'end-1c'),
            self.product_total6.get("1.0", 'end-1c')
        ]
        sum = 0
        for x in price_total:
            try:
                sum += float(x)
            except:
                pass
        self.product_grand_total.insert(END, round(sum, 2))

    def show_price(self, event):
        con = sqlite3.connect('MyDatabase.db')

        self.product_price.delete(1.0, END)
        cur = con.cursor()
        cur.execute('SELECT Product_Price FROM Product WHERE Product_Name = ?', (self.product_name.get(),))
        self.product_price.insert(END, cur.fetchall())

        self.product_price2.delete(1.0, END)
        cur2 = con.cursor()
        cur2.execute('SELECT Product_Price FROM Product WHERE Product_Name = ?', (self.product_name2.get(),))
        self.product_price2.insert(END, cur2.fetchall())

        self.product_price3.delete(1.0, END)
        cur3 = con.cursor()
        cur3.execute('SELECT Product_Price FROM Product WHERE Product_Name = ?', (self.product_name3.get(),))
        self.product_price3.insert(END, cur3.fetchall())

        self.product_price4.delete(1.0, END)
        cur4 = con.cursor()
        cur4.execute('SELECT Product_Price FROM Product WHERE Product_Name = ?', (self.product_name4.get(),))
        self.product_price4.insert(END, cur4.fetchall())

        self.product_price5.delete(1.0, END)
        cur5 = con.cursor()
        cur5.execute('SELECT Product_Price FROM Product WHERE Product_Name = ?', (self.product_name5.get(),))
        self.product_price5.insert(END, cur5.fetchall())

        self.product_price6.delete(1.0, END)
        cur6 = con.cursor()
        cur6.execute('SELECT Product_Price FROM Product WHERE Product_Name = ?', (self.product_name6.get(),))
        self.product_price6.insert(END, cur6.fetchall())

    def LiveCal(self, event):

        self.product_total.delete(1.0, END)
        price = int(self.product_number.get("1.0", 'end-1c')) * float(self.product_price.get("1.0", 'end-1c'))
        self.product_total.insert(END, round(price, 2))

    def LiveCal2(self, event):

        self.product_total2.delete(1.0, END)
        price2 = int(self.product_number2.get("1.0", 'end-1c')) * float(self.product_price2.get("1.0", 'end-1c'))
        self.product_total2.insert(END, round(price2, 2))

    def LiveCal3(self, event):

        self.product_total3.delete(1.0, END)
        price3 = int(self.product_number3.get("1.0", 'end-1c')) * float(self.product_price3.get("1.0", 'end-1c'))
        self.product_total3.insert(END, round(price3, 2))

    def LiveCal4(self, event):

        self.product_total4.delete(1.0, END)
        price4 = int(self.product_number4.get("1.0", 'end-1c')) * float(self.product_price4.get("1.0", 'end-1c'))
        self.product_total4.insert(END, round(price4, 2))

    def LiveCa15(self, event):

        self.product_total5.delete(1.0, END)
        price5 = int(self.product_number5.get("1.0", 'end-1c')) * float(self.product_price5.get("1.0", 'end-1c'))
        self.product_total5.insert(END, round(price5, 2))

    def LiveCa16(self, event):

        self.product_total6.delete(1.0, END)
        price6 = int(self.product_number6.get("1.0", 'end-1c')) * float(self.product_price6.get("1.0", 'end-1c'))
        self.product_total6.insert(END, round(price6, 2))

    def combo_product(self):
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Product_Name FROM Product')

        self.data = []

        for row in cur.fetchall():
            self.data.append(row[0])

        self.product_name['values'] = self.data
        self.product_name2['values'] = self.data
        self.product_name3['values'] = self.data
        self.product_name4['values'] = self.data
        self.product_name5['values'] = self.data
        self.product_name6['values'] = self.data



    def clear_data(self):

        self.product_name.set('')
        self.product_name2.set('')
        self.product_name3.set('')
        self.product_name4.set('')
        self.product_name5.set('')
        self.product_name6.set('')

        self.product_price.delete(1.0, END)
        self.product_price2.delete(1.0, END)
        self.product_price3.delete(1.0, END)
        self.product_price4.delete(1.0, END)
        self.product_price5.delete(1.0, END)
        self.product_price6.delete(1.0, END)

        self.product_number.delete(1.0, END)
        self.product_number2.delete(1.0, END)
        self.product_number3.delete(1.0, END)
        self.product_number4.delete(1.0, END)
        self.product_number5.delete(1.0, END)
        self.product_number6.delete(1.0, END)

        self.product_total.delete(1.0, END)
        self.product_total2.delete(1.0, END)
        self.product_total3.delete(1.0, END)
        self.product_total4.delete(1.0, END)
        self.product_total5.delete(1.0, END)
        self.product_total6.delete(1.0, END)

        self.product_grand_total.delete(1.0, END)


class PageFour(tk.Frame):

    db_name = 'MyDatabase.db'


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = LabelFrame(self, text = "" )
        frame.grid(row = 2)


        self.history_list = ttk.Treeview(frame, height = 18, column =('A','B','C','D','E','F'))
        self.history_list.heading('#0', text = "วันที่เอกสาร")
        self.history_list.heading('A', text = "เลขที่เอกสาร")
        self.history_list.heading('B', text="ชื่อลูกค้า")
        self.history_list.heading('C', text="เลขทะเบียนรถ")
        self.history_list.heading('D', text="จำนวนเงิน")
        self.history_list.heading('E', text="ผู้รับผิดชอบ")
        self.history_list.heading('F', text="สถานะ")
        self.history_list.column('#0', width=110)
        self.history_list.column('A', width=110)
        self.history_list.column('B', width=200)
        self.history_list.column('C', width=100)
        self.history_list.column('D', width=110)
        self.history_list.column('E', width=110)
        self.history_list.column('F', width=50)
        vsb = ttk.Scrollbar(frame, orient='vertical', command=self.history_list.yview)
        hsb = ttk.Scrollbar(frame, orient = 'horizontal' , command = self.history_list.xview)
        self.history_list.grid(row=0, sticky = 'nsew')
        self.history_list.bind('<Double-Button-1>', self.show_details)
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        self.history_list.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)


        Label(self, text = "ค้นหาตามวันที่",font=("Helvetica", 11)).grid(row = 1 ,sticky = W)
        self.date_search = Entry(self, justify = 'right', width = 13)
        self.date_search.bind('<KeyRelease>', self.search_record_date)
        self.date_search.place(x = 120, y = 47)
        Label(self, text = "ค้นหาตามชื่อ", font=("Helvetica", 11)).place(x = 250 , y = 48)
        self.comp_name_search = Entry(self, justify = 'right', width = 13)
        self.comp_name_search.bind('<KeyRelease>', self.search_record_name)
        self.comp_name_search.place(x = 360, y =47)
        self.cancel_but = tk.Button(self,text="ยกเลิกใบกำกับภาษี", command = self.cancel_record)
        self.cancel_but.place(x = 670, y = 40)

        frame3 = ttk.LabelFrame(self, text="ชุดคำสั่ง")
        frame3.grid(row=0, column=0, sticky=NW)

        button3 = ttk.Button(frame3, text="ขายสินค้ารายการเดียว", command=lambda: controller.show_frame(StartPage),
                             width=14)
        button3.grid(row=0, column=0, )
        button3 = ttk.Button(frame3, text="ขายสินค้าหลายรายการ", command=lambda: controller.show_frame(PageThree),
                             width=14)
        button3.grid(row=0, column=1, )
        button3 = ttk.Button(frame3, text="ข้อมูลสินค้า", command=lambda: controller.show_frame(PageOne),
                             width=11)
        button3.grid(row=0, column=2, )
        button3 = ttk.Button(frame3, text="ข้อมูลลูกค้า", command=lambda: controller.show_frame(PageTwo),
                             width=11)
        button3.grid(row=0, column=3, )
        button6 = ttk.Button(frame3, text="ประวัติ", command=lambda: controller.show_frame(PageFour),
                             width=11)
        button6.grid(row=0, column=4)
        button6 = ttk.Button(frame3, text="พนักงาน", command=lambda: controller.show_frame(PageFive),
                             width=11)
        button6.grid(row=0, column=5)
        self.viewing_record()

    def show_details(self, event):

        record_date = self.history_list.item(self.history_list.selection())['text']
        record_tax_id = self.history_list.item(self.history_list.selection())['values'][0]
        record_comp_name = self.history_list.item(self.history_list.selection())['values'][1]
        record_car_plate = self.history_list.item(self.history_list.selection())['values'][2]
        record_total_price = self.history_list.item(self.history_list.selection())['values'][3]
        record_staff_name = self.history_list.item(self.history_list.selection())['values'][4]
        self.more_detail = Toplevel()
        self.more_detail.title("Result")
        self.more_detail.geometry("350x400")
        Label(self.more_detail, text="วันที่:").grid(row=0)
        Label(self.more_detail, text=record_date).grid(row=0, column=1)
        Label(self.more_detail, text="เลขที่:").grid(row=1)
        Label(self.more_detail, text=record_tax_id).grid(row=1, column=1)
        Label(self.more_detail, text="ชื่อพนักงาน:").grid(row=2)
        Label(self.more_detail, text=record_staff_name).grid(row=2, column=1)
        Label(self.more_detail, text="ชื่อลูกค้า:").grid(row=3)
        Label(self.more_detail, text=record_comp_name).grid(row=3, column=1)
        Label(self.more_detail, text="ทะเบียนรถ:").grid(row=4)
        Label(self.more_detail, text=record_car_plate).grid(row=4, column=1)
        Label(self.more_detail, text="ราคาทั้งหมด:").grid(row=5)
        Label(self.more_detail, text=record_total_price).grid(row=5, column=1)
        frame = LabelFrame(self.more_detail, text="รายการสินค้าทั้งหมด")
        frame.grid(row=0, column=2)
        self.product_list = ttk.Treeview(self.more_detail, height=5, column=('A'))
        self.product_list.heading('#0', text="ชื่อสินค้า")
        self.product_list.heading('A', text="จำนวน")
        self.product_list.column('#0', width=200)
        self.product_list.column('A', width=80)
        self.product_list.place(x=20, y=150)
        Label(self.more_detail, text="สินค้าทั้งหมด").place(x=20, y=125)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute(
            "SELECT Product_Name, Product_Number FROM Record_Product INNER JOIN Record ON Record.Record_ID = Record_Product.Record_ID WHERE Record_Product.Record_ID = ?",
            (record_tax_id,))
        for row in cur.fetchall():
            self.product_list.insert('', 0, text=row[0], values=(row[1]))

        self.more_detail.focus_set()
        self.more_detail.grab_set()
        self.more_detail.mainloop()

    def cancel_record(self):
        try:
            self.history_list.item(self.history_list.selection())['values'][1]
        except IndexError as e:
            messagebox.showwarning("เกิดข้อผิดพลาด", "กรุณาเลือกสินค้า")
            return
        record_id = self.history_list.item(self.history_list.selection())['values'][0]
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT Status FROM Record WHERE Record_ID = ?' , (record_id,))
        record_status = (str(cur.fetchone()).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))
        if record_status == 'ยกเลิก':
            normal_status = '-'
            cur2 = con.cursor()
            cur2.execute('UPDATE Record SET Status = ? WHERE Record_ID = ?', (normal_status, record_id))
            con.commit()
            self.viewing_record()
        else:
            cancel_text = 'ยกเลิก'
            cur3 = con.cursor()
            cur3.execute('UPDATE Record SET Status = ? WHERE Record_ID = ?', (cancel_text, record_id))
            con.commit()
            self.viewing_record()




    def viewing_record(self):
        records = self.history_list.get_children()
        for element in records:
            self.history_list.delete(element)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Record ORDER BY Record_ID DESC')
        for row in cur.fetchall():
            self.history_list.insert('', 0, text=row[1], values=(row[0], row[3],row[2], row[4],row[5],row[6]))

    def search_record_date(self,event):
        records = self.history_list.get_children()
        for element in records:
            self.history_list.delete(element)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Record WHERE Record_Date like ? ORDER BY Record_ID DESC',('%' + self.date_search.get() + '%',))
        for row in cur.fetchall():
            self.history_list.insert('', 0, text=row[1], values=(row[0], row[3], row[2], row[4],row[5],row[6]))

    def search_record_name(self,event):
        records = self.history_list.get_children()
        for element in records:
            self.history_list.delete(element)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Record WHERE Company_Name like ? ORDER BY Record_ID DESC',('%' + self.comp_name_search.get() + '%',))
        for row in cur.fetchall():
            self.history_list.insert('', 0, text=row[1], values=(row[0], row[3], row[2], row[4],row[5],row[6]))


class PageFive(tk.Frame):

    db_name = 'MyDatabase.db'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        frame1 = LabelFrame(self, text = "ลงทะเบียนพนักงาน")
        frame1.grid(row =1,sticky = W)
        frame3 = LabelFrame(self, text = "รายชื่อพนักงานทั้งหมด")
        frame3.grid(row = 2, sticky = W)
        frame4 = LabelFrame(self, text = "ประวัติพนักงานเข้า-ออก")
        frame4.place( x = 250 , y = 86)

        Label(frame1, text = "ใส่่ชื่อพนักงาน:").grid(row = 0)
        self.staff_name = Entry(frame1, justify = 'right')
        self.staff_name.bind('<KP_Enter>', self.add_confirmation)
        self.staff_name.grid(row = 0, column = 1)
        self.staff_name.bind('<Return>', self.add_confirmation)

        Label(frame3, text = "ค้นหา:").grid(row = 0, sticky = W)

        self.staff_list = ttk.Treeview(frame3, height = 15, column =('A'))
        self.staff_list.heading('#0', text = "ชื่อพนักงาน")
        self.staff_list.heading('A', text = "รหัสพนักงาน")
        self.staff_list.column('#0', width=150)
        self.staff_list.column('A', width=80)
        vsb = ttk.Scrollbar(frame3, orient='vertical', command=self.staff_list.yview)
        self.staff_list.grid(row=1, sticky = 'nsew')
        vsb.grid(row=1, column=1, sticky='ns')
        self.staff_list.configure(yscrollcommand=vsb.set)

        Label(frame4, text="ค้นหา:").grid(row=0, sticky=W)
        self.staff_record_list = ttk.Treeview(frame4, height=15, column=('A', 'B', 'C','D'))
        self.staff_record_list.heading('#0', text="ชื่อพนักงาน")
        self.staff_record_list.heading('A', text="รหัสพนักงาน")
        self.staff_record_list.heading('B', text="วันที่")
        self.staff_record_list.heading('C', text="เข้ากะ")
        self.staff_record_list.heading('D', text="ออกกะ")
        self.staff_record_list.column('#0', width=150)
        self.staff_record_list.column('A', width=80)
        self.staff_record_list.column('B', width=100)
        self.staff_record_list.column('C', width=80)
        self.staff_record_list.column('D', width=80)
        vsb2 = ttk.Scrollbar(frame4, orient='vertical', command=self.staff_record_list.yview)
        self.staff_record_list.grid(row=1, sticky='nsew')
        vsb2.grid(row=1, column=1, sticky='ns')
        self.staff_record_list.configure(yscrollcommand=vsb2.set)



        frame2 = LabelFrame(self, text='ชุดคำสั่ง')
        frame2.grid(row=0, column=0, sticky=W)


        button3 = ttk.Button(frame2, text="ขายสินค้ารายการเดียว", command=lambda: controller.show_frame(StartPage),
                             width=14)
        button3.grid(row=0, column=0, )
        button3 = ttk.Button(frame2, text="ขายสินค้าหลายรายการ", command=lambda: controller.show_frame(PageThree),
                             width=14)
        button3.grid(row=0, column=1, )
        button3 = ttk.Button(frame2, text="ข้อมูลสินค้า", command=lambda: controller.show_frame(PageOne),
                             width=11)
        button3.grid(row=0, column=2, )
        button3 = ttk.Button(frame2, text="ข้อมูลลูกค้า", command=lambda: controller.show_frame(PageTwo),
                             width=11)
        button3.grid(row=0, column=3, )
        button6 = ttk.Button(frame2, text="ประวัติ", command=lambda: controller.show_frame(PageFour),
                             width=11)
        button6.grid(row=0, column=4)
        button6 = ttk.Button(frame2, text="พนักงาน", command=lambda: controller.show_frame(PageFive),
                             width=11)
        button6.grid(row=0, column=5)

        self.show_staff_record()
        self.show_staff()
    def show_staff(self):
        records = self.staff_list.get_children()
        for element in records:
            self.staff_list.delete(element)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Staff ORDER BY Staff_ID ASC')
        for row in cur.fetchall():
            self.staff_list.insert('', END, text=row[1], values=(row[0]))

    def show_staff_record(self):
        records = self.staff_record_list.get_children()
        for element in records:
            self.staff_record_list.delete(element)
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Staff_Record ORDER BY Staff_Record_ID ASC')
        for row in cur.fetchall():
            self.staff_record_list.insert('', END, text=row[2], values=(row[1],row[3],row[4],row[5]))

    def add_staff(self):
        con = sqlite3.connect('MyDatabase.db')
        cur = con.cursor()
        cur.execute('INSERT INTO Staff(Staff_Name) VALUES(?)' , (self.staff_name.get(),))
        con.commit()
        self.confirmation.destroy()
        self.show_staff()

    def add_confirmation(self,event):

        self.confirmation = Toplevel()
        self.confirmation.title("ยืนยันหรือไม่")
        self.confirmation.geometry("%dx%d+%d+%d" % (270, 90, 300, 250))
        Label(self.confirmation, text="ยืนยันการการลงทะเบียนหรือไม่?", font=("Helvetica", 15)).grid(row=0,columnspan=2)
        self.confirm_button = Button(self.confirmation, text="ยืนยัน", font=("Helvetica", 14), width=5,
                                         command=self.add_staff)
        self.confirm_button.grid(row=1)
        self.cancel_button = Button(self.confirmation, text="ยกเลิก", font=("Helvetica", 14), width=5,command=self.confirmation.destroy)
        self.cancel_button.grid(row=1, column=1)
        self.confirmation.focus_set()
        self.confirmation.grab_set()
        self.confirmation.mainloop()





app = Invoice()
app.geometry("800x480")
app.title("Invoice")
app.mainloop()
