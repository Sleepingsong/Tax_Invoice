from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import font
from PIL import Image,ImageTk
from requests import Session
import zeep
from zeep import Client
from zeep.transports import Transport
import urllib3
import time

LARGE_FONT = ("Verdana",12)


class Invoice( tk.Tk ):

	def __init__(self,*args,**kwargs):
		tk.Tk.__init__( self,*args,**kwargs )
		container = tk.Frame( self )

		container.grid()
		container.grid_rowconfigure( 0,weight = 1 )
		container.grid_columnconfigure( 0,weight = 1 )

		self.frames = { }

		for F in (StartPage,PageOne,PageTwo,PageThree):
			frame = F( container,self )
			self.frames[F] = frame
			frame.grid( row = 0,column = 0,sticky = "NSEW" )

		self.show_frame( StartPage )

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage( tk.Frame ):  # Calculate Price

	db_name = 'MyDatabase.db'

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )

		AFont = font.Font( family = 'Helvetica',size = 12,weight = 'bold' )
		BFont = font.Font( family = 'Helvetica',size = 11,)
		self.on_color = 'red'
		self.off_color = 'black'

		frame = ttk.LabelFrame( self,text = 'สินค้า' )
		frame.grid( row = 0,column = 0,sticky = W )
		frame7 = ttk.LabelFrame( self,text = 'ราคาน้ำมัน ณ ปัจจุบัน' )
		frame7.grid( row = 1,sticky = NW )
		frame8 = ttk.LabelFrame( self,text = 'ชุดคำสั่ง' )
		frame8.grid( row = 0,column = 1,sticky = NW )
		frame9 = ttk.LabelFrame( self,text = "คำนวณเงิน" )
		frame9.grid( row = 1,column = 0,sticky = NE )
		frame10 = ttk.LabelFrame( self,text = "ผู้ซื้อ" )
		frame10.grid( row = 2,column = 0,sticky = W )
		frame11 = ttk.LabelFrame(self, text = "รหัสประจำตัวผู้เสียภาษี")
		frame11.grid(row = 2, column = 1,sticky = W)

		self.chk1 = BooleanVar()
		self.chk2 = BooleanVar()
		self.chk3 = BooleanVar()
		self.chk4 = BooleanVar()
		self.chk5 = BooleanVar()
		self.chk6 = BooleanVar()

		# load1 = Image.open("Gasohol95.jpg")
		# load1 = load1.resize((150,60), Image.ANTIALIAS)
		# render = ImageTk.PhotoImage(load1)
		# img1 = Label(frame, image=render)
		# img1.image = render
		# img1.grid(row = 0)
		self.image1 = Image.open( "Gasohol95.jpg" )
		self.image1 = self.image1.resize( (150,60),Image.ANTIALIAS )
		self.photo1 = ImageTk.PhotoImage( self.image1 )
		self.G95_button = tk.Button( frame,image = self.photo1,height = 60,width = 150,command = self.checkG95 )
		self.G95_button.grid( row = 0 )

		self.Product1 = Checkbutton( frame,text = "Supreme Gasohol 95",font = AFont, variable = self.chk1 , fg = self.off_color)
		self.Product1.grid( row = 1,column = 0 )

		# load2 = Image.open("Gasohol95_Plus.jpg")
		# load2 = load2.resize((150,60), Image.ANTIALIAS)
		# render = ImageTk.PhotoImage(load2)
		# img2 = Label(frame, image=render)
		# img2.image = render
		# img2.grid(row = 0, column = 1)
		self.image2 = Image.open( "Gasohol95_Plus.jpg" )
		self.image2 = self.image2.resize( (150,60),Image.ANTIALIAS )
		self.photo2 = ImageTk.PhotoImage( self.image2 )
		self.GP95_button = tk.Button( frame,image = self.photo2,height = 60,width = 150,command = self.checkGP95 )
		self.GP95_button.grid( row = 0,column = 1 )
		self.Product2 = Checkbutton( frame,text = "Supreme Plus Gasohol 95",font = AFont,variable = self.chk2, fg = self.off_color)
		self.Product2.grid( row = 1,column = 1 )

		# load3 = Image.open("Gasohol_E20.jpg")
		# load3 = load3.resize((150,60), Image.ANTIALIAS)
		# render = ImageTk.PhotoImage(load3)
		# img3 = Label(frame, image=render)
		# img3.image = render
		# img3.grid(row = 0, column = 2)
		self.image3 = Image.open( "Gasohol_E20.jpg" )
		self.image3 = self.image3.resize( (150,60),Image.ANTIALIAS )
		self.photo3 = ImageTk.PhotoImage( self.image3 )
		self.E20_button = tk.Button( frame,image = self.photo3,height = 60,width = 150,command = self.checkE20 )
		self.E20_button.grid( row = 0,column = 2 )
		self.Product3 = Checkbutton( frame,text = "Supreme E20",font = AFont,variable = self.chk3 , fg = self.off_color)
		self.Product3.grid( row = 1,column = 2 )

		# load4 = Image.open("Gasohol_91.jpg")
		# load4 = load4.resize((150,60), Image.ANTIALIAS)
		# render = ImageTk.PhotoImage(load4)
		# img4 = Label(frame, image=render)
		# img4.image = render
		# img4.grid(row = 2,column = 0)
		self.image4 = Image.open( "Gasohol_91.jpg" )
		self.image4 = self.image4.resize( (150,60),Image.ANTIALIAS )
		self.photo4 = ImageTk.PhotoImage( self.image4 )
		self.G91_button = tk.Button( frame,image = self.photo4,height = 60,width = 150,command = self.checkG91 )
		self.G91_button.grid( row = 2,column = 0 )
		self.Product4 = Checkbutton( frame,text = "Supreme Gasohol 91",font = AFont,variable = self.chk4 , fg = self.off_color)
		self.Product4.grid( row = 3,column = 0 )

		# load5 = Image.open("Diesel_Plus.jpg")
		# load5 = load5.resize((150,60), Image.ANTIALIAS)
		# render = ImageTk.PhotoImage(load5)
		# img5 = Label(frame, image=render)
		# img5.image = render
		# img5.grid(row = 2, column = 1)
		self.image5 = Image.open( "Diesel_Plus.jpg" )
		self.image5 = self.image5.resize( (150,60),Image.ANTIALIAS )
		self.photo5 = ImageTk.PhotoImage( self.image5 )
		self.DSP_button = tk.Button( frame,image = self.photo5,height = 60,width = 150,command = self.checkDSP )
		self.DSP_button.grid( row = 2,column = 1 )
		self.Product5 = Checkbutton( frame,text = "Supreme Plus Diesel",font = AFont,variable = self.chk5 , fg = self.off_color)
		self.Product5.grid( row = 3,column = 1 )

		# load6 = Image.open("Diesel.jpg")
		# load6 = load6.resize((150,60), Image.ANTIALIAS)
		# render = ImageTk.PhotoImage(load6)
		# img6 = Label(frame, image=render)
		# img6.image = render
		# img6.grid(row = 2, column = 2)
		self.image6 = Image.open( "Diesel.jpg" )
		self.image6 = self.image6.resize( (150,60),Image.ANTIALIAS )
		self.photo6 = ImageTk.PhotoImage( self.image6 )
		self.DS_button = tk.Button( frame,image = self.photo6,height = 60,width = 150,command = self.checkDS )
		self.DS_button.grid( row = 2,column = 2 )
		self.Product6 = Checkbutton( frame,text = "Supreme Diesel",font = AFont,variable = self.chk6 , fg = self.off_color)
		self.Product6.grid( row = 3,column = 2 )

		Label( frame7,text = 'Supreme Gasohol 95 :',font = BFont ).grid( row = 0,column = 0,sticky = E )
		Label( frame7,text = 'บาท',font = BFont ).grid( row = 0,column = 2 )
		self.G95_price = Entry( frame7,width = 8,justify = 'right' )
		self.G95_price.grid( row = 0,column = 1 )

		Label( frame7,text = 'Supreme Plus Gasohol 95 :',font = BFont ).grid( row = 1,column = 0,sticky = E )
		Label( frame7,text = 'บาท',font = BFont ).grid( row = 1,column = 2 )
		self.GP95_price = Entry( frame7,width = 8,justify = 'right' )
		self.GP95_price.grid( row = 1,column = 1 )

		Label( frame7,text = 'Supreme E20 :',font = BFont ).grid( row = 2,column = 0,sticky = E )
		Label( frame7,text = 'บาท',font = BFont ).grid( row = 2,column = 2 )
		self.E20_price = Entry( frame7,width = 8,justify = 'right' )
		self.E20_price.grid( row = 2,column = 1 )

		Label( frame7,text = 'Supreme Gasohol 91 :',font = BFont ).grid( row = 3,column = 0,sticky = E )
		Label( frame7,text = 'บาท',font = BFont ).grid( row = 3,column = 2 )

		self.G91_price = Entry( frame7,width = 8,justify = 'right' )
		self.G91_price.grid( row = 3,column = 1 )

		Label( frame7,text = 'Supreme Diesel :',font = BFont ).grid( row = 4,column = 0,sticky = E )
		Label( frame7,text = 'บาท',font = BFont ).grid( row = 4,column = 2 )
		self.DS_price = Entry( frame7,width = 8,justify = 'right' )
		self.DS_price.grid( row = 4,column = 1 )

		Label( frame7,text = 'Supreme Plus Diesel :',font = BFont ).grid( row = 5,column = 0,sticky = E )
		Label( frame7,text = 'บาท',font = BFont ).grid( row = 5,column = 2 )
		self.DSP_price = Entry( frame7,width = 8,justify = 'right' )
		self.DSP_price.grid( row = 5,column = 1 )

		Label( frame9,text = 'จำนวนลิตร',font = BFont ).grid( row = 0,column = 0 )
		Label( frame9,text = 'ลิตร',font = BFont ).grid( row = 0,column = 2 )
		self.product_liter = Entry( frame9,justify = 'right' )
		self.product_liter.grid( row = 0,column = 1 )
		Label( frame9,text = 'ยอดทั้งหมด',font = BFont ).grid( row = 1,column = 0 )
		Label( frame9,text = 'บาท',font = BFont ).grid( row = 1,column = 2 )
		self.total_price = Entry( frame9,justify = 'right' )
		self.total_price.grid( row = 1,column = 1 )


		# Label( frame11,text = "รหัสประจำตัวผู้เสียภาษี",font = BFont ).grid( row = 0 )
		Label(frame10, text = "ชื่อบริษัท").grid(row=1,column = 0,sticky = E)
		self.comp_name = Entry(frame10,justify = 'right',width = 17)
		self.comp_name.grid(row =1 , column = 1,sticky = W)
		Label(frame10,text= "สาขา").grid(row =1 , column = 2,sticky = E)
		self.branch_num = Entry(frame10,justify = 'right',width = 5)
		self.branch_num.grid(row =1 , column = 3,sticky = W)
		Label(frame10,text="ชื่อตึก").grid(row =1 , column = 4,sticky = E)
		self.building_name = Entry(frame10, justify='right',width =17)
		self.building_name.grid(row=1, column=5,sticky = W)
		Label(frame10,text= "ชั้น").grid(row=1, column = 6,sticky = E)
		self.branch_floor = Entry(frame10, justify='right',width = 8)
		self.branch_floor.grid(row=1, column=7,sticky = W)
		Label(frame10, text="หมู่บ้าน").grid(row=2,column=0,sticky = E)
		self.village_name = Entry(frame10, justify='right',width = 17)
		self.village_name.grid(row=2, column=1,sticky = W)
		Label(frame10, text="เลขห้อง").grid(row=2,column = 2 ,sticky = E)
		self.room_no = Entry(frame10, justify='right', width=5)
		self.room_no.grid(row=2, column=3,sticky =W)
		Label(frame10, text="เลขที่บ้าน").grid(row=2, column=4,sticky = E)
		self.house_no = Entry(frame10, justify='right', width=5)
		self.house_no.grid(row=2, column=5,sticky = W)
		Label(frame10, text="หมู่").grid(row=2, column=6, sticky = E)
		self.Moo_no = Entry(frame10, justify='right', width=8)
		self.Moo_no.grid(row=2, column=7,sticky = W)
		Label(frame10, text="ซอย").grid(row=3,column = 0,sticky = E)
		self.Soi_no = Entry(frame10, justify='right',width = 10)
		self.Soi_no.grid(row=3, column=1,sticky =W)
		Label(frame10, text="ถนน").grid(row=3, column=2,sticky = E)
		self.Stree_name = Entry(frame10, justify='right',width = 17)
		self.Stree_name.grid(row=3, column=3,sticky =W)
		Label(frame10, text="ตำบล").grid(row=3, column = 4,sticky = E)
		self.Thumbon_name = Entry(frame10, justify='right', width=17)
		self.Thumbon_name.grid(row=3, column=5, sticky=W)
		Label(frame10, text="อำเภอ").grid(row=3, column = 6, sticky=E)
		self.Aumper_name = Entry(frame10, justify='right', width=8)
		self.Aumper_name.grid(row=3, column=7, sticky=W)
		Label(frame10, text="จังหวัด").grid(row=4, column=0,sticky=E)
		self.Province_name = Entry(frame10, justify='right', width=17)
		self.Province_name.grid(row=4, column=1, sticky=W)
		Label(frame10, text="รหัสไปษณีย์").grid(row=4, column = 2,sticky=E)
		self.Postcode = Entry(frame10, justify='right', width=5)
		self.Postcode.grid(row=4, column=3, sticky=W)


		self.cus_list = Listbox(frame11, height = 5, selectmode=SINGLE)
		self.cus_list.bind('<Double-Button>', self.show_data)
		self.cus_list.grid(row = 1)
		db = sqlite3.connect( 'MyDatabase.db' )
		cursor = db.execute( 'SELECT Tax_ID FROM Customer' )
		for row in cursor.fetchall():
			self.cus_list.insert(END, row)


		# button1 = ttk.Button( frame10,text = "ดูข้อมูลเพิ่มเติม",width = 15,command = lambda: self.show_cus_name() )
		# button1.grid( row = 0,column = 2 )
		# Label( frame10,text = "รหัสประจำตัว",font = BFont ).grid( row = 1 )
		# Label( frame10,text = "ทะเบียนรถ",font = BFont ).grid( row = 2 )
		# self.invoice_id = ttk.Entry( frame10 ).grid( row = 1,column = 1,sticky = W )
		# self.car_plate = ttk.Entry( frame10 ).grid( row = 2,column = 1,sticky = W )
		# Label( frame10,text = "ชื่อ",font = BFont ).grid( row = 1,column = 2,sticky = W )
		# self.c_name = ttk.Entry( frame10 ).grid( row = 1,column = 2,sticky = E )
		# Label( frame10,text = "เบอร์โทรศัพท์",font = BFont ).grid( row = 1,column = 3 )
		# self.phone_num = ttk.Entry( frame10 ).grid( row = 1,column = 4 )
		# Label( frame10,text = "ที่อยู่",font = BFont ).grid( row = 2,column = 2,sticky = W )
		# self.c_address = ttk.Entry( frame10,width = 55 ).grid( row = 2,column = 2,columnspan = 3,sticky = E )

		button4 = ttk.Button( frame9,text = "คำนวณราคา",command = self.CalPrice )
		button4.grid( row = 2,columnspan = 3 )
		button4 = ttk.Button( frame9,text = "ยกเลิก",command = self.Clear )
		button4.grid( row = 3,columnspan = 3 )

		button3 = ttk.Button( frame8,text = "ข้อมูลลูกค้า",command = lambda: controller.show_frame( PageTwo ),
							  width = 15 )
		button3.grid( row = 2,column = 0,)
		button3 = ttk.Button( frame8,text = "ข้อมูลสินค้า",command = lambda: controller.show_frame( PageOne ),
							  width = 15 )
		button3.grid( row = 1,column = 0,)
		button3 = ttk.Button( frame8,text = "คำนวณสินค้าเพิ่มเติม",command = lambda: controller.show_frame( PageThree ),
							  width = 15 )
		button3.grid( row = 0,column = 0,)

		self.Show_gas_price()






	# def show_cus_name(self):
	#
	# 	con = sqlite3.connect( 'MyDatabase.db' )
	# 	cur = con.cursor()
	# 	cur.execute( 'SELECT Customer_Name FROM Customer WHERE Customer_Name = ?',self.product_name.get() )
	# 	# self.c_name.insert(END,cur.fetchall())
	# 	print( cur.fetchall() )


	def show_data(self,event):

		self.comp_name.delete(0,'end')
		self.branch_num.delete(0,'end')
		self.branch_floor.delete(0,'end')
		self.building_name.delete(0,'end')
		self.village_name.delete(0,'end')
		self.house_no.delete(0,'end')
		self.Moo_no.delete(0,'end')
		self.Soi_no.delete(0,'end')
		self.Stree_name.delete(0,'end')
		self.Thumbon_name.delete(0,'end')
		self.Aumper_name.delete(0,'end')
		self.Province_name.delete(0,'end')
		self.Postcode.delete(0,'end')

		self.get_selecte_value = self.cus_list.get(self.cus_list.curselection())
		con = sqlite3.connect('MyDatabase.db')
		cur = con.cursor()
		cur.execute('SELECT Name FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
		self.comp_name.insert(END,cur.fetchone())

		cur2 = con.cursor()
		cur2.execute('SELECT BranchNumber FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
		self.branch_num.insert(END,cur2.fetchall())

		cur3 = con.cursor()
		cur3.execute('SELECT BuildingName FROM Customer WHERE Tax_ID = ?', self.get_selecte_value)
		self.building_name.insert(END, cur3.fetchall())

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
		self.Soi_no.insert(END, cur8.fetchone())

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

	def Show_gas_price(self):

		con = sqlite3.connect( 'MyDatabase.db' )
		cur1 = con.cursor()
		cur1.execute( 'SELECT Product_Price FROM Product WHERE Product_ID = 1' )
		self.G95_price.insert(END,cur1.fetchall())

		cur2 = con.cursor()
		cur2.execute( 'SELECT Product_Price FROM Product WHERE Product_ID = 26' )
		self.GP95_price.insert( END,cur2.fetchall() )

		cur3 = con.cursor()
		cur3.execute( 'SELECT Product_Price FROM Product WHERE Product_ID = 27' )
		self.E20_price.insert( END,cur3.fetchall() )

		cur4 = con.cursor()
		cur4.execute( 'SELECT Product_Price FROM Product WHERE Product_ID = 28' )
		self.G91_price.insert( END,cur4.fetchall() )

		cur5 = con.cursor()
		cur5.execute( 'SELECT Product_Price FROM Product WHERE Product_ID = 29' )
		self.DS_price.insert( END,cur5.fetchall() )

		cur6 = con.cursor()
		cur6.execute( 'SELECT Product_Price FROM Product WHERE Product_ID = 30' )
		self.DSP_price.insert( END,cur6.fetchall() )

	def checkG95(self):
		if self.chk1.get() == False:
			self.chk1.set( True )
			self.Product1["fg"] = self.on_color
		else:
			self.chk1.set( False )
			self.Product1["fg"] = self.off_color

	def checkGP95(self):
		if self.chk2.get() == False:
			self.chk2.set( True )
			self.Product2["fg"] = self.on_color
		else:
			self.chk2.set( False )
			self.Product2["fg"] = self.off_color

	def checkE20(self):
		if self.chk3.get() == False:
			self.chk3.set( True )
			self.Product3["fg"] = self.on_color
		else:
			self.chk3.set( False )
			self.Product3["fg"] = self.off_color

	def checkG91(self):
		if self.chk4.get() == False:
			self.chk4.set( True )
			self.Product4["fg"] = self.on_color
		else:
			self.chk4.set( False )
			self.Product4["fg"] = self.off_color

	def checkDSP(self):
		if self.chk5.get() == False:
			self.chk5.set( True )
			self.Product5["fg"] = self.on_color
		else:
			self.chk5.set( False )
			self.Product5["fg"] = self.off_color

	def checkDS(self):
		if self.chk6.get() == False:
			self.chk6.set( True )
			self.Product6["fg"] = self.on_color
		else:
			self.chk6.set( False )
			self.Product6["fg"] = self.off_color

	def CalPrice(self):

		if self.chk1.get() == True:
			if not self.total_price.get():
				price = float( self.product_liter.get() ) * float( self.G95_price.get() )
				self.total_price.insert( END,round( price,3 ) )

			else:
				liter = float( self.total_price.get() ) / float( self.G95_price.get() )
				self.product_liter.insert( END,round( liter,3 ) )

		if self.chk2.get() == True:
			if not self.total_price.get():
				price = float( self.product_liter.get() ) * float( self.GP95_price.get() )
				self.total_price.insert( END,round( price,3 ) )

			else:
				liter = float( self.total_price.get() ) / float( self.GP95_price.get() )
				self.product_liter.insert( END,round( liter,3 ) )
		if self.chk3.get() == True:
			if not self.total_price.get():
				price = float( self.product_liter.get() ) * float( self.E20_price.get() )
				self.total_price.insert( END,round( price,3 ) )

			else:
				liter = float( self.total_price.get() ) / float( self.E20_price.get() )
				self.product_liter.insert( END,round( liter,3 ) )
		if self.chk4.get() == True:
			if not self.total_price.get():
				price = float( self.product_liter.get() ) * float( self.G91_price.get() )
				self.total_price.insert( END,round( price,3 ) )

			else:
				liter = float( self.total_price.get() ) / float( self.G91_price.get() )
				self.product_liter.insert( END,round( liter,3 ) )
		if self.chk5.get() == True:
			if not self.total_price.get():
				price = float( self.product_liter.get() ) * float( self.DSP_price.get() )
				self.total_price.insert( END,round( price,3 ) )

			else:
				liter = float( self.total_price.get() ) / float( self.DSP_price.get() )
				self.product_liter.insert( END,round( liter,3 ) )
		if self.chk6.get() == True:
			if not self.total_price.get():
				price = float( self.product_liter.get() ) * float( self.DS_price.get() )
				self.total_price.insert( END,round( price,3 ) )

			else:
				liter = float( self.total_price.get() ) / float( self.DS_price.get() )
				self.product_liter.insert( END,round( liter,3 ) )

	def Clear(self):
		self.product_liter.delete( 0,END )
		self.total_price.delete( 0,END )

	def list_customer(self):
		db = sqlite3.connect( 'MyDatabase.db' )
		cursor = db.execute( 'SELECT Tax_ID FROM Customer ORDER BY Tax_ID DESC' )

		for row in cursor.fetchall():
			self.cus_list.insert(END, row)


class PageOne( tk.Frame):  # Product Page

	db_name = 'MyDatabase.db'

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )
		frame = ttk.LabelFrame( self,text = 'เพิ่มสินค้า' )
		frame.grid( row = 0,column = 0,sticky = NW )

		style = ttk.Style( self )
		style.configure( "TButton",font = ('wasy10',14) )

		Label( frame,text = 'ชื่อสินค้า' ).grid( row = 1,column = 0 )
		self.name = Entry( frame )
		self.name.grid( row = 1,column = 1 )

		Label( frame,text = 'ประเภทสินค้า' ).grid( row = 2,column = 0 )
		self.type = Entry( frame,justify = 'right' )
		self.type.grid( row = 2,column = 1 )

		Label( frame,text = 'ราคา' ).grid( row = 3,column = 0 )
		self.price = Entry( frame,justify = 'right' )
		self.price.grid( row = 3,column = 1 )

		ttk.Button( frame,text = 'เพิ่มข้อมูล',command = self.adding ).grid( row = 4,column = 0 )
		button1 = ttk.Button( frame,text = 'ลบข้อมูล',command = self.deleting )
		button1.grid( row = 4,column = 1 )
		button2 = ttk.Button( frame,text = 'แก้ไขข้อมูล',command = self.editing )
		button2.grid( row = 4,column = 2 )

		self.tree = ttk.Treeview( self,height = 15,column = ("2","3") )
		self.tree.grid( row = 1,column = 0 )
		self.tree.heading( '#0',text = 'ชื่อสินค้า',anchor = W )
		self.tree.heading( 0,text = 'ประเภทสินค้า',anchor = W )
		self.tree.heading( 1,text = 'ราคา',anchor = W )

		frame2 = LabelFrame( self,text = 'ชุดคำสั่ง' )
		frame2.grid( row = 0,column = 0,sticky = E )

		button3 = ttk.Button( frame2,text = "หน้าข้อมูลลูกค้า",command = lambda: controller.show_frame( PageTwo ) )
		button3.grid( row = 1,column = 0,)
		button3 = ttk.Button( frame2,text = "หน้าคำนวณสินค้า",command = lambda: controller.show_frame( StartPage ) )
		button3.grid( row = 0,column = 0,)

		self.viewing_record()

	def run_query(self,query,parameters=()):
		with sqlite3.connect( self.db_name ) as conn:
			cursor = conn.cursor()
			query_result = cursor.execute( query,parameters )
			conn.commit()
		return query_result

	def viewing_record(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete( element )
		query = 'SELECT * FROM Product ORDER BY Product_ID DESC'
		db_rows = self.run_query( query )
		for row in db_rows:
			self.tree.insert( '',0,text = row[1],values = (row[2],row[3]) )


	def validation(self):
		return len( self.name.get() ) != 0 and len( self.type.get() ) != 0 and len( self.price.get() ) != 0

	def adding(self):
		if self.validation():
			query = 'INSERT INTO Product VALUES (NULL, ?, ?,?)'
			parameters = (self.name.get(),self.type.get(),self.price.get())
			self.run_query( query,parameters )
			self.message['text'] = 'Record {} added to database'.format( self.name.get() )
			self.name.delete( 0,END )
			self.type.delete( 0,END )
			self.price.delete( 0,END )
		else:
			self.message['text'] = 'name field or price field is empty'
		self.viewing_record()

	def deleting(self):
		self.message['text'] = ''
		try:
			self.tree.item( self.tree.selection() )['values'][0]
		except IndexError as e:
			self.message['text'] = 'Please select record'
			return

		self.message['text'] = ''
		name = self.tree.item( self.tree.selection() )['text']
		query = 'DELETE FROM Product WHERE Product_Name = ?'
		self.run_query( query,(name,) )
		self.message['text'] = 'Record {} is deleted'.format( name )
		self.viewing_record()

	def editing(self):
		try:
			self.tree.item( self.tree.selection() )['values'][1]
		except IndexError as e:
			self.message['text'] = 'Please select record'
			return

		# name = self.tree.item( self.tree.selection() )['text']
		old_price = self.tree.item( self.tree.selection() )['values'][1]

		self.edit_main = Toplevel()
		self.edit_main.title( 'Editing' )

		# Label( self.edit_main,text = 'Old name: ' ).grid( row = 0,column = 1 )
		# Entry( self.edit_main,textvariable = StringVar( self.edit_main,value = name ),state = 'readonly' ).grid(
		# 	row = 0,column = 2 )
		# Label( self.edit_main,text = 'New name: ' ).grid( row = 1,column = 1 )
		# new_name = Entry( self.edit_main )
		# new_name.grid( row = 1,column = 2 )

		Label( self.edit_main,text = 'Old Price: ' ).grid( row = 2,column = 1 )
		Entry( self.edit_main,textvariable = StringVar( self.edit_main,value = old_price ),state = 'readonly' ).grid(
			row = 2,column = 2 )
		Label( self.edit_main,text = 'New price: ' ).grid( row = 3,column = 1 )
		new_price = Entry( self.edit_main )
		new_price.grid( row = 3,column = 2 )

		Button( self.edit_main,text = 'Save Change',
				command = lambda: self.edit_record(new_price.get(),old_price ) ).grid( row = 4,
																											column = 2,
																											sticky = W )

		self.edit_main.mainloop()

	def edit_record(self,new_price,old_price):
		query = 'UPDATE Product SET Product_Price = ? WHERE Product_Price = ?'
		paremeters = (new_price,old_price)
		self.run_query( query,paremeters )
		self.edit_main.destroy()
		self.viewing_record()


class PageTwo( tk.Frame ):  # Customer Page

	db_name = 'MyDatabase.db'

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )
		AFont = font.Font( family = 'Helvetica',size = 12,weight = 'bold' )
		BFont = font.Font( family = 'Helvetica',size = 11,)
		frame =LabelFrame(self,text = "ค้นหา")
		frame.grid(row = 0, sticky = NW)

		default = StringVar(self, value = 0)
		Label(frame, text = "เลขประจำตัวผู้เสียภาษีอากร (13 หลัก)",font = BFont).grid(row = 0)
		Label(frame, text = "สาขาที่",font = BFont).grid(row = 1,sticky = E)
		self.tax_enter = Entry( frame )
		self.tax_enter.grid( row = 0,column = 1,sticky = W )
		self.branch_enter = Entry(frame, textvariable = default)
		self.branch_enter.grid(row = 1, column = 1,sticky = W)
		self.button1 = Button( frame,text = 'ค้นหา',font = AFont,height = 1,width = 10,command = lambda: self.tax_search() )
		self.button1.grid( row = 2,column = 1)
		self.button2 = Button( frame,text = 'บันทึก',font = AFont,height = 1,width = 10, command = self.save_data)
		self.button2.grid( row = 2,sticky = E)

		self.tree = ttk.Treeview( self,height = 17,column = ("1") )
		self.tree.heading( '#0',text = "ประเภท" )
		self.tree.heading( 0,text = "ผลลัพธ์" )
		self.tree.grid( row = 1 )

		frame2 = LabelFrame( self,text = "ชุดคำสั่ง" )
		frame2.grid( row = 0,column = 1,sticky = E )

		self.my_list = []

		#
		# Label( frame2,text = 'ชื่อลูกค้า' ).grid( row = 1,column = 2 )
		# self.Customer_name = Entry( frame2,justify='right'  )
		# self.Customer_name.grid( row = 1,column = 3 )
		#
		# Label( frame2,text = 'ทะเบียนรถ' ).grid( row = 1,column = 4 )
		# self.Car_plate = Entry( frame2,justify='right'  )
		# self.Car_plate.grid( row = 1,column = 5 )
		#
		# Label( frame2,text = 'ชื่อบริษัท' ).grid( row = 3,column = 2 )
		# self.Company_name = Entry( frame2,justify='right'  )
		# self.Company_name.grid( row = 3,column = 3 )
		#
		# Label( frame2,text = 'เบอร์โทรศัพท์' ).grid( row = 2,column = 2 )
		# self.Phone_number = Entry( frame2,justify='right'  )
		# self.Phone_number.grid( row = 2,column = 3 )
		#
		# Label( frame2,text = 'ที่อยู่' ).grid( row = 2,column = 4 )
		# self.Customer_address = Entry( frame2 ,justify='right' )
		# self.Customer_address.grid( row = 2,column = 5 )
		#
		# ttk.Button( frame2,text = 'เพิ่มข้อมูล',command = self.adding2 ).grid( row = 4,column = 2 )
		# button1 = ttk.Button( frame2,text = 'ลบข้อมูล',command = self.deleting2 )
		# button1.grid( row = 4,column = 3 )
		# button2 = ttk.Button( frame2,text = 'แก้ไขข้อมูล' )
		# button2.grid( row = 4,column = 4 )
		#
		# self.tree2 = ttk.Treeview( self,height = 15,column = ("1","2","3") )
		# self.tree2.grid( row = 2,column = 0)
		# self.tree2.heading( '#0',text = 'ชื่อลูกค้า',anchor = W )
		# self.tree2.heading( 1,text = 'ทะเบียนรถ',anchor = W )
		# self.tree2.heading( 2,text = 'ชื่อบริษัท',anchor = W )
		# self.tree2.heading( 3,text = 'เบอร์โทรศัพท์',anchor = W )
		#
		# frame2 = LabelFrame(self, text = 'ชุดคำสั่ง')
		# frame2.grid(row = 0, column = 0, sticky = E)

		button3 = ttk.Button( frame2,text = "หน้าข้อมูลสินค้า",command = lambda: controller.show_frame( PageOne ) )
		button3.grid( row = 1,column = 0,)
		button3 = ttk.Button( frame2,text = "หน้าคำนวณสินค้า",command = lambda: controller.show_frame( StartPage ) )
		button3.grid( row = 0,column = 0,)

	# self.viewing_record2()

	def tax_search(self):

		count = True
		while count:
			try:
				for i in self.tree.get_children():
					self.tree.delete(i)
				self.my_list.clear()
				urllib3.disable_warnings( urllib3.exceptions.InsecureRequestWarning )
				session = Session()
				session.verify = False
				transport = Transport( session = session )

				client = Client( 'https://rdws.rd.go.th/serviceRD3/vatserviceRD3.asmx?wsdl',
								 transport = transport )
				result = client.service.Service(
					username = 'anonymous',
					password = 'anonymous',
					TIN = self.tax_enter.get(),
					ProvinceCode = 0,
					BranchNumber = self.branch_enter.get(),
					AmphurCode = 0
				)

				# Convert Zeep Response object (in this case Service) to Python dict.
				result = zeep.helpers.serialize_object( result )

				# print(result)
				for k in result.keys():
					if result[k] is not None:
						v = result[k].get( 'anyType',None )[0]
						self.tree.insert( '','end',text = k,value = v )
						self.my_list.append(v)

			except:
				time.sleep(3)
				print("Try Again")
			else:
				count = False



	def save_data(self):
		try:
			conn = sqlite3.connect('MyDatabase.db')
			c = conn.cursor()
			c.execute('INSERT INTO Customer VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', self.my_list)
			conn.commit()
		except:
			print('Something wrong')





# def run_query(self,query,parameters=()):
	# 	with sqlite3.connect( self.db_name ) as conn:
	# 		cursor = conn.cursor()
	# 		query_result = cursor.execute( query,parameters )
	# 		conn.commit()
	# 	return query_result
	#
	# def viewing_record2(self):
	# 	records = self.tree2.get_children()
	# 	for element in records:
	# 		self.tree2.delete( element )
	# 	query = 'SELECT * FROM Customer ORDER BY Customer_ID DESC'
	# 	db_rows = self.run_query( query )
	# 	for row in db_rows:
	# 		self.tree2.insert( '',0,text = row[1],values = (row[2],row[3],row[4]) )
	#
	# def validation2(self):
	# 	return len( self.Customer_name.get() ) != 0 \
	# 		   and len( self.Company_name.get() ) != 0 and len( self.Car_plate.get() ) != 0 \
	# 		   and len( self.Phone_number.get() ) != 0
	#
	# def adding2(self):
	# 	if self.validation2():
	# 		query = 'INSERT INTO Customer VALUES (NULL, ?, ?,?,?,?)'
	# 		parameters = (
	# 			self.Customer_name.get(),self.Phone_number.get(),self.Car_plate.get(),self.Company_name.get(),
	# 			self.Customer_address.get())
	# 		self.run_query( query,parameters )
	# 		self.message2['text'] = 'Record {} added to database'.format( self.Company_name.get() )
	# 		self.Customer_name.delete( 0,END )
	# 		self.Car_plate.delete( 0,END )
	# 		self.Company_name.delete( 0,END )
	# 		self.Phone_number.delete( 0,END )
	#
	# 	else:
	# 		self.message2['text'] = 'Some fields are empty'
	# 	self.viewing_record2()
	#
	# def deleting2(self):
	# 	self.message2['text'] = ''
	# 	try:
	# 		self.tree2.item( self.tree2.selection() )['values'][0]
	# 	except IndexError as e:
	# 		self.message2['text'] = 'Please select record'
	# 		return
	#
	# 	self.message2['text'] = ''
	# 	name = self.tree2.item( self.tree2.selection() )['text']
	# 	query = 'DELETE FROM Customer WHERE Customer_Name = ?'
	# 	self.run_query( query,(name,) )
	# 	self.message2['text'] = 'Record {} is deleted'.format( name )
	# 	self.viewing_record2()


class PageThree( tk.Frame ):  # CalPrice

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )

		frame = ttk.LabelFrame( self,text = 'สินค้าทั้งหมด' )
		frame.grid( row = 0,column = 0,sticky = NW )

		Label( frame,text = "ชื่อสินค้า" ).grid( row = 1,sticky = W )
		self.product_name = ttk.Combobox( frame,width = 40,justify = 'right' )
		self.product_name['values'] = self.combo_product()
		self.product_name.grid( row = 2,column = 0 )
		self.product_name2 = ttk.Combobox( frame,width = 40,justify = 'right' )
		self.product_name2['values'] = self.combo_product()
		self.product_name2.grid( row = 3,column = 0 )
		self.product_name3 = ttk.Combobox( frame,width = 40,justify = 'right' )
		self.product_name3['values'] = self.combo_product()
		self.product_name3.grid( row = 4,column = 0 )
		self.product_name4 = ttk.Combobox( frame,width = 40,justify = 'right' )
		self.product_name4['values'] = self.combo_product()
		self.product_name4.grid( row = 5,column = 0 )
		self.product_name5 = ttk.Combobox( frame,width = 40,justify = 'right' )
		self.product_name5['values'] = self.combo_product()
		self.product_name5.grid( row = 6,column = 0 )
		self.product_name6 = ttk.Combobox( frame,width = 40,justify = 'right' )
		self.product_name6['values'] = self.combo_product()
		self.product_name6.grid( row = 7,column = 0 )

		# Label( frame,text = "ประเภทสินค้า" ).grid( row = 1,column = 1,sticky = W )
		# self.product_type = ttk.Combobox(frame, width = 20, state='readonly')
		# self.product_type['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		# self.product_type.grid( row = 2,column = 1 )
		# self.product_type2 = ttk.Combobox(frame, width = 20, state='readonly')
		# self.product_type2['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		# self.product_type2.grid( row = 3,column = 1 )
		# self.product_type3 = ttk.Combobox(frame, width = 20, state='readonly')
		# self.product_type3['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		# self.product_type3.grid( row = 4,column = 1 )
		# self.product_type4 = ttk.Combobox(frame, width = 20, state='readonly')
		# self.product_type4['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		# self.product_type4.grid( row = 5,column = 1 )
		# self.product_type5 = ttk.Combobox(frame, width = 20, state='readonly')
		# self.product_type5['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		# self.product_type5.grid( row = 6,column = 1 )
		# self.product_type6 = ttk.Combobox(frame, width = 20, state='readonly')
		# self.product_type6['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		# self.product_type6.grid( row = 7,column = 1 )

		Label( frame,text = "ราคา(บาท)" ).grid( row = 1,column = 1,sticky = W )
		self.product_price = Entry( frame,width = 10,justify = 'right' )
		self.product_price.grid( row = 2,column = 1 )
		self.product_price2 = Entry( frame,width = 10,justify = 'right' )
		self.product_price2.grid( row = 3,column = 1 )
		self.product_price3 = Entry( frame,width = 10,justify = 'right' )
		self.product_price3.grid( row = 4,column = 1 )
		self.product_price4 = Entry( frame,width = 10,justify = 'right' )
		self.product_price4.grid( row = 5,column = 1 )
		self.product_price5 = Entry( frame,width = 10,justify = 'right' )
		self.product_price5.grid( row = 6,column = 1 )
		self.product_price6 = Entry( frame,width = 10,justify = 'right' )
		self.product_price6.grid( row = 7,column = 1 )

		Label( frame,text = "จำนวน" ).grid( row = 1,column = 2,sticky = W )
		self.product_number = Entry( frame,width = 10,justify = 'right' )
		self.product_number.grid( row = 2,column = 2 )
		self.product_number2 = Entry( frame,width = 10,justify = 'right' )
		self.product_number2.grid( row = 3,column = 2 )
		self.product_number3 = Entry( frame,width = 10,justify = 'right' )
		self.product_number3.grid( row = 4,column = 2 )
		self.product_number4 = Entry( frame,width = 10,justify = 'right' )
		self.product_number4.grid( row = 5,column = 2 )
		self.product_number5 = Entry( frame,width = 10,justify = 'right' )
		self.product_number5.grid( row = 6,column = 2 )
		self.product_number6 = Entry( frame,width = 10,justify = 'right' )
		self.product_number6.grid( row = 7,column = 2 )

		Label( frame,text = "ราคาทั้งหมด" ).grid( row = 1,column = 3,sticky = W )
		self.product_total = Text( frame,height = 1,width = 10 )
		self.product_total.grid( row = 2,column = 3 )
		self.product_total2 = Text( frame,height = 1,width = 10,)
		self.product_total2.grid( row = 3,column = 3 )
		self.product_total3 = Text( frame,height = 1,width = 10,)
		self.product_total3.grid( row = 4,column = 3 )
		self.product_total4 = Text( frame,height = 1,width = 10,)
		self.product_total4.grid( row = 5,column = 3 )
		self.product_total5 = Text( frame,height = 1,width = 10,)
		self.product_total5.grid( row = 6,column = 3 )
		self.product_total6 = Text( frame,height = 1,width = 10,)
		self.product_total6.grid( row = 7,column = 3 )

		frame2 = ttk.LabelFrame( self,text = 'คำนวณราคา' )
		frame2.grid( row = 1,column = 0,sticky = W )
		Label( frame2,text = "ราคาสินค้าทั้งหมด(ไม่รวม Vat) :" ).grid( row = 1,column = 0 )
		self.product_total_no = Entry( frame2,width = 15,justify = 'right' )
		self.product_total_no.grid( row = 1,column = 1 )

		Label( frame2,text = "ภาษีมูลค่าเพิ่ม :" ).grid( row = 2,column = 0 )
		v = StringVar( self,value = '7%' )
		self.Invoice = Entry( frame2,textvariable = v,width = 15,justify = 'right',state = 'readonly' )
		self.Invoice.grid( row = 2,column = 1 )

		Label( frame2,text = "ราคาทั้งหมด(รวม Vat) :" ).grid( row = 3,column = 0 )
		self.product_grand_total = Entry( frame2,width = 15,justify = 'right' )
		self.product_grand_total.grid( row = 3,column = 1 )
		button1 = ttk.Button( frame2,text = 'คำนวณสินค้าทั้งหมด',command = self.CalProduct,width = 15 )
		button1.grid( row = 4,columnspan = 2 )
		button2 = ttk.Button( frame2,text = 'ล้างข้อมูล',width = 15 )
		button2.grid( row = 5,columnspan = 2 )

		frame3 = ttk.LabelFrame( self,text = "ปุ่มคำสั่งต่างๆ" )
		frame3.grid( row = 0,column = 1,sticky = NW )

		button3 = ttk.Button( frame3,text = 'หน้าข้อมูลสินค้า',command = lambda: controller.show_frame( PageOne ),
							  width = 20 )
		button3.grid( row = 2,column = 0 )

		button4 = ttk.Button( frame3,text = 'หน้าข้อมูลลูกค้า',command = lambda: controller.show_frame( PageTwo ),
							  width = 20 )
		button4.grid( row = 1,column = 0 )

		button5 = ttk.Button( frame3,text = "กลับหน้าคำนวณราคาน้ำมัน",
							  command = lambda: controller.show_frame( StartPage ),width = 20 )
		button5.grid( row = 0,column = 0 )

	def CalProduct(self):
		self.product1 = int( self.product_number.get() ) * int( self.product_price.get() )
		self.product_total.insert( END,self.product1 )
		self.product2 = int( self.product_number2.get() ) * int( self.product_price2.get() )
		self.product_total2.insert( END,self.product2 )
		self.product3 = int( self.product_number3.get() ) * int( self.product_price3.get() )
		self.product_total3.insert( END,self.product3 )
		self.product4 = int( self.product_number4.get() ) * int( self.product_price4.get() )
		self.product_total4.insert( END,self.product4 )
		self.product5 = int( self.product_number5.get() ) * int( self.product_price5.get() )
		self.product_total5.insert( END,self.product5 )
		self.product6 = int( self.product_number6.get() ) * int( self.product_price6.get() )
		self.product_total6.insert( END,self.product6 )

		self.productTotal = self.product1 + self.product2 + self.product3 + self.product4 + self.product5 + self.product6
		self.product_total_no.insert( END,self.productTotal )

		self.productVat = self.productTotal * 0.7 + self.productTotal
		self.product_grand_total.insert( END,self.productVat )

	def combo_product(self):
		db = sqlite3.connect( 'MyDatabase.db' )
		cursor = db.execute( 'SELECT Product_Name FROM Product' )

		data = []

		for row in cursor.fetchall():
			data.append( row[0] )

		return data


app = Invoice()
app.geometry( "800x480" )
app.title( "Invoice" )
app.mainloop()
