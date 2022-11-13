from cProfile import label
import csv
from tkinter import * 
from tkinter import ttk
import tkinter as tk 
from tkinter import messagebox
from turtle import right

class Front_page(Tk):
    def __init__(self):
        super().__init__()  
        self.geometry('1366x768+0+0')
        self.minsize(width=1366, height=768)
        self.maxsize(width=1600, height=900)
        self.title('shop')
        Label1=Label(text='Welcome To Library Management System',font='Arial 20 bold',fg='maroon1', bg='blue2', padx=10)
        Label1.place(x=400,y=20)
        
        Label2=Label(text=' Book Modification->>>',font='Arial 13 bold',fg='maroon1', bg='blue2', padx=10)
        Label2.place(x=90,y=350)
        self.button1 =Button(self, command=main().add_book,text='ADD BOOK')
        self.button1.place(x=350,y=350)
        self.button2 =Button(self, command=main().delete_book,text='DELETE BOOK')
        self.button2.place(x=550,y=350)
        self.button3 =Button(self, command=main().modify_book,text='MODIFY BOOK')
        self.button3.place(x=750,y=350)

        Label3=Label(text=' Search--------------->>>',font='Arial 13 bold',fg='maroon1', bg='blue2', padx=10)
        Label3.place(x=90,y=420)
        self.button4 =Button(self, command=main().search,text='SEARCH')
        self.button4.place(x=350,y=420)
        # self.button3=ttk.Button(self, command=None,text='user')
        # self.button3.place(x=300,y=450) 

        Label4=Label(text='Member Management>>>',font='Arial 13 bold',fg='maroon1', bg='blue2', padx=3)
        Label4.place(x=90,y=490)
        self.button5 =Button(self, command=main().add_member,text='ADD MEMBER')
        self.button5.place(x=350,y=490)
        self.button6 =Button(self, command=main().delete_member,text='DELETE MEMBER')
        self.button6.place(x=550,y=490)

        Label5=Label(text='Library Management>>>',font='Arial 13 bold',fg='maroon1', bg='blue2', padx=3)
        Label5.place(x=90,y=560)
        self.button7 =Button(self, command=main().checkout,text='CHECKOUT')
        self.button7.place(x=350,y=560)
        self.button8 =Button(self, command=main().return_book,text='RETURN')
        self.button8.place(x=550,y=560)
        self.button9 =Button(self, command=main().reserve,text='RESERVE')
        self.button9.place(x=750,y=560)
        self.button10 =Button(self, command=main().renew,text='RENEW')
        self.button10.place(x=950,y=560)
        
        self.button11 =Button(self, command=main().book_display,text='RENEW')
        self.button11.place(x=650,y=660)

#usage


class main(): 
    def filing(self,a):
        self.list=[]
        with open(a, mode ='r')as file:
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != []]
        self.list = [x for x in self.list if x != ['','','','']]
        return self.list

    def quick_sort(self,given_list):
        if len(given_list) < 1:
            return given_list
        else:
            pivot_element = given_list[0]
#here   I am choosing the first element to be a pivot

        left = self.quick_sort([element for element in given_list[1:] if element < pivot_element])
#moving smaller to left
 
        right = self.quick_sort([element for element in given_list[1:] if element > pivot_element])
#moving greater to right
        return left + [pivot_element] + right
#usage


    def filing1(self,a,r,l):
        self.rows=l
        with open(a, r) as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerows(self.rows)
    def filing2(self,a,r,l):
        with open(a, r) as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerow(l)

    def add_book(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('ADD BOOK')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Information Below',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Enter Books Title>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Enter Books Author>> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Enter Books Subject>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Enter Books Publication date.>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Save Record ', command=self.file_addbook)
        button1.place(x=210,y=440)
    def file_addbook(self):
        self.list=[]
        self.list1=[]
        self.counter=0
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get(),'not reserved','not borrowed',0]
            with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file, dialect='excel') 
                for lines in csvFile: 
                    self.list1.append(lines)
            self.list1 = [x for x in self.list1 if x != ['','','','']]
            self.list1 = [x for x in self.list1 if x != []]
            self.list1.append(self.row)
            del self.list1[0]
            self.list1.insert(0,['Title','Author','Subject','Publication Date','reserved','borrow','week borrowed'])
            with open('H:/dsap2/bookrecord.csv', 'w+') as self.csvfile: 
                csvwriter = csv.writer(self.csvfile,dialect='excel')  
                csvwriter.writerows(self.list1)
            messagebox.showinfo('Book added',f'{self.entry1.get()} is added successfully')
            self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def delete_book(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('DELETE BOOK')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Information Below',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Enter Books Title>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Enter Books Author>> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Enter Books Subject>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Enter Books Publication date.>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Delete Record ', command=self.file_delbook)
        button1.place(x=210,y=440)
    def file_delbook(self):
        self.list=[]
        with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get(),'not reserved','not borrowed','0']
            if self.row in self.list:
                self.list.remove(self.row)
                with open('H:/dsap2/bookrecord.csv', 'w+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerows(self.list) 
                messagebox.showinfo('Book Deleted',f'{self.entry1.get()} is deleted successfully')
                self.new.destroy()
            else:
                messagebox.showinfo('not found','not found')
                self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def modify_book1(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('MODIFY BOOK')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Information Below to Modify',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Enter Books Title>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Enter Books Author>> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Enter Books Subject>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Enter Books Publication date.>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Modify Record ', command=self.file_modbook1)
        button1.place(x=210,y=440)
    def modify_book(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('MODIFY BOOK')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter which book to modify',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Enter Books Title>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Enter Books Author>> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Enter Books Subject>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Enter Books Publication date.>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Modify Record ', command=self.file_modbook)
        button1.place(x=210,y=440)     
    def file_modbook1(self):
        self.list=[]
        with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get(),'not reserved','not borrowed','0']
            self.filing2('H:/dsap2/bookrecord.csv','a+',self.row)
            messagebox.showinfo('Book Added',f'{self.entry1.get()} is modified successfully')
            self.new.destroy()
            self.new.destroy()
                
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()
    def file_modbook(self):
        self.list=[]
        with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get(),'not reserved','not borrowed','0']
            if self.row in self.list:
                self.list.remove(self.row)
                self.modify_book1()
               # self.new.destroy()
                
            else:
                messagebox.showinfo('not found','not found or cant be changed because it is borrowed')
                self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def search_result(self,list):
        self.lists=list
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('Result')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text=f'{self.lists[0]}',font='Arial 10 bold',fg='black',bg='pink2')
        label.place(x=70,y=10)
        Label1=Label(self.new,text=f'{self.lists[1]}',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text=f'{self.lists[2]}',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text=f'{self.lists[3]}',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text=f'{self.lists[4]}',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
        label4=Label(self.new,text=f'{self.lists[5]}',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=400)
    def search(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('SEARCH')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Information Below to Search',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Enter Books Title>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Enter Books Author>> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Enter Books Subject>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Enter Books Publication date.>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Search', command=self.file_search)
        button1.place(x=210,y=440)
    def file_search(self):
        self.list3=[] 
        count=0
        with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list3.append(lines)
        self.list3 = [x for x in self.list3 if x != ['','','',''] ]
        self.list3 = [x for x in self.list3 if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get()]
            for i in range(len(self.list3)):
                if self.list3[i][0:4]==self.row:
                    self.s=self.list3[i]
                    self.new.destroy()
                    self.search_result(self.s)
                    count+=1
                    break
            if count==0:
                    messagebox.showinfo('not found','not found')
                    self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def add_member(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('ADD MEMBER')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Customer Information Below',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Customer  Name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Serial Number    >> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Gender...        >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Registration Date>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Add Member', command=self.file_addmember)
        button1.place(x=210,y=440)     
    def file_addmember(self):
        self.list=[]
        self.counter=0
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get()]
            self.filing2('H:/dsap2/memberrecord.csv','a+',self.row)
            messagebox.showinfo('Book Added',f'{self.entry1.get()} is added successfully')
            self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def delete_member(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('DELETE MEMBER')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Customer Information Below',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Customer  Name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Serial Number    >> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='Gender...        >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='Registration Date>>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Delete Record ', command=self.file_delmember)
        button1.place(x=210,y=440)
    def file_delmember(self):
        self.list=[]
        with open('H:/dsap2/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.row=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get()]
            if self.row in self.list:
                self.list.remove(self.row)
                with open('H:/dsap2/memberrecord.csv', 'w+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerows(self.list) 
                messagebox.showinfo('Mmeber Deleted',f'{self.entry1.get()} is deleted successfully')
                self.new.destroy()
            else:
                messagebox.showinfo('not found','not found')
                self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def checkout(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('CHECKOUT')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Customer and book Information Below to borrow',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Customer  Name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Serial Number    >> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='book name     >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='author name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Checkout', command=self.file_checkout)
        button1.place(x=210,y=440)     
    def file_checkout(self):
        self.list=[]
        self.list1=[]
        self.list2=[]
        self.list4=[]
        self.list3=[]
        count=0
        with open('H:/dsap2/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.list1=[self.entry1.get(),self.entry2.get()]
            for i in  range(len(self.list)):
                if self.list[i][:2]==self.list1:
                    with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                        csvFile = csv.reader(file,dialect='excel') 
                        for lines in csvFile: 
                            self.list2.append(lines)
                    self.list3=[self.entry3.get(),self.entry4.get()]
                    for j in  range(len(self.list2)):
                        if self.list2[j][:2]==self.list3:
                            self.list4=self.list[i][:2]+self.list2[j][:4]+['not reserved','borrowed','1 week']
                            with open('H:/dsap2/borrowrecord.csv', 'a+') as self.csvfile: 
                                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                                csvwriter.writerow(self.list4) 
                            del self.list2[j]
                            self.list2.insert(i,self.list4[2:])
                            with open('H:/dsap2/bookrecord.csv', 'w+') as self.csvfile: 
                                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                                csvwriter.writerows(self.list2) 
                            messagebox.showinfo('checkout',f'you have borrowed {self.entry3.get()}  successfully')
                            self.new.destroy()
                            count+=1
            # if count==0:
            #     messagebox.showinfo('not found','not found')
            #     self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def return_book(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('RETURN')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Customer and book Information Below to Return',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Customer  Name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Serial Number    >> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='book name     >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='author name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Return Book', command=self.returnbook_filing)
        button1.place(x=210,y=440)  
    def returnbook_filing(self):
        self.list=[]
        self.list1=[]
        self.list22=[]
        self.list3=[]
        count=0
        with open('H:/dsap2/borrowrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)

        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        print(self.list)
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.list1=[self.entry1.get(), self.entry2.get(), self.entry3.get(),self.entry4.get()]
            for i in  range(len(self.list)):
                if self.list1==self.list[i][:4]:
                    self.list3=self.list[i][:4]+['not reserved','not borrowed',0]
                    del self.list[i]
                    with open('H:/dsap2/borrowrecord.csv', 'w+') as self.csvfile: 
                                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                                csvwriter.writerows(self.list)
                    # with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                    #     csvFile = csv.reader(file,dialect='excel') 
                    #     for lines in csvFile: 
                    #         self.list22.append(lines)
                    # self.list22 = [x for x in self.list if x != ['','','',''] ]
                    # self.list22 = [x for x in self.list if x != [] ]
                    # del self.list22[i]
                    # self.list22.insert(i,self.list3)
                    # with open('H:/dsap2/bookrecord.csv', 'w+') as self.csvfile: 
                    #             csvwriter = csv.writer(self.csvfile,dialect='excel') 
                    #             csvwriter.writerows(self.list22) 
                    messagebox.showinfo('checkout',f'you have returned{self.entry3.get()}  successfully')
                    self.new.destroy()
                    count+=1
            if count==0:
                    messagebox.showinfo('not found','not found')
                    self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()
                    
    def reserve(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('RESERVE')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Customer and book Information Below to Reserve',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Customer  Name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Serial Number    >> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='book name     >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='author name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Reserve', command=self.reserve_filing)
        button1.place(x=210,y=440)    
    def reserve_filing(self):
        self.list=[]
        self.list1=[]
        self.list2=[]
        self.list4=[]
        self.list3=[]
        count=0
        with open('H:/dsap2/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        with open('H:/dsap2/borrowrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list1.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ]
        self.list1 = [x for x in self.list if x != ['','','',''] ]
        self.list1 = [x for x in self.list if x != [] ]
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.list3=[self.entry1.get(), self.entry2.get()]
            for i in  range(len(self.list)):
                if self.list3==self.list[i][:2]: 
                    for j in  range(len(self.list1)):
                        if self.list1[j][2:4]==[self.entry3.get(),self.entry4.get()]:
                            self.list4=self.list[i][:2]+self.list1[j][0:6]+['reserved','not borrowed',0]
                            with open('H:/dsap2/borrowrecord.csv', 'a+') as self.csvfile: 
                                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                                csvwriter.writerow(self.list4)
                            messagebox.showinfo('checkout',f'you have reserved {self.entry3.get()}  successfully')
                            self.new.destroy()
                            count+=1
            if count==0:
                    messagebox.showinfo('not found','not found')
                    self.new.destroy()
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()
                    
    def renew(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('RENEW')
        #self.new.overrideredirect(True)
        self.new.minsize(width=700,height=550)
        self.new.maxsize(width=550,height=550)
        label=Label(self.new,text='Enter Customer and book Information Below to Reserve',font='Arial 12 bold',fg='black',bg='pink2')
        label.place(x=300,y=10)
        Label1=Label(self.new,text='Customer  Name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label1.place(x=70,y=50)
        Label2=Label(self.new,text='Serial Number    >> ',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label2.place(x=70,y=150)
        Label3=Label(self.new,text='book name     >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        Label3.place(x=70,y=250)
        label4=Label(self.new,text='author name   >>',font='Arial 10 bold',fg='maroon1',bg='blue2')
        label4.place(x=70,y=350)
    
        self.entry1=Entry(self.new)
        self.entry1.place(x=420,y=50)
        self.entry2=Entry(self.new)
        self.entry2.place(x=420,y=150)
        self.entry3=Entry(self.new)
        self.entry3.place(x=420,y=250)
        self.entry4=Entry(self.new)
        self.entry4.place(x=420,y=350)
    
        button1=Button(self.new,text='Renew', command=self.renew_filing)
        button1.place(x=210,y=440)  
    def renew_filing(self):
        self.list=[]
        self.list1=[]
        self.list2=[]
        self.list4=[]
        self.list3=[]
        count=0
        with open('H:/dsap2/borrowrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','',''] ]
        self.list = [x for x in self.list if x != [] ] 
        if self.entry1.get()!='' and self.entry2.get()!='' and self.entry3.get()!='' and self.entry4.get()!='':
            self.list1=[self.entry1.get(), self.entry2.get(),self.entry3.get(), self.entry4.get()]
            for i in  range(len(self.list)):  
                if self.list1==self.list[i][:4]:
                    self.list2=self.list[i][:7]+['reborrowed','1 week']
                    with open('H:/dsap2/borrowrecord.csv', 'a+') as self.csvfile: 
                        csvwriter = csv.writer(self.csvfile,dialect='excel') 
                        csvwriter.writerow(self.list2)
                    messagebox.showinfo('checkout',f'you have renewed {self.entry3.get()} successfully')
                    self.new.destroy()
                    count+=1
        else:
            messagebox.showerror('Error','Enter correct information')
            self.new.destroy()

    def book_display(self):
        self.list=[]
        self.display1= Toplevel()
        self.display1.geometry('900x400+300+120')
        self.display1.minsize(width=900, height=400)
        self.display1.maxsize(width=900, height=400)
        self.display1.title('Record')
        # canvas4 = Canvas(self.display1, height=70, width=750, bg='khaki4')
        # canvas4.pack()
        # # button01=Button(canvas4,text='EXIT',command=self.display1.destroy())
        # # button01.pack(side=RIGHT)
        # self.label1=Label(canvas4,text='none')
        # self.label1.pack(side=LEFT,padx=200)
        # canvas5=Canvas(self.display1, height=70, width=750, bg='khaki4')
        # canvas5.pack()
        # for k, res in enumerate(self.list):
        #     self.price+=round(res[3],0)
        with open('H:/dsap2/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file, dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','','']]
        self.list = [x for x in self.list if x != []]
        del self.list[0]
        self.label3=Label(self.display1,text=' \t\t     Title      \t     Author     \t       Subject      \t           Borrowed  ')
        self.label3.pack(padx=0,anchor=W)
        scrollbar = Scrollbar(self.display1)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.listbox = Listbox(self.display1, width=110, height=45,bg='#D0E6D7',fg='#465961',highlightcolor='#8DC6B0',highlightbackground='#B98DC6',highlightthickness=10,selectbackground='#B98DC6'  )
        self.listbox.pack()
        for i in  range(len(self.list)):
            t=str(self.list[i][0])+'--------------------'+str(self.list[i][1])+'--------------------'+str(self.list[i][2])+'---------------- '+str(self.list[i][5])
            self.listbox.insert(i,t)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)




    # def login(self):
    #     self.main=Toplevel()
    #     self.main.destroy
    #     self.main.geometry('550x550+420+150')
    #     self.main.title('Customer Login') 
    #     self.main.resizable(FALSE, FALSE)
    #     photo = PhotoImage(file = "E:/OOP Project/images.png")
    #     self.main.iconphoto(False, photo)
    #     self.main.minsize(width=550,height=550)
    #     self.main.maxsize(width=550,height=550) 
    #     frame=Frame(self.main,bg='#5D6D7E',bd=5)
    #     frame.grid(row=0,column=0,sticky=NW)
    #     # frontp1 = ImageTk.PhotoImage(Image.open('background/final.jpg').resize((550,550), Image.ANTIALIAS))
    #     self.main.overrideredirect(True)
    #     #self.bg_image = Label(frame, image=self.bg).grid(row=10,column=10 )
    #     Label1=Label(frame,text='Email',font='Arial 15 bold',fg='maroon1', bg='blue2', padx=10)
    #     Label1.place(x=100,y=200)
    #     Label2=Label(frame,text='Password',font='Arial 15 bold',fg='maroon1',bg='blue2', padx=10)
    #     Label2.place(x=90,y=280)
    #     self.entry_1=Entry(frame)
    #     self.entry_1.place(x=220,y=200)
    #     self.entry_2=Entry(frame,show="*")
    #     self.entry_2.place(x=220,y=280)
    #     global photo_1,photo_2,photo_3
    #     photo_3 = ImageTk.PhotoImage(Image.open('E:/OOP Project/background/user.jpg').resize((150,150), Image.ANTIALIAS))
    #     Label(frame, image=photo_3, bg='navy blue').place(x=200, y=20)
    #     photo_1 = ImageTk.PhotoImage(Image.open('E:/OOP Project/button/loginb.png').resize((100,50), Image.ANTIALIAS))
    #     button1 =Button(self.main, command=self.file_login,width=100,height=50,border=0,image=photo_1)
    #     button1.place(x=240,y=350)
    #     photo_2 = ImageTk.PhotoImage(Image.open('E:/OOP Project/button/exit.png').resize((80,30), Image.ANTIALIAS))
    #     button3=Button(self.main, command=self.main.destroy,width=80,height=30,border=0,image=photo_2)
    #     button3.place(x=250,y=450) 





if __name__ == "__main__":
    root= Front_page()
    root.mainloop()
