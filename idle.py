
##a=5
##def var():##global variable
##    global a
##    a=6 ##local variable
##    
##    print("inside function",a)##local scope ##global scope
##var()
##print("outside function",a)
    
##print vs return
##def add():
##    a=5
##    b=5
##    c=a+b
##    print(c)
##add()

##def add():
##    a=5
##    b=5
##    c=a+b
##    return c
##    print("data")
##
##
##output = add()
##print(output)

##def marks(sub1,sub2):
##    total_marks=sub1+sub2
##    return total_marks
##sub1 =int(input("enter subject 1 marks "))
##sub2 =int(input("enter subject 2 marks "))
##final_marks = marks(sub1,sub2)
##
##def percentage(total_marks):
##    percentage = (total_marks/200)*100
##    return percentage
##final_percentage = percentage(final_marks)
##print(f"your final percentage {final_percentage}%")

##lambda
##lambda arg:exp

##a=lambda x,y:x>y
##print(a(2,3))

##
##compare = lambda x:f"{x} is positive number" if(x>0)else f"{x} is negative"
##print(compare(-8))


##map()
##n = [1,2,3,4,5,6]
##data = list(map(lambda x:x%2==0,n))
##print(data)

##filter()
##n = [1,2,3,4,5,6]
##data = list(filter(lambda x:x%2==0,n))
##print(data)

##reduce()
##from functools import reduce
##n = [1,22,3,4,5,56]
##data = reduce(lambda x,y:x if x>y else y,n)
##print(data)


##def factorial(n):
##    if(n==0 or n==1):
##        return 1
##    else:
##      return n*factorial(n-1)
##n = int(input("enter number "))
##myfact = factorial(n)
##print(f"factorial of {n}: {myfact}")


##def fibonacci(n):
##    if(n==0 or n==1):
##        return 1
##    else:
##      return fibonacci(n - 1) + fibonacci(n - 2)
##n = int(input("enter number "))
##myfibo = fibonacci(n)
##print(f"fibonacci of {n}: {myfibo}")

import tkinter

def hello():
    print("HELLO")


root = tkinter.Tk()
root.title("first app")
root.geometry("400x300")
root.configure(bg="lightblue")
##root.resizable(False, False)
##root.minsize(300, 200)
##root.maxsize(800, 600)

button = tkinter.Button(root,text = "Click Me!",command= hello,width=10,bg="#4ceb34",
               fg = '#fff',activebackground="#0c4094",activeforeground="white")
button.pack()

label =tkinter.Label(root,text = 'name')
label.pack()

entry = tkinter.Entry(root,show = "*")
entry.pack()

##print(label.keys())
for i in entry.keys():
    print(i," : ",entry[i])

root.mainloop()


##def hello():
##    print("hello!!")
##
##root = tkinter.Tk()
##root.title("first app")
##root.geometry("400x500")
##root.configure(bg="lightblue")
##root.resizable(False, False)
##root.minsize(300, 200)
##root.maxsize(800, 600)

##button = tkinter.Button(root,text = "Click Me!",command= hello,width=10,bg="#4ceb34",
##               fg = '#fff',activebackground="#0c4094",activeforeground="white")
##button.pack()
##
##label =tkinter.Label(root,text = "Name")
##label.pack()
##
##entry = tkinter.Entry(root,show = "*")
##entry.pack()
##
####print(entry.keys())
##
##for i in button.keys():
##    print(i,":",button[i])
##
##root.mainloop()

##Layout Managers - position with pack(), place(), grid()
####pack()

##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.delete(0, tkinter.END)  # Clear the entry before inserting the new value
##    totalprice_entry.insert(6,str(totalprice))
##
##window = tkinter.Tk()
##
##window.title("Price Calculator")
##window.geometry('400x200')
####
##priceperitem_label = tkinter.Label(window, text="Price per item")
##priceperitem_label.pack()
##priceperitem_entry = tkinter.Entry(window)
##priceperitem_entry.pack()

##numberofitems_label = tkinter.Label(window, text="Number of items")
##numberofitems_label.pack()
##numberofitems_entry = tkinter.Entry(window)
##numberofitems_entry.pack()

##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_label.pack(padx = 10,pady = 40,anchor = 'ne')
##totalprice_label.pack()
##totalprice_entry = tkinter.Entry(window)
##totalprice_entry.pack()
##totalprice_entry.pack(side="right")

##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)
##calculate_button.pack()
##calculate_button.pack(fill='x',padx=3,pady=6)

##print(totalprice_label.keys())

##window.mainloop()

##

##place

##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.delete(0, tkinter.END)  # Clear the entry before inserting the new value
##    totalprice_entry.insert(0, str(totalprice))
##
##window = tkinter.Tk()
##window.title("Price Calculator")
##window.geometry('400x200')
##
##priceperitem_label = tkinter.Label(window, text="Price per item")
##priceperitem_label.place(x=0, y=0)
##priceperitem_entry = tkinter.Entry(window)
##priceperitem_entry.place(x=0, y=20)
##
##numberofitems_label = tkinter.Label(window, text="Number of items")
##numberofitems_label.place(x=0, y=45)
##numberofitems_entry = tkinter.Entry(window)
##numberofitems_entry.place(x=0, y=70)
##
##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_label.place(x=0, y=100)
##totalprice_entry = tkinter.Entry(window)
##totalprice_entry.place(x=0, y=120)
##
##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)
##calculate_button.place(x=0, y=150)
##
##window.mainloop()
##
##Grid

##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.insert(0, string=str(totalprice))
    
##window = tkinter. Tk()
##
##priceperitem_label = tkinter.Label(window, text = "Price per item")
##priceperitem_entry = tkinter. Entry(window)
##
##numberofitems_label = tkinter.Label(window, text = "Numebr of items")
##numberofitems_entry = tkinter. Entry(window)
##
##totalprice_label = tkinter.Label(window, text="Total price:")
##totalprice_entry = tkinter.Entry(window)
##
##calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)
##
##
##widgets = [priceperitem_label, priceperitem_entry, numberofitems_label,
##numberofitems_entry, totalprice_label, totalprice_entry, calculate_button]
##
##for i in range(len(widgets)):
##    widgets[i].place(x=i, y=i*20)

##Grid

##priceperitem_label.grid(row=0, column =0)
##priceperitem_entry.grid(row= 0, column=1)
##numberofitems_label.grid(row=1, column=0)
##numberofitems_entry.grid(row=1, column=1)
##totalprice_label.grid(row=2, column=0)
##totalprice_entry.grid(row=2, column=1)
##calculate_button.grid(row=3, column=0,columnspan=2)

##grid responsive
##
##window.grid_rowconfigure(0, weight=1)
##window.grid_rowconfigure(1, weight=1)
##window.grid_rowconfigure(2, weight=1)
##window.grid_rowconfigure(3, weight=1)
##window.grid_columnconfigure(0, weight=1)
##window.grid_columnconfigure(1, weight=1)
##
##
##rows = 4
##columns = 2
##for i in range(rows):
##    window.grid_rowconfigure(i, weight=1)
##for i in range(columns):
##    window.grid_columnconfigure(i, weight=1)
##
##   
##window.mainloop()

#####frame
##grid with frame
##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.insert(0, string=str(totalprice))
##    
##window = tkinter. Tk()
##frame = tkinter.Frame(window)
##priceperitem_label = tkinter.Label(frame, text="Price per item")
##priceperitem_entry = tkinter.Entry(frame)
##numberofitems_label = tkinter.Label(frame, text="Numebr of items")
##numberofitems_entry = tkinter. Entry(frame)
##totalprice_label = tkinter.Label(frame, text="Total price:")
##totalprice_entry = tkinter. Entry(frame)
##calculate_button = tkinter. Button(frame, text="Calculate total", command=computePrice)
##
##priceperitem_label.grid(row=0, column =0)
##priceperitem_entry.grid(row= 0, column=1)
##numberofitems_label.grid(row=1, column=0)
##numberofitems_entry.grid(row=1, column=1)
##totalprice_label.grid(row=2, column=0)
##totalprice_entry.grid(row=2, column=1)
##calculate_button.grid(row=3, column=0, columnspan=2)
##
##frame. pack()
##window.mainloop()

##use padding and center
##def computePrice():
##    totalprice = int(priceperitem_entry.get()) * int(numberofitems_entry.get())
##    totalprice_entry.delete(0, tkinter.END)  # Clear the entry before inserting the new value
##    totalprice_entry.insert(0, str(totalprice))
##    
##window = tkinter.Tk()
##window.title("Price Calculator")
##
##frame = tkinter.Frame(window)
##frame.pack(pady=20, padx=20)
####frame.place(relx=1.0, rely=0.5, anchor=tkinter.CENTER)##center
##
##priceperitem_label = tkinter.Label(frame, text="Price per item")
####priceperitem_label.place(relx=0.2,rely=0.0)
####priceperitem_label.grid(row=0, column=0, pady=5, padx=5)
##priceperitem_entry = tkinter.Entry(frame)
##priceperitem_entry.grid(row=0, column=1, pady=5, padx=5)
##
##numberofitems_label = tkinter.Label(frame, text="Number of items")
##numberofitems_label.grid(row=1, column=0, pady=5, padx=5)
##numberofitems_entry = tkinter.Entry(frame)
##numberofitems_entry.grid(row=1, column=1, pady=5, padx=5)
##
##totalprice_label = tkinter.Label(frame, text="Total price:")
##totalprice_label.grid(row=2, column=0, pady=5, padx=5)
##totalprice_entry = tkinter.Entry(frame)
##totalprice_entry.grid(row=2, column=1, pady=5, padx=5)
##
##calculate_button = tkinter.Button(frame, text="Calculate total", command=computePrice)
##calculate_button.grid(row=3, column=0,columnspan=2, pady=5, padx=5)
##
##window.mainloop()
##

##Spinbox, Checkbox, Radiobutton

##Spinbox

##window = tkinter.Tk()
##window.title("Tkinter tutorial")
####spin = tkinter.Spinbox(window, from_=0, to=10)
##spin = tkinter.Spinbox(window, from_=0, to=10, values=["hello", "hi", "yes", "no",])
####spin = tkinter.Spinbox(window, values=["hello", "hi", "yes", "no"])
##spin.pack()
##window.mainloop()

##def spinPressed():
##    print(spinvar.get())
####    
##window=tkinter. Tk()
##window.title("Tkinter tutorial")
####
##spinvar = tkinter.StringVar()
##spin = tkinter.Spinbox(window, values=["hello", "hi", "yes", "no"],textvariable=spinvar,
##                  command = spinPressed)
##spin.pack()
####
##window.mainloop()
##

##Checkbox
##def checkPressed():
##    print(checkvar.get())
##    
##window=tkinter. Tk()
##window.title("Tkinter tutorial")
##
##checkvar = tkinter.StringVar()
##check = tkinter.Checkbutton(window, text="Check me!", variable=checkvar, onvalue="True",
##                            offvalue="False", command=checkPressed)
##check.pack()
##                            
##window.mainloop()

###radio
##window = tkinter. Tk()
##window. title("Tkinter tutorial")
##
##def radioPressed():
##    print(radiovar.get())
##
##radiovar = tkinter.StringVar()
##
##radio = tkinter.Radiobutton(window, variable=radiovar, text="June", value="June month",
##                            command=radioPressed)
##radio1 = tkinter.Radiobutton(window, variable=radiovar, text="July", value= "July month",
##                             command=radioPressed)
##radio2 = tkinter.Radiobutton(window, variable=radiovar, text="August", value="August month",
##                             command=radioPressed)
##radio3 = tkinter.Radiobutton(window, variable=radiovar, text="September", value="Sept month",
##                             command=radioPressed)
##
##radio.pack()
##radio1. pack()
##radio2.pack()
##radio3.pack()
##
##window.mainloop()
 
##a=6##global variable 
##def add():
##    global a
##    a=4 ##local variable
##    print(a) ##local scope ##global scope
##add()    
##print("outside",a)



