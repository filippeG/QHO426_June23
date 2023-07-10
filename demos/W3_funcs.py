#Definition of a function - specifying what the procedureis, what it does and how so that it can be later called/used(maybemultipletimes)

#Parameter - data given into/injected into you function
#Default Parameter - assumed if nothing is passed as argument

def t_area(b=1,h=1):
    area = 0.5*h*b
    return area

#Call to the fumction - make your program execute the function

total = t_area() + t_area(h=5) + t_area(10, 18)
print(f"Total area of 3 triangles is {total}")

height = float(input("Enter Height: "))
base = float(input("Enter Base: "))
t_area(height, base)