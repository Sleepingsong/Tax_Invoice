from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3

LARGE_FONT = ("Verdana",12)


class Invoice( tk.Tk ):

	def __init__(self,*args,**kwargs):
		tk.Tk.__init__( self,*args,**kwargs )
		container = tk.Frame( self )

		container.grid()
		container.grid_rowconfigure( 0,weight = 1 )
		container.grid_columnconfigure( 0,weight = 1 )

		self.frames = { }

		for F in (StartPage,PageOne, PageTwo):
			frame = F( container,self )
			self.frames[F] = frame
			frame.grid( row = 0,column = 0,sticky = "NSEW" )

		self.show_frame( StartPage )

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage( tk.Frame ): #Calculate Price

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )

		frame = ttk.LabelFrame( self,text = 'สินค้าทั้งหมด' )
		frame.grid( row = 0,column = 0,sticky = NW )

		style = ttk.Style(self)
		style.configure("TButton", font=('wasy10', 14))

		Label( frame,text = "ชื่อสินค้า" ).grid( row = 1,sticky = W )
		self.product_name = Entry( frame,width = 40,justify='right'   )
		self.product_name.grid( row = 2,column = 0 )
		self.product_name2 = Entry( frame,width = 40,justify='right'  )
		self.product_name2.grid( row = 3,column = 0 )
		self.product_name3 = Entry( frame,width = 40,justify='right'  )
		self.product_name3.grid( row = 4,column = 0 )
		self.product_name4 = Entry( frame,width = 40,justify='right'  )
		self.product_name4.grid( row = 5,column = 0 )
		self.product_name5 = Entry( frame,width = 40,justify='right'  )
		self.product_name5.grid( row = 6,column = 0 )
		self.product_name6 = Entry( frame,width = 40,justify='right'  )
		self.product_name6.grid( row = 7,column = 0 )

		Label( frame,text = "ประเภทสินค้า" ).grid( row = 1,column = 1,sticky = W )
		self.product_type = ttk.Combobox(frame, width = 20, state='readonly')
		self.product_type['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		self.product_type.grid( row = 2,column = 1 )
		self.product_type2 = ttk.Combobox(frame, width = 20, state='readonly')
		self.product_type2['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		self.product_type2.grid( row = 3,column = 1 )
		self.product_type3 = ttk.Combobox(frame, width = 20, state='readonly')
		self.product_type3['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		self.product_type3.grid( row = 4,column = 1 )
		self.product_type4 = ttk.Combobox(frame, width = 20, state='readonly')
		self.product_type4['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		self.product_type4.grid( row = 5,column = 1 )
		self.product_type5 = ttk.Combobox(frame, width = 20, state='readonly')
		self.product_type5['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		self.product_type5.grid( row = 6,column = 1 )
		self.product_type6 = ttk.Combobox(frame, width = 20, state='readonly')
		self.product_type6['values'] = ("น้ำมัน","แก๊ซ","หล่อลื่นเครื่องยนต์","จารบี","น้ำมันเบรก","น้ำมันหล่อลื่น","เกียร์และเฝืองท้าย")
		self.product_type6.grid( row = 7,column = 1 )


		Label( frame,text = "ราคา(บาท)" ).grid( row = 1,column = 2,sticky = W )
		self.product_price = Entry(frame, width = 10,justify='right' )
		self.product_price.grid(row = 2, column = 2)
		self.product_price2 = Entry(frame, width = 10,justify='right' )
		self.product_price2.grid(row = 3, column = 2)
		self.product_price3 = Entry(frame, width = 10,justify='right' )
		self.product_price3.grid(row = 4, column = 2)
		self.product_price4 = Entry(frame, width = 10,justify='right' )
		self.product_price4.grid(row = 5, column = 2)
		self.product_price5 = Entry(frame, width = 10,justify='right' )
		self.product_price5.grid(row = 6, column = 2)
		self.product_price6 = Entry(frame, width = 10,justify='right' )
		self.product_price6.grid(row = 7, column = 2)

		Label(frame,text = "จำนวน").grid(row = 1, column = 3, sticky = W)
		self.product_number  = Entry(frame, width = 10,justify='right' )
		self.product_number.grid(row =2, column = 3)
		self.product_number2  = Entry(frame, width = 10,justify='right' )
		self.product_number2.grid(row =3, column = 3)
		self.product_number3  = Entry(frame, width = 10,justify='right' )
		self.product_number3.grid(row =4, column = 3)
		self.product_number4  = Entry(frame, width = 10,justify='right' )
		self.product_number4.grid(row =5, column = 3)
		self.product_number5  = Entry(frame, width = 10,justify='right' )
		self.product_number5.grid(row =6, column = 3)
		self.product_number6  = Entry(frame, width = 10,justify='right' )
		self.product_number6.grid(row =7, column = 3)

		Label(frame, text = "ราคาทั้งหมด(บาท)").grid(row = 1, column = 4, sticky = W)
		self.product_total = Text(frame, height =1 , width= 10 )
		self.product_total.grid(row = 2, column = 4)
		self.product_total2 = Text(frame, height =1 , width= 10, )
		self.product_total2.grid(row = 3, column = 4)
		self.product_total3 = Text(frame, height =1 , width= 10, )
		self.product_total3.grid(row = 4, column = 4)
		self.product_total4 = Text(frame, height =1 , width= 10, )
		self.product_total4.grid(row = 5, column = 4)
		self.product_total5 = Text(frame, height =1 , width= 10, )
		self.product_total5.grid(row = 6, column = 4)
		self.product_total6 = Text(frame, height =1 , width= 10, )
		self.product_total6.grid(row = 7, column = 4)

		frame2 = ttk.LabelFrame( self,text = 'คำนวณราคา' )
		frame2.grid( row = 1,column = 0, sticky = E)
		Label(frame2, text = "ราคาสินค้าทั้งหมด(ไม่รวม Vat) :").grid(row =1, column = 0)
		self.product_total_no = Entry(frame2, width = 15, justify = 'right')
		self.product_total_no.grid(row = 1, column = 1)

		Label(frame2, text = "ภาษีมูลค่าเพิ่ม :").grid(row =2, column = 0)
		v = StringVar(self, value='7%')
		self.Invoice = Entry(frame2, textvariable = v ,width = 15, justify = 'right' , state = 'readonly')
		self.Invoice.grid(row = 2, column = 1)

		Label(frame2, text = "ราคาทั้งหมด(รวม Vat) :").grid(row = 3, column = 0)
		self.product_grand_total = Entry(frame2, width = 15, justify = 'right')
		self.product_grand_total.grid(row = 3, column = 1)

		frame3 = ttk.LabelFrame(self, text = "ปุ่มคำสั่งต่างๆ")
		frame3.grid(row = 0 ,column = 1, sticky = NW)
		button1 = ttk.Button(frame3, text = 'คำนวณสินค้าทั้งหมด', command = self.CalProduct)
		button1.grid(row = 0)

		button2 = ttk.Button(frame3, text = 'ล้างข้อมูล')
		button2.grid(row = 1, column = 0)

		button3 = ttk.Button(frame3, text = 'หน้าข้อมูลสินค้า', command = lambda: controller.show_frame( PageOne ))
		button3.grid(row = 2, column =0)

		button4 = ttk.Button(frame3, text = 'หน้าข้อมูลลูกค้า', command = lambda: controller.show_frame( PageTwo ))
		button4.grid(row = 3, column = 0)

	def CalProduct(self):
		self.product1 = int(self.product_number.get()) * int(self.product_price.get())
		self.product_total.insert(END,self.product1)
		self.product2 = int(self.product_number2.get()) * int(self.product_price2.get())
		self.product_total2.insert(END, self.product2)
		self.product3 = int(self.product_number3.get()) * int(self.product_price3.get())
		self.product_total3.insert(END, self.product3)
		self.product4 = int(self.product_number4.get()) * int(self.product_price4.get())
		self.product_total4.insert(END, self.product4)
		self.product5 = int(self.product_number5.get()) * int(self.product_price5.get())
		self.product_total5.insert(END, self.product5)
		self.product6 = int(self.product_number6.get()) * int(self.product_price6.get())
		self.product_total6.insert(END, self.product6)

		self.productTotal = self.product1 + self.product2 + self.product3 + self.product4 + self.product5 + self.product6
		self.product_total_no.insert(END, self.productTotal)

		self.productVat = self.productTotal * 0.7 + self.productTotal
		self.product_grand_total.insert(END, self.productVat)


class PageOne( tk.Frame ):  # Product Page

	db_name = 'MyDatabase.db'

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )
		frame = ttk.LabelFrame( self,text = 'เพิ่มสินค้า' )
		frame.grid( row = 0,column = 0,sticky = NW )




		Label( frame,text = 'ชื่อสินค้า' ).grid( row = 1,column = 0 )
		self.name = Entry( frame )
		self.name.grid( row = 1,column = 1 )

		Label( frame,text = 'ประเภทสินค้า' ).grid( row = 2,column = 0 )
		self.type = Entry( frame ,justify='right' )
		self.type.grid( row = 2,column = 1 )

		Label( frame,text = 'ราคา' ).grid( row = 3,column = 0 )
		self.price = Entry( frame,justify='right'  )
		self.price.grid( row = 3,column = 1 )

		ttk.Button( frame,text = 'เพิ่มข้อมูล',command = self.adding ).grid( row = 4,column = 0,columnspan = 2 )
		self.message = Label( text = '',fg = 'red' )
		self.message.grid( row = 4,column = 0 )

		self.tree = ttk.Treeview( self,height = 15,column = ("2","3") )
		self.tree.grid( row = 1,column = 0)
		self.tree.heading( '#0',text = 'ชื่อสินค้า',anchor = W )
		self.tree.heading( 0,text = 'ประเภทสินค้า',anchor = W )
		self.tree.heading( 1,text = 'ราคา',anchor = W )

		frame2 = LabelFrame(self, text = 'ชุดคำสั่ง')
		frame2.grid(row = 0, column = 0,sticky = E)

		button1 = ttk.Button( frame2,text = 'ลบข้อมูล',command = self.deleting )
		button1.grid( row = 0,column = 0 )
		button2 = ttk.Button( frame2,text = 'แก้ไขข้อมูล',command = self.editing )
		button2.grid( row = 1,column = 0 )
		button3 = ttk.Button( frame2,text = "หน้าข้อมูลลูกค้า",command = lambda: controller.show_frame( PageTwo ) )
		button3.grid( row = 0,column = 1,)
		button3 = ttk.Button( frame2,text = "หน้าคำนวณสินค้า",command = lambda: controller.show_frame( StartPage ) )
		button3.grid( row = 0,column = 2,)

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
		self.message['text'] = ''
		try:
			self.tree.item( self.tree.selection() )['values'][1]
		except IndexError as e:
			self.message['text'] = 'Please select record'
			return

		name = self.tree.item( self.tree.selection() )['text']
		old_price = self.tree.item( self.tree.selection() )['values'][1]

		self.edit_main = Toplevel()
		self.edit_main.title( 'Editing' )

		Label( self.edit_main,text = 'Old name: ' ).grid( row = 0,column = 1 )
		Entry( self.edit_main,textvariable = StringVar( self.edit_main,value = name ),state = 'readonly' ).grid(
			row = 0,column = 2 )
		Label( self.edit_main,text = 'New name: ' ).grid( row = 1,column = 1 )
		new_name = Entry( self.edit_main )
		new_name.grid( row = 1,column = 2 )

		Label( self.edit_main,text = 'Old Price: ' ).grid( row = 2,column = 1 )
		Entry( self.edit_main,textvariable = StringVar( self.edit_main,value = old_price ),state = 'readonly' ).grid(
			row = 2,column = 2 )
		Label( self.edit_main,text = 'New price: ' ).grid( row = 3,column = 1 )
		new_price = Entry( self.edit_main )
		new_price.grid( row = 3,column = 2 )

		Button( self.edit_main,text = 'Save Change',
				command = lambda: self.edit_record( new_name.get(),name,new_price.get(),old_price ) ).grid( row = 4,
																											column = 2,
																											sticky = W )

		self.edit_main.mainloop()

	def edit_record(self,new_name,name,new_price,old_price):
		query = 'UPDATE Product SET Product_Name = ?, Product_Price = ? WHERE Product_Name = ? AND Product_Price = ?'
		paremeters = (new_name,new_price,name,old_price)
		self.run_query( query,paremeters )
		self.edit_main.destroy()
		self.message['text'] = 'Record {} changed'.format( name )
		self.viewing_record()


class PageTwo( tk.Frame ):  # Customer Page

	db_name = 'MyDatabase.db'

	def __init__(self,parent,controller):
		tk.Frame.__init__( self,parent )



		frame2 = LabelFrame( self,text = "เพิ่มข้อมูลลูกค้า" )
		frame2.grid( row = 0,column = 0,sticky = NW )

		Label( frame2,text = 'ชื่อลูกค้า' ).grid( row = 1,column = 2 )
		self.Customer_name = Entry( frame2,justify='right'  )
		self.Customer_name.grid( row = 1,column = 3 )

		Label( frame2,text = 'ทะเบียนรถ' ).grid( row = 1,column = 4 )
		self.Car_plate = Entry( frame2,justify='right'  )
		self.Car_plate.grid( row = 1,column = 5 )

		Label( frame2,text = 'ชื่อบริษัท' ).grid( row = 1,column = 6 )
		self.Company_name = Entry( frame2,justify='right'  )
		self.Company_name.grid( row = 1,column = 7 )

		Label( frame2,text = 'เบอร์โทรศัพท์' ).grid( row = 2,column = 2 )
		self.Phone_number = Entry( frame2,justify='right'  )
		self.Phone_number.grid( row = 2,column = 3 )

		Label( frame2,text = 'ที่อยู่' ).grid( row = 2,column = 4 )
		self.Customer_address = Entry( frame2 ,justify='right' )
		self.Customer_address.grid( row = 2,column = 5 )

		ttk.Button( frame2,text = 'เพิ่มข้อมูล',command = self.adding2 ).grid( row = 3,column = 7,columnspan = 2 )
		self.message2 = Label( text = '',fg = 'red' )
		self.message2.grid( row = 3,column = 0 )

		self.tree2 = ttk.Treeview( self,height = 15,column = ("1","2","3") )
		self.tree2.grid( row = 2,column = 0)
		self.tree2.heading( '#0',text = 'ชื่อลูกค้า',anchor = W )
		self.tree2.heading( 1,text = 'ทะเบียนรถ',anchor = W )
		self.tree2.heading( 2,text = 'ชื่อบริษัท',anchor = W )
		self.tree2.heading( 3,text = 'เบอร์โทรศัพท์',anchor = W )

		frame2 = LabelFrame(self, text = 'ชุดคำสั่ง')
		frame2.grid(row = 1, column = 0, sticky = W)

		button1 = ttk.Button( frame2,text = 'ลบข้อมูล',command = self.deleting2 )
		button1.grid( row = 0,column = 0 )
		# button2 = ttk.Button( frame2,text = 'แก้ไขข้อมูล',command = self.editing )
		# button2.grid( row = 1,column = 0 )
		button3 = ttk.Button( frame2,text = "หน้าข้อมูลสินค้า",command = lambda: controller.show_frame( PageOne ) )
		button3.grid( row = 0,column = 1,)
		button3 = ttk.Button( frame2,text = "หน้าคำนวณสินค้า",command = lambda: controller.show_frame( StartPage ) )
		button3.grid( row = 0,column = 2,)


		self.viewing_record2()

	def run_query(self,query,parameters=()):
		with sqlite3.connect( self.db_name ) as conn:
			cursor = conn.cursor()
			query_result = cursor.execute( query,parameters )
			conn.commit()
		return query_result

	def viewing_record2(self):
		records = self.tree2.get_children()
		for element in records:
			self.tree2.delete( element )
		query = 'SELECT * FROM Customer ORDER BY Customer_ID DESC'
		db_rows = self.run_query( query )
		for row in db_rows:
			self.tree2.insert( '',0,text = row[1],values = (row[2],row[3],row[4]) )

	def validation2(self):
		return len( self.Customer_name.get() ) != 0 \
			   and len( self.Company_name.get() ) != 0 and len( self.Car_plate.get() ) != 0 \
			   and len( self.Phone_number.get() ) != 0

	def adding2(self):
		if self.validation2():
			query = 'INSERT INTO Customer VALUES (NULL, ?, ?,?,?,?)'
			parameters = (
				self.Customer_name.get(),self.Phone_number.get(),self.Car_plate.get(),self.Company_name.get(),
				self.Customer_address.get())
			self.run_query( query,parameters )
			self.message2['text'] = 'Record {} added to database'.format( self.Company_name.get() )
			self.Customer_name.delete( 0,END )
			self.Car_plate.delete( 0,END )
			self.Company_name.delete( 0,END )
			self.Phone_number.delete( 0,END )

		else:
			self.message2['text'] = 'Some fields are empty'
		self.viewing_record2()

	def deleting2(self):
		self.message2['text'] = ''
		try:
			self.tree2.item( self.tree2.selection() )['values'][0]
		except IndexError as e:
			self.message2['text'] = 'Please select record'
			return

		self.message2['text'] = ''
		name = self.tree2.item( self.tree2.selection() )['text']
		query = 'DELETE FROM Customer WHERE Customer_Name = ?'
		self.run_query( query,(name,) )
		self.message2['text'] = 'Record {} is deleted'.format( name )
		self.viewing_record2()


app = Invoice()
app.geometry( "800x480" )
app.title("Invoice")
app.mainloop()
