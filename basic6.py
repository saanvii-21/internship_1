##f=open('file1.txt','w+')
##print(f.tell())
##f.write("Hello world!")
##print(f.tell())
##f.seek(0)
##print(f.read())
##f.close()

#exceptional handling 
##try:
##    f = open('file1.txt','r')
##except:
##    print("file not found")
##else:
##    print(f.read())
##finally:
##    print("Done")

##try:
##    f = open('file1.txt','r')
##    n=5
##    print(f.read())
##    print(n)
##except FileNotFoundError:
##    print("file not found")
##except NameError:
##    print("name not found")


##try:
##    f = open('file1.txt','r')
##    n=int(input("enter no.:"))
##    l = 4/n
##    print(f.read())
##    print(n)
##    print(l)
##except FileNotFoundError:
##    print("file not found")
##except NameError:
##    print("name not found")

##try:
##    f = open('file1.txt','r')
##    n=int(input("enter no.:"))
##    l =[1,2,3]
##    print(f.read())
##    print(n)
##    print(l[100])
##except FileNotFoundError:
##    print("file not found")
##except Exception as e:
##    print("name not found",e.with_traceback)



