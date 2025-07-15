###create string
##name="Saanvi"
##
###access string
##print(name)
##
###access string characters
##print(name[1])
##
###edit string
##name= "J" + name[1:]
##print(name)

###deleting string
##del name

###string methods
##text = "hello world"

##print(text.upper())      
##print(text.lower())      
##print(text.replace("world", "Python"))  
##print(text.count("l"))   
##print(text.find("world"))
##a='_Hello world'
##print(a.strip('_'))

#indexing
##a="Hello world"
##print(a[4])
##print(a[-7])

###slicing
##print(a[2:9:2])
##print(a[2:9:3])
##print(a[::-1])
##print(a[-2:-9:1])
##print(a[2:9:-1])
##print(a[9:2:-1])
##print(a[9:8])

##a="hello"
##print(a)
##print(id(a))

##a='hello'
##print(a)
##print(id(a))

##a='Hello world'
##a[5]='X'
##print(a)#error
##a='_Hello world'
##print(a.strip('_'))

##set
a={1,2,3,4,4,5,6,7,"orange"}
print(a.pop())
