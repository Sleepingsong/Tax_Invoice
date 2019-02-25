from requests import Session
import zeep
from zeep import Client
from zeep.transports import Transport
from tkinter import *
from tkinter import ttk
import tkinter as tk
import urllib3

root = tk.Tk()

tax_enter = Entry(root)
tax_enter.grid(row = 0)
button1 = Button(root, text = 'ค้นหา', command= lambda: tax_search())
button1.grid(row = 1)


def tax_search():

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = Session()
    session.verify = False
    transport = Transport(session=session)

    client = Client('https://rdws.rd.go.th/serviceRD3/vatserviceRD3.asmx?wsdl',
                    transport=transport)
    result = client.service.Service(
        username='anonymous',
        password='anonymous',
        TIN = tax_enter.get(),
        ProvinceCode=0,
        BranchNumber=0,
        AmphurCode=0
    )
    # Convert Zeep Response object (in this case Service) to Python dict.
    result = zeep.helpers.serialize_object(result)
    # print(result)
    for k in result.keys():
        # print(k, result[k])
        if result[k] is not None:
            v = result[k].get('anyType', None)[0]
            print(k,v)


root.geometry('800x600')
root.mainloop()