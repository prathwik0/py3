#read employee details
#display basic salary, allowace, cross pay, income tax, net pay


emp = input("Enter the name : ")
salary = int(input("Enter basic salary : "))
allowance = int(input("Enter allowance : "))


grosssal = salary + allowance

tax = 0

if grosssal <= 5000:
    tax = grosssal * 0
elif grosssal <= 10000:
    tax = grosssal * 0.1
elif grosssal <= 20000:
    tax = grosssal * 0.2
else:
    tax = grosssal * 0.3

netsal = grosssal - tax

print("\nNon-cumulative tax\nBasic Salary : ", salary, "\nAllowance :", allowance, "\nGross Salary :", grosssal, "\nIncome tax :", tax, "\nNet Salary:", netsal)

tax = 0

#cumulative tax
if grosssal > 20000:
    tax = tax + (grosssal - 20000) * 0.1
if grosssal > 10000:
    tax = tax + (grosssal - 10000) * 0.1
if grosssal > 5000:
    tax = tax + (grosssal - 5000) * 0.1

netsal = grosssal - tax

print("\nCumulative tax\nBasic Salary : ", salary, "\nAllowance :", allowance, "\nGross Salary :", grosssal, "\nIncome tax :", tax, "\nNet Salary:", netsal)
