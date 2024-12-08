import tkinter
from tkinter import *
import random
import time
from tkinter import filedialog,messagebox
#functions
def menu():
    root2=Toplevel()
    root2.title('Menu')
    root2.geometry('500x600')
    root2.configure(background='black')
    numberLable = Label(root2, text='Pizza:-100/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Burger:-120/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Sandwich:-110/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Frenchfries:-90/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Dalkhichadi:-120/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Biryani:-150/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Pulav:-150/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Pasta:-180/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Lassi:-20/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Coffee:-30/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='faluda:-40/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Jaljeera:-50/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='MasalaTea:-60/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='BadamMilk:-70/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='Roohfzaa:-80/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='ColdDrink:-90/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='OreoCake:-50/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='AppleCake:-60/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='KitkatCake:-70/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='BrownieCake:-80/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='BananaCake:-90/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='MangoCake:-100/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='PineappleCake:-110/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    numberLable = Label(root2, text='ChocolateCake:-120/-', fg='white', font=('Times New Roman', 12, 'bold'), bg='black')
    numberLable.pack()
    root2.mainloop()
def reset():
    textReceipt.delete('1.0',END)
def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textReceipt.get('1.0',END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Saved', 'your bill has been saved')
def receipt():
    textReceipt.delete('1.0',END)
    x=random.randint(100,10000)
    billnumber="Bill number"+str(x)
    # date=time().strftime("%d/%m/%Y")
    textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\n')
    textReceipt.insert(END,'***********************************\n')
    textReceipt.insert(END,'Items:\t\t cost of items\n')
    textReceipt.insert(END,'***********************************\n')
    if e_pizza.get() !='0':
        textReceipt.insert(END, f'Pizza\t\t\t {int( e_pizza.get())*100 } \n\n')
    if e_Burger.get() != '0':
        textReceipt.insert(END, f'Burger\t\t\t {int( e_Burger.get())*120} \n\n')
    if e_sandwitch.get() != '0':
        textReceipt.insert(END, f'sandwitch\t\t\t {int( e_sandwitch.get())*110 } \n\n')
    if e_frenchfries.get() != '0':
        textReceipt.insert(END, f'frenchfries\t\t\t {int( e_frenchfries.get())*90 } \n\n')
    if e_Dalkhichadi.get() != '0':
        textReceipt.insert(END, f'Dalkhichadi\t\t\t {int( e_Dalkhichadi.get())*120 } \n\n')
    if e_Biryani.get() != '0':
        textReceipt.insert(END, f'Biryani\t\t\t {int( e_Biryani.get())*150 } \n\n')
    if e_Pulav.get() != '0':
        textReceipt.insert(END, f'Pulav\t\t\t {int( e_Pulav.get())*150 } \n\n')
    if e_Pasta.get() != '0':
        textReceipt.insert(END, f'Pasta\t\t\t {int( e_Pasta.get())*180 } \n\n')
    if e_Lassi.get() != '0':
        textReceipt.insert(END, f'Lassi\t\t\t {int( e_Lassi.get())*20 } \n\n')
    if e_coffee.get() != '0':
        textReceipt.insert(END, f'coffee\t\t\t {int( e_coffee.get())*30 } \n\n')
    if e_faluda.get() != '0':
        textReceipt.insert(END, f'faluda\t\t\t {int( e_faluda.get())*40 } \n\n')
    if e_jaljeera.get() != '0':
        textReceipt.insert(END, f'jaljeera\t\t\t {int( e_jaljeera.get())*50 } \n\n')
    if e_MasalaTea.get() != '0':
        textReceipt.insert(END, f'MasalaTea\t\t\t {int( e_MasalaTea.get())*60} \n\n')
    if e_BadamMilk.get() != '0':
        textReceipt.insert(END, f'BadamMilk\t\t\t {int( e_BadamMilk.get())*70 } \n\n')
    if e_Roohfzaa.get() != '0':
        textReceipt.insert(END, f'Roohfzaa\t\t\t {int( e_Roohfzaa.get())*80 } \n\n')
    if e_coldDrink.get() != '0':
        textReceipt.insert(END, f'coldDrink\t\t\t {int( e_coldDrink.get())*90} \n\n')
    if e_Oreo.get() != '0':
        textReceipt.insert(END, f'Oreo\t\t\t {int( e_Oreo.get())*50 } \n\n')
    if e_Apple.get() != '0':
        textReceipt.insert(END, f'Apple\t\t\t {int( e_Apple.get())*60 } \n\n')
    if e_Kitkat.get() != '0':
        textReceipt.insert(END, f'Kitkat\t\t\t {int( e_Kitkat.get())*70 } \n\n')
    if e_Brownie.get() != '0':
        textReceipt.insert(END, f'Brownie\t\t\t {int( e_Brownie.get())*80 } \n\n')
    if e_Banana.get() != '0':
        textReceipt.insert(END, f'Banana\t\t\t {int( e_Banana.get())*90 } \n\n')
    if e_Mango.get() != '0':
        textReceipt.insert(END, f'Mango\t\t\t {int( e_Mango.get())*100 } \n\n')
    if e_Pineapple.get() != '0':
        textReceipt.insert(END, f'Pineapple\t\t\t {int( e_Pineapple.get())*110 } \n\n')
    if e_chocolate.get() != '0':
        textReceipt.insert(END, f'chocolate\t\t\t {int( e_chocolate.get())*120 } \n\n')
    textReceipt.insert(END, '***********************************\n')
    if costoffoodvar.get()!='0 Rs':
     textReceipt.insert(END,f'Cost of Food\t\t\t{priceofFood}RS\n\n')
    if costofdrinksvar.get() != '0 Rs':
     textReceipt.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}RS\n\n')
    if costofcakesvar.get() != '0 Rs':
     textReceipt.insert(END, f'Cost of Cakes\t\t\t{priceofCakes}RS\n\n')

    textReceipt.insert(END, f'Sub Total\t\t\t{subtotalItems}Rs\n\n')
    textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
    textReceipt.insert(END, f'Total cost\t\t\t{subtotalItems+50}Rs\n\n')
    textReceipt.insert(END, '***********************************\n')


def totalcost():
    global priceofFood,priceofdrinks,priceofCakes,subtotalItems
    item1=int(e_pizza.get())
    item2=int(e_Burger.get())
    item3=int(e_sandwitch.get())
    item4=int(e_frenchfries.get())
    item5=int(e_Dalkhichadi.get())
    item6=int(e_Biryani.get())
    item7=int(e_Pulav.get())
    item8=int(e_Pasta.get())

    item9=int(e_Lassi.get())
    item10=int(e_coffee.get())
    item11=int(e_faluda.get())
    item12=int(e_jaljeera.get())
    item13=int(e_MasalaTea.get())
    item14=int(e_BadamMilk.get())
    item15=int(e_Roohfzaa.get())
    item16=int(e_coldDrink.get())

    item17=int(e_Oreo.get())
    item18=int(e_Apple.get())
    item19=int(e_Kitkat.get())
    item20=int(e_Brownie.get())
    item21=int(e_Banana.get())
    item22=int(e_Mango.get())
    item23=int(e_Pineapple.get())
    item24=int(e_chocolate.get())

    priceofFood=(item1*100)+(item2*120)+(item3*110)+(item4*90)+(item5*120)+(item6*150)+(item7*150)+(item8*180)
    priceofdrinks=(item9*20)+(item10*30)+(item11*40)+(item12*50)+(item13*60)+(item14*70)+(item15*80)+(item16*90)
    priceofCakes=(item17*50)+(item18*60)+(item19*70)+(item20*80)+(item21*90)+(item22*100)+(item23*110)+(item24*120)

    costoffoodvar.set(str(priceofFood)+' Rs')
    costofdrinksvar.set(str(priceofdrinks)+' Rs')
    costofcakesvar.set(str(priceofCakes)+' Rs')

    subtotalofItems=priceofFood+priceofdrinks+priceofCakes
    subtotalvar.set('Rs'+str(subtotalofItems))

    servicetaxvar.set('50 Rs')

    totalcost= subtotalofItems+50
    totalcostvar.set(' Rs'+str(totalcost))


def Pizza():
    if var1.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.delete('0',END)
        textpizza.focus()
    else:
        textpizza.config(state=DISABLED)
        e_pizza.set('0')
def Burger():
    if var2.get()==1:
        textBurger.config(state=NORMAL)
        textBurger.delete('0',END)
        textBurger.focus()
    else:
        textBurger.config(state=DISABLED)
        e_Burger.set('0')
def sandwitch():
    if var3.get()==1:
        textsandwitch.config(state=NORMAL)
        textsandwitch.delete('0',END)
        textsandwitch.focus()
    else:
        textsandwitch.config(state=DISABLED)
        e_sandwitch.set('0')
def frenchfries():
    if var4.get()==1:
        textfrenchfries.config(state=NORMAL)
        textfrenchfries.delete('0',END)
        textfrenchfries.focus()
    else:
        textfrenchfries.config(state=DISABLED)
        e_frenchfries.set('0')
def Biryani():
    if var5.get()==1:
        textBiryani.config(state=NORMAL)
        textBiryani.delete('0',END)
        textBiryani.focus()
    else:
        textBiryani.config(state=DISABLED)
        e_Biryani.set('0')
def Pulav():
    if var6.get()==1:
        textPulav.config(state=NORMAL)
        textPulav.delete('0',END)
        textPulav.focus()
    else:
        textPulav.config(state=DISABLED)
        e_Pulav.set('0')
def Pasta():
    if var7.get()==1:
        textPasta.config(state=NORMAL)
        textPasta.focus()
    else:
        textPasta.config(state=DISABLED)
        e_Pasta.set('0')
def Dalkhichadi():
    if var8.get()==1:
        textDalkhichadi.config(state=NORMAL)
        textDalkhichadi.delete('0',END)
        textDalkhichadi.focus()
    else:
        textDalkhichadi.config(state=DISABLED)
        e_Dalkhichadi.set('0')
def Lassi():
    if var9.get()==1:
        textLassi.config(state=NORMAL)
        textLassi.delete('0',END)
        textLassi.focus()
    else:
        textLassi.config(state=DISABLED)
        e_Lassi.set('0')
def coffee():
    if var10.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete('0',END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')
def Faluda():
    if var11.get()==1:
        textFaluda.config(state=NORMAL)
        textFaluda.delete('0',END)
        textFaluda.focus()
    else:
        textFaluda.config(state=DISABLED)
        e_faluda.set('0')
def jaljeera():
    if var12.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete('0',END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')
def MasalaTea():
    if var13.get()==1:
        textMasalaTea.config(state=NORMAL)
        textMasalaTea.delete('0',END)
        textMasalaTea.focus()
    else:
        textMasalaTea.config(state=DISABLED)
        e_MasalaTea.set('0')
def BadamMilk():
    if var14.get()==1:
        textBadamMilk.config(state=NORMAL)
        textBadamMilk.delete('0',END)
        textBadamMilk.focus()
    else:
        textBadamMilk.config(state=DISABLED)
        e_BadamMilk.set('0')
def Roohfzaa():
    if var15.get()==1:
        textRoohfzaa.config(state=NORMAL)
        textRoohfzaa.delete('0',END)
        textRoohfzaa.focus()
    else:
        textRoohfzaa.config(state=DISABLED)
        e_Roohfzaa.set('0')
def ColdDrink():
    if var16.get()==1:
        textColdDrink.config(state=NORMAL)
        textColdDrink.delete('0',END)
        textColdDrink.focus()
    else:
        textColdDrink.config(state=DISABLED)
        e_coldDrink.set('0')
def Oreo():
    if var17.get()==1:
        textOreo.config(state=NORMAL)
        textOreo.delete('0',END)
        textOreo.focus()
    else:
        textOreo.config(state=DISABLED)
        e_Oreo.set('0')
def Apple():
    if var18.get()==1:
        textApple.config(state=NORMAL)
        textApple.delete('0',END)
        textApple.focus()
    else:
        textApple.config(state=DISABLED)
        e_Apple.set('0')
def Kitkat():
    if var19.get()==1:
        textKitkat.config(state=NORMAL)
        textKitkat.delete('0',END)
        textKitkat.focus()
    else:
        textKitkat.config(state=DISABLED)
        e_Kitkat.set('0')
def Brownie():
    if var20.get()==1:
        textBrownie.config(state=NORMAL)
        textBrownie.delete('0',END)
        textBrownie.focus()
    else:
        textBrownie.config(state=DISABLED)
        e_Brownie.set('0')
def Banana():
    if var21.get()==1:
        textBanana.config(state=NORMAL)
        textBanana.delete('0',END)
        textBanana.focus()
    else:
        textBanana.config(state=DISABLED)
        e_Banana.set('0')
def Mango():
    if var22.get()==1:
        textMango.config(state=NORMAL)
        textMango.delete('0',END)
        textMango.focus()
    else:
        textMango.config(state=DISABLED)
        e_Mango.set('0')
def Pineapple():
    if var23.get()==1:
        textPineapple.config(state=NORMAL)
        textPineapple.delete('0',END)
        textPineapple.focus()
    else:
        textPineapple.config(state=DISABLED)
        e_Pineapple.set('0')
def Chocolate():
    if var24.get()==1:
        textChocolate.config(state=NORMAL)
        textChocolate.delete('0',END)
        textChocolate.focus()
    else:
        textChocolate.config(state=DISABLED)
        e_chocolate.set('0')




root=Tk()
root.geometry("1350x800+0+0")
root.title("Hotel Management System")
root.configure(background="gray")
topFrame=Frame(root,bg="black",bd=10,relief=RIDGE)
topFrame.pack(side=TOP)
lableTitle=Label(topFrame,text="HOTEL NET-TECH MANAGEMENT",font=("Times New Roman",40,"bold"),fg="black",bd=10,relief=RIDGE)
lableTitle.pack(side=TOP)
#frames
menuFrame=Frame(root,bg="gray",bd=10,relief=RIDGE)
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bg="gray",bd=10,relief=RIDGE)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text="Food",bg="gray",font=('Times New Roman',15,'bold'),bd=10,relief=RIDGE)
foodFrame.pack(side=LEFT)


drinksFrame=LabelFrame(menuFrame,text="Drinks",bg="gray",font=('Times New Roman',15,'bold'),bd=10,relief=RIDGE)
drinksFrame.pack(side=LEFT)


cakesFrame=LabelFrame(menuFrame,text="Cakes",bg="gray",font=('Times New Roman',15,'bold'),bd=10,relief=RIDGE)
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bg="gray",bd=10,relief=RIDGE)
rightFrame.pack(side=RIGHT)


leftFrame=Frame(root,bg="gray",bd=10,relief=RIDGE)
leftFrame.pack(side=LEFT)


timeFrame=Frame(leftFrame,bg="gray",bd=10,relief=RIDGE)
timeFrame.pack(side=BOTTOM)

calFrame=Frame(rightFrame,bg="gray",bd=10,relief=RIDGE)
calFrame.pack()

receiptFrame=Frame(rightFrame,bg="gray",bd=10,relief=RIDGE)
receiptFrame.pack()

ButtonFrame=Frame(rightFrame,bg="gray",bd=10,relief=RIDGE)
ButtonFrame.pack()

#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()

e_pizza=StringVar()
e_Burger=StringVar()
e_sandwitch=StringVar()
e_frenchfries=StringVar()
e_Biryani=StringVar()
e_Pulav=StringVar()
e_Pasta=StringVar()
e_Dalkhichadi=StringVar()

e_Lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_jaljeera=StringVar()
e_MasalaTea=StringVar()
e_BadamMilk=StringVar()
e_Roohfzaa=StringVar()
e_coldDrink=StringVar()

e_Oreo=StringVar()
e_Apple=StringVar()
e_Kitkat=StringVar()
e_Brownie=StringVar()
e_Banana=StringVar()
e_Mango=StringVar()
e_Pineapple=StringVar()
e_chocolate=StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

strftime=StringVar()

e_pizza.set('0')
e_Burger.set('0')
e_sandwitch.set('0')
e_frenchfries.set('0')
e_Biryani.set('0')
e_Pulav.set('0')
e_Pasta.set('0')
e_Dalkhichadi.set('0')

e_Lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_jaljeera.set('0')
e_MasalaTea.set('0')
e_BadamMilk.set('0')
e_Roohfzaa.set('0')
e_coldDrink.set('0')

e_Oreo.set('0')
e_Apple.set('0')
e_Kitkat.set('0')
e_Brownie.set('0')
e_Banana.set('0')
e_Mango.set('0')
e_Pineapple.set('0')
e_chocolate.set('0')

#Entry fields for food items

pizza=Checkbutton(foodFrame,text="Pizza",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var1,command=Pizza)
pizza.grid(row=0,column=0,sticky=W)
textpizza=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_pizza)
textpizza.grid(row=0,column=1)

Burger=Checkbutton(foodFrame,text="Burger",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var2,command=Burger)
Burger.grid(row=1,column=0,sticky=W)
textBurger=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Burger)
textBurger.grid(row=1,column=1,padx=10,pady=10)

sandwitch=Checkbutton(foodFrame,text="Sandwitch",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var3,command=sandwitch)
sandwitch.grid(row=2,column=0,sticky=W)
textsandwitch=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_sandwitch)
textsandwitch.grid(row=2,column=1,padx=10,pady=10)


frenchfries=Checkbutton(foodFrame,text="frenchfries",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var4,command=frenchfries)
frenchfries.grid(row=3,column=0,sticky=W)
textfrenchfries=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_frenchfries)
textfrenchfries.grid(row=3,column=1,padx=10,pady=10)


Dalkhichadi=Checkbutton(foodFrame,text="Dalkhichadi",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var5,command=Dalkhichadi)
Dalkhichadi.grid(row=4,column=0,sticky=W)
textDalkhichadi=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Dalkhichadi)
textDalkhichadi.grid(row=4,column=1,padx=10,pady=10)


Biryani=Checkbutton(foodFrame,text="Biryani",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var6,command=Biryani)
Biryani.grid(row=5,column=0,sticky=W)
textBiryani=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Biryani)
textBiryani.grid(row=5,column=1,padx=10,pady=10)


Pulav=Checkbutton(foodFrame,text="Pulav",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var7,command=Pulav)
Pulav.grid(row=6,column=0,sticky=W)
textPulav=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Pulav)
textPulav.grid(row=6,column=1,padx=10,pady=10)


Pasta=Checkbutton(foodFrame,text="Pasta",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var8,command=Pasta)
Pasta.grid(row=7,column=0,sticky=W)
textPasta=Entry(foodFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Pasta)
textPasta.grid(row=7,column=1,padx=10,pady=10)

#Entry fields for drink items

Lassi=Checkbutton(drinksFrame,text="Lassi",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var9,command=Lassi)
Lassi.grid(row=0,column=0,sticky=W)
textLassi=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Lassi)
textLassi.grid(row=0,column=1,padx=10,pady=10)

coffee=Checkbutton(drinksFrame,text="coffee",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var10,command=coffee)
coffee.grid(row=1,column=0,sticky=W)
textcoffee=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1,padx=10,pady=10)

Faluda=Checkbutton(drinksFrame,text="Faluda",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var11,command=Faluda)
Faluda.grid(row=2,column=0,sticky=W)
textFaluda=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_faluda)
textFaluda.grid(row=2,column=1,padx=10,pady=10)

jaljeera=Checkbutton(drinksFrame,text="jaljeera",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var12,command=jaljeera)
jaljeera.grid(row=3,column=0,sticky=W)
textjaljeera=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=3,column=1,padx=10,pady=10)

MasalaTea=Checkbutton(drinksFrame,text="MasalaTea",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var13,command=MasalaTea)
MasalaTea.grid(row=4,column=0,sticky=W)
textMasalaTea=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_MasalaTea)
textMasalaTea.grid(row=4,column=1,padx=10,pady=10)

BadamMilk=Checkbutton(drinksFrame,text="BadamMilk",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var14,command=BadamMilk)
BadamMilk.grid(row=6,column=0,sticky=W)
textBadamMilk=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_BadamMilk)
textBadamMilk.grid(row=6,column=1,padx=10,pady=10)

Roohfzaa=Checkbutton(drinksFrame,text="Roohfzaa",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var15,command=Roohfzaa)
Roohfzaa.grid(row=7,column=0,sticky=W)
textRoohfzaa=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Roohfzaa)
textRoohfzaa.grid(row=7,column=1,padx=10,pady=10)

ColdDrink=Checkbutton(drinksFrame,text="ColdDrink",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var16,command=ColdDrink)
ColdDrink.grid(row=8,column=0,sticky=W)
textColdDrink=Entry(drinksFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_coldDrink)
textColdDrink.grid(row=8,column=1,padx=10,pady=10)



#
# #Entry fields for cakes items

Oreo=Checkbutton(cakesFrame,text="Oreo",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var17,command=Oreo)
Oreo.grid(row=0,column=0,sticky=W)
textOreo=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Oreo)
textOreo.grid(row=0,column=1,padx=10,pady=10)


Apple=Checkbutton(cakesFrame,text="Apple",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var18,command=Apple)
Apple.grid(row=1,column=0,sticky=W)
textApple=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Apple)
textApple.grid(row=1,column=1,padx=10,pady=10)



Kitkat=Checkbutton(cakesFrame,text="Kitkat",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var19,command=Kitkat)
Kitkat.grid(row=2,column=0,sticky=W)
textKitkat=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Kitkat)
textKitkat.grid(row=2,column=1,padx=10,pady=10)

Brownie=Checkbutton(cakesFrame,text="Brownie",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var20,command=Brownie)
Brownie.grid(row=3,column=0,sticky=W)
textBrownie=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Brownie)
textBrownie.grid(row=3,column=1,padx=10,pady=10)

Banana=Checkbutton(cakesFrame,text="Banana",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var21,command=Banana)
Banana.grid(row=4,column=0,sticky=W)
textBanana=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Banana)
textBanana.grid(row=4,column=1,padx=10,pady=10)

Mango=Checkbutton(cakesFrame,text="Mango",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var22,command=Mango)
Mango.grid(row=5,column=0,sticky=W)
textMango=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Mango)
textMango.grid(row=5,column=1,padx=10,pady=10)

Pineapple=Checkbutton(cakesFrame,text="Pineapple",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var23,command=Pineapple)
Pineapple.grid(row=6,column=0,sticky=W)
textPineapple=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_Pineapple)
textPineapple.grid(row=6,column=1,padx=10,pady=10)

Chocolate=Checkbutton(cakesFrame,text="Chocolate",font=('Times New Roman',20),fg="black",onvalue=1,offvalue=0,variable=var24,command=Chocolate)
Chocolate.grid(row=7,column=0,sticky=W)
textChocolate=Entry(cakesFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=20,state=DISABLED,textvariable=e_chocolate)
textChocolate.grid(row=7,column=1,padx=10,pady=10)

#Costlable and entry fields
lableCostofFood=Label(costFrame,text="Cost of Food",font=('Times New Roman',20,'bold'),fg="black",bg="gray")
lableCostofFood.grid(row=0,column=0)
textCostofFood=Entry(costFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=14,textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=10,pady=10)

lableCostofDrinks=Label(costFrame,text="Cost of Drinks",font=('Times New Roman',20,'bold'),fg="black",bg="gray")
lableCostofDrinks.grid(row=1,column=0)
textCostofDrinks=Entry(costFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=14,textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=10,pady=10)

lableCostofCakes=Label(costFrame,text="Cost of Cakes",font=('Times New Roman',20,'bold'),fg="black",bg="gray")
lableCostofCakes.grid(row=2,column=0)
textCostofCakes=Entry(costFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=14,textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=10,pady=10)

lableSubTotal=Label(costFrame,text="Sub Total",font=('Times New Roman',20,'bold'),fg="black",bg="gray")
lableSubTotal.grid(row=0,column=2)
textSubTotal=Entry(costFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=14,textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=10,pady=10)

lableServiceTax=Label(costFrame,text="Service Tax",font=('Times New Roman',20,'bold'),fg="black",bg="gray")
lableServiceTax.grid(row=1,column=2)
textServiceTax=Entry(costFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=14,textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=10,pady=10)

lableTotalCost=Label(costFrame,text="Total Cost",font=('Times New Roman',20,'bold'),fg="black",bg="gray")
lableTotalCost.grid(row=2,column=2)
textTotalCost=Entry(costFrame,font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,width=14,textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=10,pady=10)

#clock
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = tkinter.Label(topFrame, font=('Times New Roman', 20, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center')
time()
#button
buttonTotal = Button(ButtonFrame, text='Total', font=('Times New Roman', 11, 'bold'), bg='white', fg='black',bd=3,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt = Button(ButtonFrame, text='Receipt', font=('Times New Roman', 10, 'bold'), bg='white', fg='black',bd=3,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave = Button(ButtonFrame, text='Save', font=('Times New Roman', 11, 'bold'), bg='white', fg='black',bd=3,command=save)
buttonSave.grid(row=0,column=2)

buttonReset = Button(ButtonFrame, text='Reset', font=('Times New Roman', 11, 'bold'), bg='white', fg='black',bd=3,command=reset)
buttonReset.grid(row=0,column=3)

buttonmenu = Button(ButtonFrame, text='Menu', font=('Times New Roman', 10, 'bold'), bg='white', fg='black',bd=3,command=menu)
buttonmenu.grid(row=0,column=4)


#textareaf
textReceipt=Text(receiptFrame,font=('Times New Roman',10,'bold'),bd=3,relief=RIDGE)
textReceipt.grid(row=1,column=1,padx=5,pady=5)

#calculator
# from tkinter import *

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Main function
if __name__ == "__main__":

    expression = ""
    equation = StringVar()

    expression_field = Entry(calFrame, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    # Creating buttons and placing them in the grid
    button1 = Button(calFrame, text=' 1 ', fg='black', bg='gray',bd=5, command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(calFrame, text=' 2 ', fg='black', bg='gray',bd=5, command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(calFrame, text=' 3 ', fg='black', bg='gray', bd=5,command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(calFrame, text=' 4 ', fg='black', bg='gray', bd=5,command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(calFrame, text=' 5 ', fg='black', bg='gray',bd=5, command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(calFrame, text=' 6 ', fg='black', bg='gray', bd=5,command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(calFrame, text=' 7 ', fg='black', bg='gray', bd=5,command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(calFrame, text=' 8 ', fg='black', bg='gray',bd=5, command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(calFrame, text=' 9 ', fg='black', bg='gray', bd=5,command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(calFrame, text=' 0 ', fg='black', bg='gray',bd=5, command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(calFrame, text=' + ', fg='black', bg='gray',bd=5, command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(calFrame, text=' - ', fg='black', bg='gray', bd=5,command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(calFrame, text=' * ', fg='black', bg='gray',bd=5, command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(calFrame, text=' / ', fg='black', bg='gray',bd=5, command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(calFrame, text=' = ', fg='black', bg='gray',bd=5, command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(calFrame, text='Clear', fg='black', bg='gray',bd=5, command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

root.mainloop()





















