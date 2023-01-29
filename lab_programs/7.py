#find roots of quadratic equation
import math

print("Enter the terms of quad. eqn ax2 + bx + c = 0 :")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

print("Eqn is {}x2 + {}x + {} = 0".format(a,b,c))

x = b*b - 4*a*c

if a*b*c == 0:
    print("Roots cannot be found")
elif x == 0:
    print("Both roots are same, which is :", b/(2*a)*(-1))
elif x > 0:
    x1 = math.sqrt(x)/(2*a)
    x2 = -b/(2*a)
    print("The roots are :", x2 + x1, x2 - x1)
else:
    x1 = math.sqrt(-1*x)/(2*a)
    x2 = -b/(2*a)
    print("The roots are imaginary : \n", x2, "+ %fi\n"%x1, x2, "- %fi\n"%x1)
