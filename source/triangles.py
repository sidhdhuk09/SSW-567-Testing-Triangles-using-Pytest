import math

def classify_triangle(a, b, c):
    if cannot_be_a_triangle(a, b, c):
        print("invalid triangle")
    elif equilateral_triangle(a, b, c):
        print("equilateral triangle")
    elif isoceles_triangle(a, b, c) and new_right_triangle(a, b, c):
        print("isosceles right-angled triangle")
    elif isoceles_triangle(a, b, c):
        print("isosceles triangle")
    elif new_right_triangle(a,b,c):
        print("right-angled triangle")
    elif proper_triangle(a, b, c):
        print("scalene triangle")
    else:
        print("Not a triangle")


def cannot_be_a_triangle(a,b,c):
    return (lambda a, b, c: a <= 0 or b <= 0 or c <= 0 or not (a + b > c and a + c > b and b + c > a))(a, b, c)

def proper_triangle(a,b,c):
   return ( lambda a,b,c:a+b>c and a+c>b and b+c>a)(a,b,c)

def isoceles_triangle(a,b,c):
    return (lambda a,b,c:a==b or a==c or b==a or b==c or c==a or c==b)(a,b,c)

def equilateral_triangle(a,b,c):
    return (lambda a,b,c:a==b==c)(a,b,c)
#def right_triangle(a,b,c):
    #return (lambda a,b,c: a**2+b**2==c**2 or a**2 + c**2==b**2 or b**2+c**2==a**2)(a,b,c)

def new_right_triangle(a,b,c): #to check if given sides of a triangle forms a right angled triangle.
    tolerance_comparision=0.01 #Tolerance comparsion is a value that is being used to determine how closely the sides of the triangle adhere to the pythagorous theorem for it to be considered as a proper right angled triangle. If the value obtained by the absolute value is less than the tolerance comparision variable then the triangle is a right-angled triangle. If the absolute value is more than the tolerance_check then it's not a right-angled triangle.
    return (lambda a,b,c,: abs(a**2+b**2-c**2)<tolerance_comparision or abs(a**2+c**2-b**2) <tolerance_comparision or abs(b**2+c**2-a**2)<tolerance_comparision) (a,b,c) #the fucntion is subtracting from c**2 to check for discrepnecies with floating point numbers. Upon finding the difference, taking the abosulte value would give us the result that would satisfy the pythagorous theorem especially if the absolute value obtained is smaller than the tolerance comparision variable.


#classify_triangle(14,15,16)