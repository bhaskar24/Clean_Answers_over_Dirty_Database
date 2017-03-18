from Tkinter import *
import tkMessageBox
import Tkinter
from prettytable import PrettyTable

global loyaltyCard
global customer

loyaltyCard = PrettyTable(['cardId', 'custFk', 'prob'])
loyaltyCard.add_row([111, 'c1', 0.4])
loyaltyCard.add_row([111, 'c2', 0.6])

customer = PrettyTable(['custId', 'name', 'income', 'prob'])
customer.add_row(['c1', 'John', 120, 0.9])
customer.add_row(['c1', 'John', 80, 0.1])
customer.add_row(['c1', 'Mary', 140, 0.4])
customer.add_row(['c1', 'Marion', 40, 0.6])

def tab_init():
   global customer
   global loyaltyCard
   
   from prettytable import from_csv
   fp = open("./tables/customer.csv", "r")
   customer = from_csv(fp)
   fp.close()
   
   from prettytable import from_csv
   fp = open("./tables/loyaltyCard.csv", "r")
   loyaltyCard = from_csv(fp)
   fp.close()

   print customer
   print loyaltyCard

def tab_print(table_name):
   import glob
   tables = glob.glob('./tables/*.csv')
   for i in tables:
      if table_name in i.replace('./tables/','').replace('.csv',''):
         from prettytable import from_csv
         fp = open("./tables/"+table_name+".csv", "r")
         customer = from_csv(fp)
         fp.close()
         #text2.delete('1.0', END) #For delete the text from input box
         text2.insert(INSERT, '\n\n')
         text2.insert(INSERT,customer)
def tab_print_proj(col, table_name):
   import glob
   tables = glob.glob('./tables/*.csv')
   for i in tables:
      if table_name in i.replace('./tables/','').replace('.csv',''):
         from prettytable import from_csv
         fp = open("./tables/"+table_name+".csv", "r")
         customer = from_csv(fp)
         fp.close()
         text2.delete('1.0', END) #For delete the text from input box
         #text2.insert(INSERT, '\n\n')
#         text2.insert(INSERT,customer)
#         print col
         print customer.get_string(fields=col)#["City name", "Population"])
         text2.insert(INSERT, customer.get_string(fields=col))#["City name", "Population"]))
def inp():
   inp=text.get('1.0', END)
   inp=inp.replace('select','').replace('from','').replace('  ',' ')
   inp=inp.strip()
   inp=inp.split(' ')
   print len(inp)
   if len(inp)==2:
      if '*' in inp[0]:
         tab_print(inp[1])
      else:
         col = inp[0].split(',')
         tab_print_proj(col, inp[1])
      
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

def checkbutton_value1():
   if(var1.get()):
      var2.set(0)

def checkbutton_value2():
   if(var2.get()):
      var1.set(0)

def tb(obj, table):
    obj.insert(INSERT,table)#print t

def widget_init(top):
   global L1
   global L2
   global text
   global text2
   global C1
   global C2
   global bluebutton
   global blckbutton

   L1 = Label(top, text="Enter your Select / Join Query Here")
   L2 = Label(top, text="Output of your Query")

   text = Text(top, wrap="word", background="white", borderwidth=0, highlightthickness=1)
#   text.config(font=("consolas", 12), undo=True, wrap='word')

   text2 = Text(top, wrap="word", background="white", borderwidth=0, highlightthickness=1)

   CheckVar1 = IntVar()
   CheckVar2 = IntVar()
   var1 = IntVar()
   var2 = IntVar()
   var = IntVar()

   C1 = Checkbutton(top, text = "Simple SQL without Query Re-writing", variable = checkbutton_value1, \
                    onvalue = 1, offvalue = 0, height=2, width = 40)
   C2 = Checkbutton(top, text = "Simple SQL with Query Re-writing", variable = checkbutton_value1, \
                    onvalue = 1, offvalue = 0, height=2, width = 40)
   label=Label(top)

   bluebutton = Button(top, text="Evaluate", width=40, fg="black", command=inp)#tb(text2, customer))
   blckbutton = Button(top, text="Exit", width=40, fg="black", command=quit)

   '''
   TextArea = Text()
   ScrollBar = Scrollbar(root)
   ScrollBar.config(command=TextArea.yview)
   TextArea.config(yscrollcommand=ScrollBar.set)
   ScrollBar.pack(side=RIGHT, fill=Y)
   TextArea.pack(expand=YES, fill=BOTH)
   '''
def widget_grid():
   L1.grid(row=0, column=1)
   L2.grid(row=0, column=2)
   text.grid(row=1, column=1)
   text2.grid(row=1, column=2)
   C1.grid(row=2, column=1)
   C2.grid(row=2, column=2)
   bluebutton.grid(row=3, column=1)
   blckbutton.grid(row=3, column=2)

if __name__=='__main__':
   global top

#   tab_init()
   top = Tkinter.Tk()
   top.resizable(width=False, height=False)
   top.wm_title("Clean Answers over Dirty Database: Using Probabilistic Approach- DDBMS Course Project - Bhaskar Gautam <bhaskar.16cs04f@nitk.edu.in> II sem")

   widget_init(top)
   widget_grid()

   top.mainloop()
