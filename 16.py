#check the greatest of 3 numbers

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))


if a > b and a > c:
    
        print ("A is greatest\n"*10)
elif b > c :
    print ("B is geatest\n"*10)
elif c > b :
    print ("C is greatest\n")
else :
    print ("All are equal\n")
