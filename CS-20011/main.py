import csv

##
class quicksort():
    def __init__(self,array):
        self.array=array
        self.sort(self.array, 0, len(self.array) - 1)

    def sort(self,array, left, right):
        if left >= right:
            return array
        pivot = self.array[(left + right) // 2]
        index = self.partition(self.array, left, right, pivot)

        self.sort(self.array, left, index - 1)
        self.sort(self.array, index, right)

    def partition(self,array, left, right, pivot):
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1

            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return left


class adm(quicksort):
    def add(self):
        self.list=[]
        with open('H:/dsap1/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','','']]
        self.a1=input('enter title , author , subject and publication date (separated by comma) = ')
        self.a1=self.a1.split(',')
        self.list.append(self.a1)
        del self.list[0]
        a=quicksort(self.list) 
        self.list.insert(0,['title','author','subject','publicatiom date'])
        with open('H:/dsap1/bookrecord.csv', 'w+') as self.csvfile: 
            csvwriter = csv.writer(self.csvfile,dialect='excel')  
            csvwriter.writerows(self.list)
        print('book entered successfully')
        

    def delete(self):
        self.list=[]
        count=0
        self.a2=input('enter title or author or subject or publication date to delete = ')
        with open('H:/dsap1/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x !=[] ]
        
        for i in range (len(self.list)):
            for j in range (0,4):
                if len(self.list)>=i:
                    if self.list[i][j]==self.a2:
                        a2=input(f'do you want to delete {self.list[i]}(y/n)=')
                        if a2=='y':
                            self.list.pop(i)
                            with open('H:/dsap1/bookrecord.csv', 'w+') as self.csvfile: 
                                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                                csvwriter.writerows(self.list)
                            print('deleted')
                            count+=1
                        break      
        if count!=0:
            print('no record found')

    def modify(self):
        self.list=[]
        self.a3=input('enter what do you want to modify = ')
        with open('H:/dsap1/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != []]
        for i in range (len(self.list)):
            for j in range (len(self.list[i])):
                if self.list[i][j]==self.a3:
                    a3=input(f'do you want to modify {self.list[i]}(y/n)=')
                    if a3=='y':
                        self.list.pop(i)
                        self.aa3=input('enter title , author , subject and publication date (separated by comma) = ')
                        self.aa3=self.aa3.split(',')
                        self.row=[self.aa3]
                        with open('H:/dsap1/bookrecord.csv', 'a') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerow(self.row) 
                        print('modified successfully')
                    elif a3=='n':break

    def __init__(self,work) :
        self.work=work
        if self.work=='add':self.add()
        elif self.work=='delete':self.delete()
        elif self.work=='modify':self.modify()
        else:print('sorry')
    
            ##class for searching
class search():
    def searchh(self):
        self.list=[]
        self.item=input('enter title or author or subject or publication date to search =')
        with open('H:/dsap1/bookrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != ['','','','']]
        count=0
        for i in range (len(self.list)):
            for j in range (len(self.list[i])):
                if self.list[i][j]==self.item:
                    print(self.list[i])
                    count+=1
        if count==0:
            print('no record found')

    def __init__(self): 
        self.searchh()


        ##class for adding member and deleting member
class membership():
    def addmember(self):
        self.x=input('enter name ,serial number,gender,registration date(separated by commas)=')
        self.x=self.x.split(',')
        self.row=[self.x]
        with open('H:/dsap1/memberrecord.csv', 'a') as self.csvfile: 
            csvwriter = csv.writer(self.csvfile,dialect='excel')  
            csvwriter.writerows(self.row)
        print('member added successfully')

    def delmember(self):
        self.list=[]
        self.a2=(input('enter serial number to delete = '))
        with open('H:/dsap1/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != []]
        for i in range (len(self.list)):
            if self.list[i][1]==self.a2:
                a3=input(f'do you want to delete {self.list[i]}( enter y/n)=')
                if a3=='y':
                    self.list.pop(i)
                    self.list = [x for x in self.list if x != ['','','','']]
                    with open('H:/dsap1/memberrecord.csv', 'w+') as self.csvfile: 
                        csvwriter = csv.writer(self.csvfile,dialect='excel') 
                        csvwriter.writerows(self.list)
                break
        print('deleted')
    
    def __init__(self,member):
        self.member=member
        if self.member=='add':
            self.addmember()
        elif self.member=='delete':
            self.delmember()

        ##class for book management
class management():
    def __init__(self,ss):
        self.s3=ss
        if self.s3=='checkout':
            self.checkout()
        elif self.s3=='renew':
            self.renew()
        elif self.s3=='reserve':
            self.reserve()
        elif self.s3=='return':
            self.returnn()

    def checkout(self):
        self.list=[]
        self.listt=[]
        self.list2=[]
        count=0
        count1=0
        self.s=input('enter serial no of the customer=')
        with open('H:/dsap1/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list.append(lines)
        self.list = [x for x in self.list if x != []]
        for i in range (len(self.list)):
            if self.list[i][1]==str(self.s):
                self.list2=self.list[i][0:2]
                m1=input('enter name of book you want to borrow=')
                with open('H:/dsap1/bookrecord.csv', mode ='r')as file: 
                    csvFile = csv.reader(file,dialect='excel') 
                    for lines in csvFile: 
                        self.listt.append(lines)
                self.listt = [x for x in self.listt if x != ['','','','']]
                self.listt = [x for x in self.listt if x != []]
                for i in range (len(self.list)):
                    if m1==self.listt[i][0]:
                        print('you have borrowed this book for 1 week')
                        self.list2+=self.listt[i][0:3]
                        self.list2.append('1 week')
                        count1+=1
                if count1==0:
                    print('this book is already borrowed reborrow or reserve in the menu')
                    break
                self.list2.extend(['not reborrowed','not reserved'])
                
                with open('H:/dsap1/borrowrecord.csv', 'a+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerow(self.list2)
                del self.listt[i]
                self.listt = [x for x in self.listt if x != []]
                
                with open('H:/dsap1/bookrecord.csv', 'w+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerows(self.listt)
                count+=1
                break
            
      
        
    def renew(self):
        self.list3=[]
        self.list33=[]
        count=0
        with open('H:/dsap1/borrowrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list3.append(lines)
        self.list3= [x for x in self.list3 if x != []]
        self.s=input('enter serial no of the customer=')
        for i in range (len(self.list3)):
            if str(self.s)==self.list3[i][1]:
                j=input('do you want to reborrow enter(y/n)=')
                if j=='n':
                    break
                else:
                    self.list33=self.list3[i][0:6]+['borrowed','not reserved']
                    print('you have borrowed this book for 1 more week ')
                    with open('H:/dsap1/borrowrecord.csv', 'a+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerow(self.list33)
                    count+=1
                    break
                            
        if count==0:
            print('no record found')            


    def reserve(self):
        count=0
        self.list4=[]
        self.list3=[]
        self.list44=[]
        self.x=input('enter your id =')
        with open('H:/dsap1/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list4.append(lines)
        self.list4 = [x for x in self.list4 if x != []]
        for i in range (len(self.list4)):
            if self.list4[i][1]==str(self.x):
                self.z=input('enter book you want to reserve=')
                with open('H:/dsap1/borrowrecord.csv', mode ='r')as file: 
                    csvFile = csv.reader(file,dialect='excel') 
                    for lines in csvFile: 
                        self.list3.append(lines)
                self.list3= [x for x in self.list3 if x != []]
                for j in range (len(self.list3)):
                    if self.z==self.list3[j][2]:
                        self.list44=self.list3[j][0:6]+['borrowed','reserved']
                        print('you have reserved this book you can borrow it next week')
                        with open('H:/dsap1/borrowrecord.csv', 'a+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerow(self.list44)
                    count+=1
                    print('book reserved')
                    break
                            
        if count==0:
            print('no record found')            

                        





    def returnn(self): 
        count=0
        self.list5=[]
        self.list=[]
        self.list55=[]
        self.listn=[]
        self.x=input('enter your id =')
        with open('H:/dsap1/memberrecord.csv', mode ='r')as file: 
                csvFile = csv.reader(file,dialect='excel') 
                for lines in csvFile: 
                    self.list5.append(lines)
        self.list5 = [x for x in self.list5 if x != []] 
        for i in range (len(self.list5)):
            if self.list5[i][1]==str(self.x):
                self.z=input('enter book you want to return=')
                with open('H:/dsap1/borrowrecord.csv', mode ='r')as file: 
                    csvFile = csv.reader(file,dialect='excel') 
                    for lines in csvFile: 
                        self.list.append(lines)
                self.list= [x for x in self.list if x != []]
                for j in range (len(self.list)):
                    if self.z==self.list[j][2]:
                        self.listn=self.list[j][2:5]+['12/12/12']
                        with open('H:/dsap1/bookrecord.csv', 'a+') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel') 
                            csvwriter.writerow(self.listn)
                        break
                        
                    else:
                        self.list55+=[self.list[j]]
                    
                print('book returned',self.list55)
                with open('H:/dsap1/borrowrecord.csv', 'w+') as self.csvfile: 
                    csvwriter = csv.writer(self.csvfile,dialect='excel') 
                    csvwriter.writerows(self.list55)
                count+=1
                break       
        if count==0:
            print('no record found')




while True: 
    print('''******************************** Welcome to library management system ******************************************
        1-add //// delete //// modify
        2-Search Book(enter title , author , subject or publication date by search)
        3-Add Member / Remove Member
        4-Checkout/renew/reserve/return a book 
        5-exit''')
    x=int(input('enter your choice(1,2,3,4,5)=')) 
    if x==1:
        s1=input('add( enter add) //// delete(enter delete) //// modify( enter modify)=')
        adm(s1)
    elif x==2:
        search()
    elif x==3:
        s2=input('do you want to add or delete member(enter add/delete)=')
        membership(s2)
    elif x==4:
        s3=input('do you want checkout/renew/reserve/return a book(enter checkout/renew/return/reserve)  =')
        management(s3)
    elif x==5:
        print('terminating......')
        break

