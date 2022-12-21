#Simple interest
principal = 10000
yrs = 5
interest = 0.1
interest = principal*yrs*interest
print("SI is ", interest, "\nAmount is", principal + interest)


#this is with input

principal = float(input("Enter the principal :"))
yrs = float(input("Enter the no of yrs :"))
irate = float(input("Enter the interest rate (in decimals) :"))

si = principal*yrs*irate

amount = principal + si

print("SI is ", interest, "\nAmount is", amount)

#for compound interest compounded annually

amt = principal*pow(1+irate, int(yrs))

print("CI is", amt - principal, "\nAmount is", amt)
