from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:
    
    def __init__(self,root):
        self.root = root
        self.root.title("LIBRARY MANAGMENT SYSTEM")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='DARK BLUE')


        MType=StringVar()
        Ref=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        LastName=StringVar()
        Address1=StringVar()
        Address2=StringVar()
        PinCode=StringVar()
        PhoneNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateOfIssue=StringVar()
        SellingPrice=StringVar()
        LateReturnFine=StringVar()
        DateOverDue=StringVar()
        DaysOnLoan=StringVar()
        DateDue=StringVar()
        TimeDuration=StringVar()
        Prescription=StringVar()


        def iReset():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            LastName.set("")
            Address1.set("")
            Address2.set("")
            PinCode.set("")
            PhoneNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateOfIssue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            DateDue.set("")
            TimeDuration.set("")
            self.txtDisplayR.delete("1.0",END)


        def iDelete():
            iReset()
            self.txtDisplayR.delete("1.0",END)
        

        def iEXIT():
            iEXIT =tkinter.messagebox.askyesno ("Library Management System", "Confirm if you want exit")
            if iEXIT >0:
               root.destroy()
               return

        def iDisplayData():

            self.txtFrameDetail.insert(END, "\t" + MType.get()+ "\t\t"+ Ref.get() + "\t"+ Title.get() +"\t" +
            Firstname.get() + "\t" + Address1.get() +"\t\t" + Address2.get() +"\t" +
            PostCode.get() + "\t"+ BookTitle.get() + "\t\t" +DateOfIssue.get() +"\t\t" + DayOnLoan.get() + "\n" )

        def iReceipt():

            self.txtDisplayR.insert(END,'Member Type: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END,'Ref No: \t\t' + Ref.get() + "\n")
            self.txtDisplayR.insert(END,'Title: \t\t' + Title.get() + "\n")
            self.txtDisplayR.insert(END,'Firstname: \t\t' + Firstname.get() + "\n")
            self.txtDisplayR.insert(END,'Address 1: \t\t' + Address1.get() + "\n")
            self.txtDisplayR.insert(END,'Address 2: \t\t' + Address2.get() + "\n")
            self.txtDisplayR.insert(END,'Pin Code: \t\t' + PinCode.get() + "\n")
            self.txtDisplayR.insert(END,'Mobile N: \t\t' + PhoneNo.get() + "\n")
            self.txtDisplayR.insert(END,'Book ID: \t\t' + BookID.get() + "\n")
            self.txtDisplayR.insert(END,'Book Title: \t\t' + BookTitle.get() + "\n")     
            self.txtDisplayR.insert(END,'Book Titlle:' + Author.get() + "\n")
            self.txtDisplayR.insert(END,'Date Borrowed: \t\t' + DateOfIssue.get() + "\n")
                                
                                       

        #===================Frame=====================================================================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle = Label(TitleFrame,width=39,font=('arial',40,'bold'),text="\tLIBRARY MANAGMENT SYSTEM\t",padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame,bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)


        DataFrame = Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE
                                , font=('arial', 12,'bold'), text="Library Membership Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE
                                , font=('arial', 12,'bold'),text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #===================Widget=====================================================================================
        self.lblMemberType = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Member Type:", padx=2,pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'), state='readonly',textvariable = MType, width=23)
        self.cboMemberType['value']=('','Student','Lecturer','Admin (Amit)')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Book ID:", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        self.txtBookID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable =BookID)
        self.txtBookID.grid(row=0, column=3)

        self.lblReferenceNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No.:", padx=2, pady=2)
        self.lblReferenceNo.grid(row=1, column=0, sticky=W)
        self.txtReferenceNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable =Ref)
        self.txtReferenceNo.grid(row=1, column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25,textvariable = BookTitle)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)
        
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state='readonly',
                                       font=('arial',12,'bold'),width=23)
        self.cboTitle['value']=('','Mr.','Miss','Dr.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25,textvariable = Author)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="First Name:", padx=2, pady=2)
        self.lblFirstName.grid(row=3, column=0, sticky=W)
        self.txtFirstName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25,textvariable = Firstname)
        self.txtFirstName.grid(row=3, column=1)

        self.lblDateOfIssue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Of Issue:", padx=2, pady=2)
        self.lblDateOfIssue.grid(row=3, column=2, sticky=W)
        self.txtDateOfIssue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25,textvariable = DateOfIssue)
        self.txtDateOfIssue.grid(row=3, column=3)

        self.lblLastName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Last Name:", padx=2, pady=2)
        self.lblLastName.grid(row=4, column=0, sticky=W)
        self.txtLastName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = LastName)
        self.txtLastName.grid(row=4, column=1)

        self.lblDateDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Due:", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25,textvariable = DateDue)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAddress1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.txtAddress1 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = Address1)
        self.txtAddress1.grid(row=5, column=1)
        
        self.lblTimeDuration = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Time Duration:", padx=2, pady=2)
        self.lblTimeDuration.grid(row=5, column=2, sticky=W)
        self.txtTimeDuration = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = TimeDuration)
        self.txtTimeDuration.grid(row=5, column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address 2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.txtAddress2 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = Address2)
        self.txtAddress2.grid(row=6, column=1)

        self.lblLateReturnFine = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Late Return Fine:", padx=2, pady=2)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = LateReturnFine)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPinCode = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Pin Code:", padx=2, pady=2)
        self.lblPinCode.grid(row=7, column=0, sticky=W)
        self.txtPinCode = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = PinCode)
        self.txtPinCode.grid(row=7, column=1)

        self.lblDateOverDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Over Due:", padx=2, pady=2)
        self.lblDateOverDue.grid(row=7, column=2, sticky=W)
        self.txtDateOverDue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = DateOverDue)
        self.txtDateOverDue.grid(row=7, column=3)

        self.lblPhoneNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Phone No.:", padx=2, pady=2)
        self.lblPhoneNo.grid(row=8, column=0, sticky=W)
        self.txtPhoneNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = PhoneNo)
        self.txtPhoneNo.grid(row=8, column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width=25, textvariable = SellingPrice)
        self.txtSellingPrice.grid(row=8, column=3)

        #=================================Widget============================================

        self.txtDisplayR = Text(DataFrameRIGHT, font=('arial', 12, 'bold'),width=32, height=13, padx=8, pady=10)
        self.txtDisplayR.grid(row=0, column=2)

        #==================================ListBox=============================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        ListOfBooks = ['Let us C','Computer science & Computer update''Engineering and   Computer science','Computer Science project',
                       'Computer science I Arrays','Computer Science unplugged','Computer  Science [part:1]','Computational science in scilab',
                       'The Computer science lab','FLASH Computer science','Rethinking Computer science Education',
                       'Engineering and Applied Science','Elements of Computer science','Computer Science II Recursion',
                       'Electrical and Computer engineering','Tommorow\'s Computing engines',
                       'Computer engineering Gr','Introduction to Computer science','Computer Science 631 [part:3]',
                       'Computer science language','Computer engineering II Lecture 1','Digital sounds as computer Science',
                       'Introduction to Computer science 2','Elements of Computer science [part : 2]','A computer science View of The Load',
                       'Introduction to Computer engineering','Computer architecture','Cornell information science',
                       'Relevance in information science','Software engineering II','IC Engineering']


        def SelectedBook(evt):
            value =str(booklist.get(booklist.curselection()))
            w = value

            if (w == "Let us C"):
               BookID.set("ISBN 7623673467628")
               BookTitle.set("Learn C programming")
               Author.set("Ambuj Singh")

               LateReturnFine.set("$0.5")
               SellingPrice.set("19$")
               DaysOnLoan.set(15)
               iReceipt()
               import datetime

               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1 + d2)
               DateOfIssue.set(d1)
               DateDue.set(d3)
               DateOverDue.set("No")

            elif(w == "Computer science & Computer update" ):
               BookID.set("100001")
               BookTitle.set("Computer science and Computer update" )
               Author.set("Mcmahon,david")
               LateReturnFine.set("$0.5")
               SellingPrice.set("$19")
               DaysOnLoan.set("$19")
               iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateOfIssue.set(d1)
               DateOverDue.set("No")

            elif (w == "Engineering and   Computer science" ):
               BooksID.set("100002")
               BookTitle.set("Engineering and Computer Science" )
               Author.set("Manteuffel, Tom")
            
               LateReturnFine.set("$0.5")
               SellingPrice.set("$19")
               DaysOnLoan.set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w == "Computer Science project"):
               BooksID.set("100003")
               BookTitle.set("Computer Science and project" )
               Author.set("Vasileios")
            
               LateReturnFine.set("$0.5")
               Sellingprice.set("$19")
               DaysOnLoan.set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Computer science I Arrays" ):
               BooksID.set("100004")
               BookTitle.set("Computer science I Arrays")
               Author.set("Vasileios")
            
               LateReturnFine.set("$0.5")
               Sellingprice.set("$19")
               DaysOnLoan.set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Computer Science unplugged" ):
               BooksID.set("100005")
               BookTitle.set("Computer Science unplugged")
               Author.set("Cortina,tom")
            
               LateReturnFine.set("$0.5")
               Sellingprice.set("$19")
               DaysOnLoan.set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Computer  Science [part:1]" ):
               BooksID.set("100006")
               BookTitle.set("Computer Science [part:1]")
               Author.set("Evans,Devid")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Computational science in scilab"):
               BooksID.set("100007")
               BookTitle. set("Computational science in scilab")
               Author. set("Storey,Brian D")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="The Computer science lab"):
               BookTitle. set("The Computer science lab")
               Author. set("lundberg,Erik")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="FLASH Computer science"):
               BooksID.set("100009")
               BookTitle. set("FLASH Computer science")
               Author. set("Lusk,Rusty")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Rethinking Computer science Education"):
               BooksID.set("100010")
               BookTitle. set("Rethinking Computer science Education")
               Author. set("Kumar,Deepak")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Engineering and Applied Science"):
               BooksID.set("100011")
               BookTitle.set("Engineering and Applied Science")
               Author. set("Murray,Richard M")
            
               LateReturnFine.set("$0.5")
               SellingPrice.set("$19")
               DaysOnLoan.set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Elements of Computer science"):
               BooksID.set("100012")
               BookTitle.set("Elements of Computer science")
               Author.set("Ayman")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Computer Science II Recursion"):
               BooksID.set("100013")
               BookTitle. set("Computer Science II Recursion")
               Author. set("Korth, Evan")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Electrical and Computer engineering"):
               BooksID.set("100014")
               BookTitle. set("Electrical and Computer engineering")
               Author. set("Frolik, Jeff")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Tommorow's Computing engines"):
               BooksID.set("100015")
               BookTitle. set("Tommorow's Computing engines")
               Author. set("J . Dally, William")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Computer engineering Gr"):
               BooksID.set("100016")
               BookTitle. set("Computer engineering Gr")
               Author. set("Seong")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
              
            elif (w =="Introduction to Computer science"):
               BooksID.set("100017")
               BookTitle. set("Introduction to Computer science")
               Author. set("Michael")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Computer Science 631 [part:3]"):
               BooksID.set("100018")
               BookTitle. set("Computer Science 631 [part:3]")
               Author. set("Ramin")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Computer science language"):
               BooksID.set("100019")
               BookTitle. set("Computer science language")
               Author. set("Irfan")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Computer engineering II Lecture 1"):
               BooksID.set("100020")
               BookTitle. set("Computer engineering II Lecture 1")
               Author. set("kalbarczyk")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Digital sounds as computer Science"):
               BooksID.set("100021")
               BookTitle. set("Digital sounds as computer Science")
               Author. set("Burg")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Introduction to Computer science 2"):
               BooksID.set("100022")
               BookTitle. set("Introduction to Computer science 2")
               Author. set("Aaron")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="Elements of Computer science [part : 2]"):
               BooksID.set("100023")
               BookTitle. set("Elements of Computer science [part : 2]")
               Author. set("Melvyn")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")
             
            elif (w =="A computer science View of The Load"):
               BooksID.set("100024")
               BookTitle. set("Introduction to Computer science")
               Author. set("David")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Introduction to Computer engineering"):
               BooksID.set("100025")
               BookTitle. set("Introduction to Computer engineering")
               Author. set("spencer")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Computer architecture"):
               BooksID.set("100026")
               BookTitle. set("Computer architecture")
               Author. set("Asanovic")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Cornell information science"):
               BooksID.set("100027")
               BookTitle. set("Cornell information science")
               Author. set("William Y")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Relevance in information science"):
               BooksID.set("100028")
               BookTitle. set("Relevance in information science")
               Author. set("Saracevic")
            
               LateReturnFine.set("$0.5")
               Sellingprice. set("$19")
               DaysOnLoan. set("$19")
               #iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateofIssue.set(d1)
               DateOverdue.set("No")

            elif (w =="Software engineering II"):
               BooksID.set("100029")
               BookTitle. set("Software engineering II")
               Author.set("steve")
            
               LateReturnFine.set("$0.5")
               SellingPrice.set("$19")
               DaysOnLoan.set("$19")
               iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateOfIssue.set(d1)
               DateOverDue.set("No")

            elif (w =="IC Engineering"):
               BooksID.set("100030")
               BookTitle.set("IC Engineering")
               Author.set("Zagozdzon-Wosik")
            
               LateReturnFine.set("$0.5")
               SellingPrice.set("$19")
               DaysOnLoan.set("$19")
               iReceipt()
               import datetime
               d1=datetime.date.today()
               d2=datetime.timedelta(days=15)
               d3 = (d1+d2)
               DateOfIssue.set(d1)
               DateOverDue.set("No")
               

        booklist = Listbox(DataFrameRIGHT, width=20, height=12,font=('arial', 12, 'bold'))
        booklist.bind('<<ListboxSelect>>', SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        for items in ListOfBooks:
            booklist.insert(END,items)

       #=====================================================================

        self.lblLabel =Label(FrameDetail, font=('arial', 10, 'bold'),pady=8,
        text="Member Type \tReference No. \tFirstname \tLast Name \tAddress 1 \tAddress 2 \tPin C0de \tBook Title \tDate\t Issued \tDays On Loan",)
        self.lblLabel.grid(row=0, column=0)

        self.txtDisplayR = Text(FrameDetail, font=('arial', 12, 'bold'),width=121, height=4, padx=2, pady=4)
        self.txtDisplayR.grid(row=1, column=0)

        #===================================Button=================================

        self.btnDisplayData=Button(ButtonFrame, text='Display Data', font=('arial',12,'bold'), width=30, bd=4)
        self.btnDisplayData.grid(row=0, column=0)

        self.btnDelete=Button(ButtonFrame, text='Delete', font=('arial',12,'bold'), width=30, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=1)

        self.btnReset=Button(ButtonFrame, text='Reset', font=('arial',12,'bold'), width=30, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=2)

        self.btnExit=Button(ButtonFrame, text='Exit', font=('arial',12,'bold'), width=30, bd=4, command=iEXIT)
        self.btnExit.grid(row=0, column=3)

        


        
if  __name__ =='__main__':
    root = Tk()
    application =Library(root)
    root.mainloop()
