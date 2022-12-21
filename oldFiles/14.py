#the if/else statement

a = int(input("Enter a : "))
b = int(input("Enter b : "))


#if else ladder
if a > b:
    print ("A is greater than b\n"*10)
elif b > a :
    print ("B is geater than A\n"*10)
else :
    print ("BOth are equal")


#nested if
if a == b:
    print ("a = B")
else:
    if a > b:
        print ("A >>> b\n"*10)
    else:
        print ("B >>> A\n"*10)
