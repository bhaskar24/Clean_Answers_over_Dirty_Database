from Tkinter import *
import tkMessageBox
import Tkinter
from prettytable import PrettyTable

global loyaltyCard
global customer

def toggle_Value1():
    if(var1.get()):
       var2.set(0)

def toggle_Value2():
    if(var2.get()):
       var1.set(0)

def reg(s):
   import re

   if re.findall('\d>\d', s) or re.findall('\d<\d', s) or re.findall('\d==\d', s) or re.findall('\d!=\d', s) or re.findall('\d!>\d', s) or re.findall('\d!<\d', s):
	   return eval(s)
   else:
      if '==' in s:
         s=s.split("==")
         if s[0].lower()==s[1].lower():
            return True
         else:
            return False
      elif '>' in s:
         s=s.split(">")
         if s[0].lower()>s[1].lower():
            return True
         else:
            return False
      elif '<' in s:
         s=s.split("<")
         if s[0].lower()>s[1].lower():
            return True
         else:
            return False
      elif '!=' in s:
         s=s.split("!=")
         if s[0].lower()>s[1].lower():
            return True
         else:
            return False
      elif '!>' in s:
         s=s.split("!>")
         if s[0].lower()>s[1].lower():
            return True
         else:
            return False
      elif '!<' in s:
         s=s.split("!<")
         if s[0].lower()>s[1].lower():
            return True
         else:
            return False
      else:
         return False
def sum_columns(columns,status):
    #input ex:
    #sum(o.prob* c*prob)    -> Status.True
    #   or
    #sum(prob)              -> Status.False
    #status means contain further calculation in column list?
    #this function returns the calculated value and update the columns in tmp.csv

    #call
    #print sum_columns('sum(prob*income)',True)
    #print sum_columns('sum(income)',False)

    sm=0    
    if status is False:
        if 'sum(' in columns:
            clm=columns.replace('sum(','').replace(')','')
            import csv
            fr=open('./tables/tmp.csv','r')
            fr = csv.DictReader(fr)
            cnt=0
            for tuple_T in fr:
                sm = sm + float(tuple_T[clm])
            return sm
    else:
        if 'sum(' in columns:
            clm=columns.replace('sum(','').replace(')','')
            clm=clm.split('*')
            #print clm
            import csv
            fr=open('./tables/tmp.csv','r')
            fr = csv.DictReader(fr)
            cnt=0
            for tuple_T in fr:
                sm = sm + eval( tuple_T[clm[0]]+'*'+tuple_T[clm[1]] )
            return sm
    
def tmp_csv(table_name, conditions, status):
   if status is True:
       import os
       from shutil import copyfile
       cross_prod(table_name)
       table_name='cond_tmp.csv'
       copyfile('./tables/tmp.csv', './tables/'+table_name+'.csv')

   fp = open("./tables/"+table_name+".csv", "r")
   # save the require tuples in tmp.csv then that require tuple retrieve by following print function
   fw = open("./tables/tmp.csv", "w")
   cond_list=conditions.strip()
   if ' or ' not in cond_list:
      cond_list=cond_list.split('and')
      tmpL=[] #tell the position of header in table
      cnt=0
      c=0
      s=[]
      cnd_s=0
      for i in cond_list:
         if cnd_s>0:
            fw.close()
            import csv
            fp=open("./tables/tmp.csv", "r")
            fp=csv.reader(fp, delimiter = ',')
            fw=open("./tables/tmp1.csv", "w")
         for row in fp:
            if c==0:
               s=row
#               print s
               try:
                  s=s.split(',')
               except:
                  pass
#               print s
               for j in s:
                  jj=j.replace('"','').replace('\n','')
                  if jj in i:
                     tmpL.append(cnt)
#                     print jj
#                     print tmpL
#                     print cnt
                  cnt=cnt+1
               if cnd_s==0:
                  fw.write(row)
               else:
                  # make into "" and string
#                  print row
                  row=str(row).replace('[','').replace(']','').replace("'",'')
                  
                  fw.write(row+'\n')
               c=c+1            
            else:
               if '>' in i or '<' in i or '=' in i or '!' in i:
                  if '=' in i and '==' not in i:
                     i=i.replace('=','==')
                  if cnd_s==0:
                     row1=row
#                     print row
                     row=row.replace('\n','')
                  else:
                     row=','.join(row)
#                     print row
                     row1=str(row)
                     row=row.replace('\n','')
#                  print row
#                  print i
                  #assuming only one codition available
#                  print 'Pos'
#                  print tmpL
#                  print s
                  sf=s[tmpL[0]].replace('"','').replace('\n','')
                  rw=row.split(',')
                  rw=rw[tmpL[0]].replace("'",'').replace('\n','')
                  sw=i.replace(sf,rw)
#                  print sw
#                  print sf
#                  print rw
#                  print reg(sw)
                  if reg(sw) is True and '.' not in sw:
#                     print row1
                     if cnd_s>0:
                        fw.write(row1+'\n')
#                        print 'write'
                     else:
                        fw.write(row1)
#                        print 'write'
                  else:
                      sf=s[tmpL[1]].replace('"','').replace('\n','')
                      rw=row.split(',')
                      rw=rw[tmpL[1]].replace("'",'').replace('\n','')
                      sw=sw.replace(sf,rw)
#                      print sw
#                      print sf
#                      print rw
                      if reg(sw) is True and '.' not in sw:
    #                     print row1
                         if cnd_s>0:
                            fw.write(row1+'\n')
    #                        print 'write'
                         else:
                            fw.write(row1)
    #                        print 'write'

         s=[]
         cnt=0
         c=0
         tmpL=[]
#         print i
#         print 'val: '+str(cnd_s)
         if cnd_s>0:
            from shutil import copyfile
            import os
            os.remove('./tables/tmp.csv')
            fw.close()
#            print 'del'
            copyfile('./tables/tmp1.csv', './tables/tmp.csv')
#            print 'copied'
         cnd_s=cnd_s+1
   try:
      fw.close()
   except:
      pass
   print 'Done'
   return True
def cross_prod(tab_list):
    #As per the cited paper they are using cross product of only two tables
    print tab_list
    tab_list=tab_list.split(',')
    fw=open('./tables/tmp.csv','w')
    import glob
    tLis=glob.glob('./tables/*.csv')
    tmp=[]
    for i in tLis:
        tmp.append(i.replace('./tables/','').replace('.csv',''))
    tLis=tmp
#    print tLis
    c1=0
    c2=0
    print tab_list
    if tab_list[0] in tLis and tab_list[1] in tLis or tab_list[0] in tLis:
        fr=open('./tables/'+tab_list[0]+'.csv', 'r')
        fr2=open('./tables/'+tab_list[1]+'.csv', 'r')
        for row_t1 in fr:
            if c2<1:
                for row_t2 in fr2:
                    if c1<1:
                        tmpR=row_t1.replace('\n','').replace('"','')
                        tmpR=tmpR.split(',')
                        tc=0
                        rt=""
                        for tR in tmpR:
                            if tc!=len(tmpR)-1:
                                rt=rt+tab_list[0]+'.'+tR+','
                            else:
                                rt=rt+tab_list[0]+'.'+tR
                            tc=tc+1
                        tmpR=row_t2.replace('\n','').replace('"','')
                        tmpR=tmpR.split(',')
                        tc=0
                        rt2=""
                        for tR in tmpR:
                            if tc!=len(tmpR)-1:
                                rt2=rt2+tab_list[1]+'.'+tR+','
                            else:
                                rt2=rt2+tab_list[1]+'.'+tR
                            tc=tc+1
                        fw.write(rt+','+rt2+'\n')
                        break
                    else:
                        c1=c1+1
                break
            else:
                c2=c2+1
    c1=0
    c2=0
    if tab_list[0] in tLis and tab_list[1] in tLis:
        fr=open('./tables/'+tab_list[0]+'.csv', 'r')
        fr2=open('./tables/'+tab_list[1]+'.csv', 'r')

        for row_t1 in fr:
            if c2>0:
#                print row_t1.replace('\n',''), c2
                for row_t2 in fr2:
                    if c1>0:
#                        print row_t2.replace('\n',''),c1
                        fw.write(row_t1.replace('\n','')+','+row_t2)
                    c1=c1+1
                fr2=open('./tables/'+tab_list[1]+'.csv', 'r')                        
                c1=0
            c2=c2+1
    fw.close()
    fr.close()
    fr2.close()

def tab_print(table_name2, status):
   print table_name2
   import glob
   tables = glob.glob('./tables/*.csv')
   table_name=table_name2.split(',')
   print table_name
   if status==False:
       for i in tables:
          if table_name[0] in i.replace('./tables/','').replace('.csv',''):
             from prettytable import from_csv
             fp = open("./tables/"+table_name[0]+".csv", "r")
             customer = from_csv(fp)
             fp.close()
             text2.delete('1.0', END) #For delete the text from input box
             #text2.insert(INSERT, '\n\n')
             text2.insert(INSERT,customer)
   elif status==True:
        cross_prod(table_name2)
        from prettytable import from_csv
        fp = open("./tables/tmp.csv", "r")
        customer = from_csv(fp)
        fp.close()
        text2.delete('1.0', END) #For delete the text from input box
         #text2.insert(INSERT, '\n\n')
        text2.insert(INSERT,customer)

def tab_print_cond(col, table_name, conditions, status):
   tmp_csv(table_name, conditions, status)
   import glob
   tables = glob.glob('./tables/*.csv')
   if status is False:
       for i in tables:
          if table_name in i.replace('./tables/','').replace('.csv',''):
             if ',' not in col:
                 #filter the table based on tuples val
                 from prettytable import from_csv
                 fp = open("./tables/tmp.csv", "r")
                 customer = from_csv(fp)
                 fp.close()
                 text2.delete('1.0', END)
                 #text2.insert(INSERT, '\n\n')
                 if '*' in col:
                     text2.insert(INSERT,customer)
                 else:
                     if type(col) is not list:
                         col=col.split(',')
                     text2.insert(INSERT, customer.get_string(fields=col))
             else:
                 col=col.split(',')
                 tab_print_proj(col, 'tmp', False)
   else:
       table_name=table_name.split(',')
       print table_name
       for i in tables:
          if table_name[0] in i.replace('./tables/','').replace('.csv','') or table_name[0] in i.replace('./tables/','').replace('.csv',''):
             if ',' not in col:
                 from prettytable import from_csv
                 fp = open("./tables/tmp.csv", "r")
                 customer = from_csv(fp)
                 fp.close()
                 text2.delete('1.0', END) #For delete the text from input box
                 text2.insert(INSERT,customer)
             else:
                 col=col.split(',')
                 tab_print_proj(col, 'tmp', False)
        
def tab_print_proj(col, table_name, status):
   import glob
   tables = glob.glob('./tables/*.csv')
   if status is False:
       for i in tables:
          if table_name in i.replace('./tables/','').replace('.csv',''):
             from prettytable import from_csv
             fp = open("./tables/"+table_name+".csv", "r")
             customer = from_csv(fp)
             fp.close()
             text2.delete('1.0', END) #For delete the text from input box
             print customer.get_string(fields=col)
             text2.insert(INSERT, customer.get_string(fields=col))
   else:
       cross_prod(table_name)
       tables = glob.glob('./tables/*.csv')
       table_name=table_name.split(',')
       for i in tables:
           if table_name[0] in i.replace('./tables/','').replace('.csv','') or  table_name[1] in i.replace('./tables/','').replace('.csv',''):
               from prettytable import from_csv
               fp = open("./tables/tmp.csv", "r")
               customer = from_csv(fp)
               fp.close()
               text2.delete('1.0', END) #For delete the text from input box
               print customer.get_string(fields=col)
               text2.insert(INSERT, customer.get_string(fields=col))
def group(tble,grpBy):
    #input       tble, grpBy
    #Example customer, id
    '''
    import operator
    from prettytable import PrettyTable
    table = PrettyTable(["Name", "Grade"])
    table.add_row(["Alice", 90])
    print table.get_string(sort_key=operator.itemgetter(1, 0), sortby="Grade")
    '''
    if ',' not in grpBy:
        from prettytable import from_csv
        fp = open("./tables/"+tble+".csv", "r")
        customer = from_csv(fp)
        fp.close()
        fp=open('./tables/tmpGroup.csv','w')
        s=customer.get_string(sortby=grpBy).replace('+','').replace(' | ',',').replace('-','').replace('| ','').replace(' |','').strip()
        s= s.replace(' ','').replace('\n\n','\n')
        fp.write(s)
        fp.close()
    #return table ie tmp.csv ordered by grpBy
def form_table(col,start,end,c):
    diff=end-start
    for row_c in range(0,diff):
        fw=open('./tables/tmp'+str(row_c)+'.csv','w')
        from prettytable import from_csv
        fp = open("./tables/tmp.csv", "r")
        customer = from_csv(fp)
        fp.close()
        fp=fw
        s=customer.get_string(start=start,end=end).replace('+','').replace(' | ',',').replace('-','').replace('| ','').replace(' |','').strip()
        s= s.replace(' ','').replace('\n\n','\n')
        fp.write(s)
        fp.close()
    diff=end-start
    import csv
    col_l=col.split(',')
    Dic={}
    print "./tables/tmp"+str(c)+".csv"
    fp = open("./tables/tmp"+str(row_c)+".csv", "r")
    reader = csv.DictReader(fp,delimiter=',')
    for row in reader:
        for attrib in col_l:
            if 'sum(' not in attrib:
                try:
                    Dic[attrib]=row[attrib]
                except:
                    pass
            else:
                try:
                    attrib=attrib.replace('sum(','').replace(')','')
                    Dic[attrib]=Dic[attrib]+float(row[attrib])
                except:
                    attrib=attrib.replace('sum(','').replace(')','')
                    Dic[attrib]=float(row[attrib])
        #print Dic
    print Dic
#    for i,j in Dic.iteritems():
#        fnlW.write()
    reader=''
    with open('./tables/tmpGroup.csv','a') as fnlW:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(fnlW, Dic.keys())
#        w.writeheader()
        w.writerow(Dic)
    print '\n'
    fp.close()
    #return tmp.csv having clustered columns 
def tab_print_grpBy(col,tble,cond,grpBy):
    #qry=[u'id,sum(prob)', u'customer', u'balance>10', u'id']
    #col=inp[0]
    #tble=inp[1]
    #cond=inp[2]
    #grpBy=inp[3]

    group(tble,grpBy)
    tmp_csv('tmpGroup', cond, False) 

    if '*' in col and 'sum(' not in col:
        from prettytable import from_csv
        fp = open("./tables/tmp.csv", "r")
        customer = from_csv(fp)
        fp.close()
        text2.delete('1.0', END) #For delete the text from input box
        text2.insert(INSERT, customer)
    else:
        #sum(o.prob* c*prob)    -> Status.True
        #sum(prob)              -> Status.False
        #status means contain further calculation in column list?
        #this function returns the calculated value and update the columns in tmp.csv
        col_l=col.split(',')
        
        if '*' not in col and 'sum(' in col:            
            # find start and end of groups
            import csv
            start=-1
            end=0
            fr = open('./tables/tmp.csv','r')
            fr = csv.DictReader(fr)
            Dic={}
            ls=[]
            for row in fr:
                try:
                    e=Dic[row[grpBy]]
                    end=ls[1]
                    ls=[]
                    end=end+1
                    ls.append(start)
                    ls.append(end)       
                    Dic[row[grpBy]] = ls
                except:
                    ls=[]
                    start=end
                    end=end+1
                    ls.append(start)
                    ls.append(end)
                    Dic[row[grpBy]]=ls
            grps=[]
            for i,j in Dic.iteritems():
                grps.append(j)
            grps.sort()
            print 'Atrib '+ col
            c=0
            import os
            os.remove('./tables/tmpGroup.csv')
            col_l=col.split(',')
            Dic={}
            for attrib in col_l:
                if 'sum(' not in attrib:
                    try:
                        Dic[attrib]=attrib
                    except:
                        pass
                else:
                    try:
                        attrib=attrib.replace('sum(','').replace(')','')
                        Dic[attrib]=attrib
                    except:
                        pass
            with open('./tables/tmpGroup.csv','a') as fnlW:  # Just use 'w' mode in 3.x
                w = csv.DictWriter(fnlW, Dic.keys())
                w.writerow(Dic)
            fnlW.close()
            for i in grps:
                print i
                start=i[0]
                end  =i[1]
                form_table(col,start,end,c)
                c=c+1
            from prettytable import from_csv
            fp = open('./tables/tmpGroup.csv','r')
            customer = from_csv(fp)
            text2.delete('1.0', END) #For delete the text from input box
            text2.insert(INSERT, customer)

            #print sum_columns('sum(prob*income)',True)
            #print sum_columns('sum(income)',False)

def inp():
   inp=text.get('1.0', END)
   inp=inp.replace('select','').replace('from','').replace('where','').replace('groupby','').replace('  ',' ')
   inp=inp.strip()
   inp=inp.split(' ')
   print len(inp)
   print inp
   status=False
   if len(inp)==2:
      if '*' in inp[0]:
          if ',' not in inp[1]:
              tab_print(inp[1], False)
          else:
              tab_print(inp[1], True)
      else:
         col = inp[0].split(',')
         #if ',' not in inp[1]: 
         if ',' not in inp[1]:
             tab_print_proj(col, inp[1], False)
         else:
             tab_print_proj(col, inp[1], True)

   #lst=nma,shyam column,col2 cod>1
   if len(inp)==3:
      col=inp[0]
      tble=inp[1]
      cond=inp[2]
      print 'Tuple'+inp[0]
      if ',' not in inp[1]:
          tab_print_cond(col, tble, cond, False)
      else:
          tab_print_cond(col, tble, cond, True)
   if len(inp)==4:
       #qry=[u'id,sum(prob)', u'customer', u'balance>10', u'id']
       col=inp[0]
       tble=inp[1]
       cond=inp[2]
       grpBy=inp[3]
       tab_print_grpBy(col,tble,cond,grpBy)

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
    obj.insert(INSERT,table)

def widget_init(top):
   global L1
   global L2
   global text
   global text2
   global C1
   global C2
   global bluebutton
   global blckbutton
   global var1
   global var2
   global ScrollBar
   global scrollb
   
   L1 = Label(top, text="Enter your Select / Join Query Here")
   L2 = Label(top, text="Output of your Query")

   text = Text(top, wrap="word", background="white", borderwidth=0, highlightthickness=1)

   xscrollbar = Scrollbar(top, orient=HORIZONTAL)
   xscrollbar.grid(row=2, column=2)

   yscrollbar = Scrollbar(top, orient=VERTICAL)
   yscrollbar.grid(row=1, column=3)
   
   text2 = Text(top, wrap="word", background="white", borderwidth=0, highlightthickness=1, xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)
   
   xscrollbar.config(command=text2.xview)
   yscrollbar.config(command=text2.yview)
   
   var1 = IntVar()
   
   var2 = IntVar()
   
   C1 = Checkbutton(top, text = "Simple SQL without Query Re-writing", variable = var1, onvalue = 1, offvalue = 0, height=2, width = 40, command = toggle_Value1)
   C1.select()
   C2 = Checkbutton(top, text = "Simple SQL with Query Re-writing", variable = var2, onvalue = 1, offvalue = 0, height=2, width = 40, command = toggle_Value2)

   label=Label(top)

   bluebutton = Button(top, text="Evaluate", width=40, fg="black", command=inp)
   blckbutton = Button(top, text="Exit", width=40, fg="black", command=quit)

def widget_grid():
   L1.grid(row=0, column=1)
   L2.grid(row=0, column=2)

   text.grid(row=1, column=1)
   text2.grid(row=1, column=2)
#   ScrollBar.grid(row=1, column=3)
   
   #text2.grid(row=1, column=3, sticky="nsew")#, padx=2, pady=2)
 #  scrollb.grid(row=2, column=3)
   
#   ScrollBar.xscrollbar.grid(row=2, column=3)
   C1.grid(row=2, column=1)
   C2.grid(row=2, column=2)
   
   bluebutton.grid(row=3, column=1)
   blckbutton.grid(row=3, column=2)

if __name__=='__main__':
   global top

   top = Tkinter.Tk()
   top.resizable(width=False, height=False)
   top.wm_title("Clean Answers over Dirty Database: Using Probabilistic Approach- DDBMS Course Project - Bhaskar Gautam <bhaskar.16cs04f@nitk.edu.in> II sem")

   widget_init(top)
   widget_grid()

#   print sum_columns('sum(prob*balance)',True)
   #print sum_columns('sum(balance)',False)
   #qry=[u'id,sum(prob)', u'customer', u'balance>10', u'id']
   col='id,sum(prob)'
   tble='customer'
   cond='balance>10'
   grpBy='id'
#   tab_print_grpBy(col,tble,cond,grpBy)
   top.mainloop()
