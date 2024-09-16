from  tkinter import  *
import tkinter

root=tkinter.Tk()
root.geometry("500x500")
root.title("Palindrom And Prime Number")

scvalue=StringVar()
scvalue.set("")

def prime():
    primef=Frame(bg="orange")
    primef.place(x=0,width=500,height=500)

    




def palindrome():
    global scvalue
    pf=Frame(root,bg="slateblue1")
    pf.place(x=0,width=500,height=500)

    Label(pf,text="Palindrome",bg="slateblue1",fg="black",font=("comic sana ms",30)).pack()


    # ------------------------- Number Entry Place ----------------------
    
    
    def event_for_in(event):
        if data.get()=="Search Here....":
            data.delete(0,"end")
            data.config(bg="white")

    def event_for_out(event):
        if data.get()=="":
            data.insert(0,"Search Here....")
            data.config(bg="yellow")

    data=Entry(pf,bg="yellow",font=("comic sana ms",20),relief=RAISED,borderwidth=5)
    data.place(x=100,y=150)

    data.insert(0,"Search Here....")
    data.bind("<FocusIn>",event_for_in)
    data.bind("<FocusOut>",event_for_out)

    # --------------------------

    # ------------- search button def -----------

    
    
    def calculate():
        global scvalue
        
        num=int(data.get())
        temp=num
        rev=0
        while temp >0:
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
        if num==rev:
            ans="Yes"
            scvalue.set(ans)
            scvalue.update
            
        else:
            ans="No"
            scvalue.set(ans)
            scvalue.update
            
            

    # -------------- Search Button -------------

    searchb=Button(pf,text="Check",bg="orange red",font=("comic sana ms",20),relief=RAISED,borderwidth=5,command=calculate)
    searchb.place(x=200,y=250)    

    # -------------- Result Show place ------------

    result=Entry(pf,textvariable=scvalue,bg="yellow",font=("comic sana ms",20),relief=RAISED,borderwidth=5)
    result.place(x=100,y=350)



def home():
    hf=Frame(root,bg="pink")
    hf.place(x=0,width=500,height=500)

    Label(hf,text="Palindrome & Prime",bg="pink",fg="black",font=("comic sana ms",30)).pack()

    sb=Button(hf,text="Prime Number ",bg="magenta2",font=("comic sana ms",30),relief=RAISED,borderwidth=5,cursor="hand2",command=prime)
    sb.place(x=100,y=150)

    sb=Button(hf,text="Palindrome",bg="magenta2",font=("comic sana ms",30),relief=RAISED,borderwidth=5,cursor="hand2",command=palindrome)
    sb.place(x=140,y=250)
home()
root.mainloop()
