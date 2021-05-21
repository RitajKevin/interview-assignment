from tkinter import * 
from tkinter import ttk



app = Tk()
app.geometry('650x300')
app.resizable(True,True)
app.title("FrontEnd")
app.configure(bg="#AED6F1")

def click(event):
    amount.delete(0,END)
    amount.config(fg="black")

def lev(event):
    Leverage.delete(0,END)
    Leverage.config(fg="black")


def Tal(event):
    Trailing.delete(0,END)
    Trailing.config(fg="black")

    
option=["BTC/USDT","BTC/USDT","BTC/USDT"]
item = ttk.Combobox(app,value =option,width=100)
item.current(0)
item.grid(row=0,column=0,columnspan = 4,padx = 10,pady = 10)



buy = Button(app, text = "BUY", width = 42,bg = "#02AB02",fg="white")
buy.grid(row=1,column=0,columnspan= 2)



sell = Button(app, text = "SELL", width = 42,bg = "#D11307",fg="white")
sell.grid(row=1,column=2,columnspan= 2)



text = StringVar()
amount= Entry(app,width=102,textvariable=text,fg="#ABB2B9")
amount.insert(0,"Amount per Trade(USDT without leverage)")
amount.bind("<Button-1>",click)
amount.grid(row=2,column=0,columnspan=4, pady=10)



BP_Lbl = Label(app, text = "BUY PRICE",bg="#AED6F1")
BP_Lbl.grid(row=3,column=0,columnspan=1, pady=3)



BTP_Lbl = Label(app, text = "Target %",bg="#AED6F1")
BTP_Lbl.grid(row=3,column=1,columnspan=1, pady=3)



SP_Lbl = Label(app, text = "Sell Price",bg="#AED6F1")
SP_Lbl.grid(row=3,column=2,columnspan=1, pady=3)



ST_Lbl = Label(app, text = "Target %",bg="#AED6F1")
ST_Lbl.grid(row=3,column=3,columnspan=1, pady=3)



Buy_Price= Entry(app,width = 23)
Buy_Price.grid(row=4,column=0,columnspan=1)



Buy_Target= Entry(app,width = 23)
Buy_Target.grid(row=4,column=1,columnspan=1)



Sell_Price= Entry(app,width = 23)
Sell_Price.grid(row=4,column=2,columnspan=1)



Sell_Target = Entry(app,width = 23)
Sell_Target.grid(row=4,column=3,columnspan=1)



Lev_Lbl = Label(app, text = "Leverage",bg="#AED6F1")
Lev_Lbl.grid(row=5,column=0,columnspan=2, pady=3)



Trail_Lbl = Label(app, text = "Trailing Stoploss in %",bg="#AED6F1")
Trail_Lbl.grid(row=5,column=2,columnspan=2, pady=3)



Leverage = Entry(app, width= 50,fg="#ABB2B9")
Leverage.insert(0,"Enter Leverage Here")
Leverage.bind("<Button-1>",lev)
Leverage.grid(row=6,column=0,columnspan=2)



Trailing = Entry(app, width = 50,fg="#ABB2B9")
Trailing.insert(0,"Enter Here")
Trailing.bind("<Button-1>",Tal)
Trailing.grid(row=6,column=2,columnspan=2)

Start = Button(app, text = "Start Bot", width = 20,bg = "#02AB02",fg="white")
Start.grid(row=7,column=1,columnspan= 2,pady = 10)

app.mainloop()
