#importing library and modules
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

#Setting up a screen window
screen=Tk()
screen.title("Python LAB EL")
screen.geometry("2000x1000")

my_img=ImageTk.PhotoImage(Image.open("C:/Users/Arpita/Pictures/RV Logo.jpg"))
my_label=Label(image=my_img).grid(row=0,column=0)

mylabel1=Label(screen,text="Choose the program you want to run", font=("Corbel",28,"bold"),bg="#7FFFD4")
mylabel1.grid(row=0,column=1)
mylabel2=Label(screen,text="Program 1: Largest Prime Factor of a given integer", font=("Corbel",20),bg="#7FFFD4")
mylabel2.grid(row=1,column=1)
mylabel3=Label(screen,text="Program 2: Set & Tuple Operations", font=("Corbel",20),bg="#7FFFD4")
mylabel3.grid(row=2,column=1)
screen.config(background='#7FFFD4')


#PROGRAM - 1

#working fucntions(commands) of the button
def program1():
    new=Toplevel()
    new.title("Program 1")
    new.config(background='#C1FFC1')
    new.geometry("2000x1000")
    label1=Label(new,text="                          ",bg='#C1FFC1').grid(row=0,column=0)
    label3=Label(new,text="                          ",bg='#C1FFC1').grid(row=0,column=1)
    mylabel4=Label(new,text="......Largest Prime Factor of a given integer......", font=("Corbel",20),bg='#C1FFC1')
    mylabel4.grid(row=0,column=3)
    label2=Label(new,text="  ",bg='#C1FFC1').grid(row=1,column=1)
    e1=Entry(new)
    e1.insert(0, "Enter the number")
    e1.grid(row=2, column=3, padx=100, pady=1)

    result_frame=LabelFrame(new, text="result for Max Prime", padx=5, pady=5)
    result_frame.grid(row=3, column=3)

    def maxPrime():
        n=int(e1.get())
        mP=-1   #mP=Max Prime
        while n%2==0:
            mP=n
            n=n/2
        for i in range(3,int(n**0.5)+1,2):
            while n%i==0:
                mP=i
                n=n/i
        if n>2:
            mP=n
        a=int(mP)
        result=Label(result_frame, text=(f"Max Prime factor of the entered number is {a}"))
        result.grid(row=4, column=3)
        e1.delete(0,END)
        
    button1=Button(new,text="maxPrime", padx=100,pady=1,command=maxPrime)
    button1.grid(row=5, column=3)

    # exit button
    ttk.Button(new, text="EXIT", command=new.destroy).grid(row=7, column=3)

setdata=set()
tupledata=tuple()

#PROGRAM - 2

def program2():
    new3=Toplevel()
    new3.title("Program 2")
    new3.config(background='#87CEEB')
    new3.geometry("2000x1000")

    def perform():
        global setdata,tupledata
        choice=clicked.get()
        if choice=="Set Operation":
            new=Toplevel()
            new.geometry('2000x1000')
            new.title("Set Operation")
            new.configure(background='deepskyblue1')
            mylabel=Label(new,text="......Set Operations......", font=("Corbel",20),fg='white',bg="deepskyblue1")
            mylabel.grid(row=0,column=1)
        
            e1=Entry(new)
            e1.insert(0,"Enter the Element")
            e1.grid(row=2, column=1, padx=100, pady=1)
            my_label=Label(new,text="Enter the element & then choose the operation to perform", font=("Georgia",16,"italic"),bg="deepskyblue1")
            my_label.grid(row=1,column=1)
            result_frame=LabelFrame(new, text="Output", padx=5, pady=5)
            result_frame.grid(row=4, column=0)

            def c1():
                global setdata
                data=e1.get()
                setdata.add(data)
                result=Label(result_frame, text=setdata)
                result.grid(row=5, column=0)
                e1.delete(0,END)
            def c2():
                global setdata
                data=e1.get()
                setdata.discard(data)
                result=Label(result_frame, text=setdata)
                result.grid(row=5, column=0)
                e1.delete(0,END)
            def c3():
                global setdata
                data=e1.get()
                setdata.update(data)
                result=Label(result_frame, text=setdata)
                result.grid(row=5, column=0)
                e1.delete(0,END)
            #Creating Buttons for Operations
            button1=Button(new,text="Add/Insert", padx=5,pady=1,command=c1).grid(row=3, column=0)
            button2=Button(new,text="Remove/Delete", padx=5,pady=1,command=c2).grid(row=3, column=1)
            button3=Button(new,text="Update/Append", padx=5,pady=1,command=c3).grid(row=3, column=2)
            ttk.Button(new,text="EXIT",command=new.destroy).grid(row=7,column=1)

        elif choice=="Tuple Operation":
            new2=Toplevel()
            new2.geometry('2000x1000')
            new2.title("Tuple Operation")
            new2.configure(background='lightgoldenrod1')
            mylabel=Label(new2,text="......Tuple Operations......", font=("Corbel",20),bg="lightgoldenrod1")
            mylabel.grid(row=0,column=1)
            #tupledata=tuple()
            e2=Entry(new2)
            e2.insert(0,"Enter the element")
            e2.grid(row=2, column=1, padx=100, pady=1)
            my_label=Label(new2,text="Enter the element & then choose the Tuple operation", font=("Georgia",16,"italic"),bg="lightgoldenrod1").grid(row=1,column=1)
            result_frame=LabelFrame(new2, text="Output", padx=5, pady=5)
            result_frame.grid(row=4, column=1)

            def c1():
                global tupledata
                data1=e2.get()
                tupledata+=(data1,)
                e2.delete(0,END)
            def c2():
                global tupledata
                del tupledata
                messagebox.showinfo("NOTE","Tuple is Deleted")
            def c3():
                global tupledata
                dis=StringVar()
                result=Label(result_frame,textvariable=dis)
                dis.set(str(tupledata))
                #result=Label(result_frame, text=tupledata)
                result.grid(row=5,column=0)
            #Creating buttons for operations
            button1=Button(new2,text="Add/Insert", padx=5,pady=1,command=c1).grid(row=3, column=0)
            button2=Button(new2,text="Delete Tuple", padx=5,pady=1,command=c2).grid(row=3, column=1)
            button3=Button(new2,text="Display/View", padx=5,pady=1,command=c3).grid(row=3, column=2)
            ttk.Button(new2,text="exit",command=new2.destroy).grid(row=6, column=1)
    label1=Label(new3,text="                                     ",bg='#87CEEB').grid(row=0,column=0)
    label2=Label(new3,text="                                     ",bg='#87CEEB').grid(row=0,column=1)
    label3=Label(new3,text="                                     ",bg='#87CEEB').grid(row=0,column=2)
    label4=Label(new3,text="                                     ",bg='#87CEEB').grid(row=3,column=4)
    label5=Label(new3,text="                                     ",bg='#87CEEB').grid(row=4,column=4)
    mylabel=Label(new3,text="......Select the Operation......", font=("Georgia",20,"italic"),fg="dark blue",bg="#87CEEB").grid(row=0,column=4)
    label6=Label(new3,text="                                     ",bg='#87CEEB').grid(row=2,column=0)
    
    clicked=StringVar()
    clicked.set('Show')
    drop=OptionMenu(new3,clicked,"Set Operation","Tuple Operation")
    drop.grid(row=1,column=4,padx=10,pady=6)
    myButton=Button(new3,text="OK",padx=10,pady=4,command=perform).grid(row=5,column=4)
    ttk.Button(new3,text="Terminate",command=new3.destroy).grid(row=7,column=4)

    
#Setting up option buttons for the two programs
Button1=Button(screen, text="Program 1", padx=50, pady=50,command=program1)
Button1.grid(row=4,column=1)
Button2=Button(screen, text="Program 2", padx=50, pady=50,command=program2)
Button2.grid(row=5,column=1)
ttk.Button(screen,text="EXIT",command=screen.destroy).grid(row=7,column=1)
#Run loop of the program
screen.mainloop()
