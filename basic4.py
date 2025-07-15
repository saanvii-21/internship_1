##a="string"
##b=[]
##def string_to_list():
##    for i in a:
##        b.append(i)
##    print(b)
##string_to_list()

##a="abc"
##b=[]
##def string_to_list_split():
##    for i in a:
##        b.append(i.split())
##    print(b)
##string_to_list_split()

##a=input("Enter a string:")
##def string_reverse():
##   print(a[::-1])
##string_reverse()

##a = [1, 1, 2, 3, 4, 5, 5]
##b = []
##def eliminate_duplicates():
##    for i in a:
##        if i not in b:
##            b.append(i)
##    print(b)
##eliminate_duplicates()

##def reverse_string():
##    text="abc"
##    rev_text=""
##    for char in text:
##        rev_text= char + rev_text
##    print("Final Reverse:  ",rev_text)
##reverse_string()

def adding_num(a,b):
    c=a+b
    if(c>0):
        print(c)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
adding_num(a,b)


    
