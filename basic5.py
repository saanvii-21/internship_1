####Return is used inside a function
####Used for logic,compultation
####Sends result back to the caller
##
##def add(a, b):
##    return a + b
##
##result = add(2, 3)  # result will be 5
##print(result)       # this prints 5
##
####can be used anywhere
####shows the output to the user
####used in debugging,user interaction
##def add(a, b):
##    print(a + b)
##
##result = add(2, 3)  # prints 5, but result is None!
##print(result)       # prints None

##a=6#global variable
##def add():
####    a=4  ##local variable
##    print(a)
##add()
##print("outside",a)

##a=int(input("Enter first subject marks:"))
##b=int(input("Enter second subject marks:"))
##def marks_add(a,b):
##        c=a+b
##        return c
##total=marks_add(a,b)
##print("Total:",total)
##
##def percentage(c):
##    marks_add(a,b)
##    percent=(c/200)*100
##    print("Percentage:",percent)
##percentage(total)


import tkinter
def hello():
    print("HELLO")

root = tkinter.Tk()
##root.mainloop()
root.title("First app")
root.geometry("400x500")
root.configure(bg="pink")
##root.resizable(False,False)
root.minsize(300,200)
root.maxsize(800,600)

button=tkinter.Button(root,text = "CHECK ME", command =hello,width=10,bg="lightgrey",fg='#fff',
                      activebackground="grey",activeforeground="white",font=("Times new roman",18,"bold"))
button.pack()

label =tkinter.Label(root,text = "Name",width=5,bg="lightblue",fg="#fff",font=("Times new roman",18,"bold"))
label.pack()


entry = tkinter.Entry(root,show = "*")
entry.pack()
##
##print(entry.keys())
##
##for i in button.keys():
##    print(i,":",button[i])

root.mainloop()




