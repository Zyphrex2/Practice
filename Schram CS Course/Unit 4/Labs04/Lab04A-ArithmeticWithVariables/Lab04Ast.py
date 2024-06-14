# Lab04Ast.py
# "Arithmetic with Variables"
# This is the student, starting version of Lab 04A.

print()
print("********************************************")
print("Lab 04A, Arithmetic with Variables")
print("100 Point Version")
print("By: DAVID BARDAN") # Substitute your own name here.
print("********************************************")
print("\n")

r = 10
x = 5
y = 77.77
z = 1.21
PI = 3.14159

a1 = 2 * (x + 1)
print("a1 = ",a1)
a2 = 2*x + 2*1
print("a2 = ",a2)
print()
b1 = 3 * (r + x)
print("b1 =", b1)
b2 = 3 * r + 3 * x
print("b2 =", b2, "\n")
c1 = r*(x+y)
print("c1 =", c1)
c2 = r*x + r*y
print("c2 =", c2, "\n")
d1 = 5 * (y-7.77)
print("d1 =", d1)
d2 = 5*y - 5* 7.77
print("d2 =", d2,"\n")
e1 = z*(y-r)
print("e1 =", e1)
e2 = z*y - z*r
print("e2 =", e2,"\n")
f1 = r*(x+y+z)
print("f1 =", f1)
f2 = r*x + r*y + r*z
print("f2 =", f2,"\n")
g1 = r + x*y + z
print("g1 =", g1)
g2 = (r+x)*(y+z)
print("g2 =", g2,"\n")
h1 = r - x*y - z
print("h1 =", h1)
h2 = (r-x)*(y-z)
print("h2 =", h2,"\n")
j1 = r*(x/y)*z
print("j1 =", j1)
j2 = (r*x)/(y*z)
print("j2 =", j2,"\n")
k1 = r-(x/y)-z
print("k1 =", k1)
k2 = (r-x)/(y-z)
print("k2 =", k2,"\n")
m1 = 1/2
print("m1 =", m1)
m2 = 3/7
print("m2 =", m2,"\n")
n1 = (2*(r+x))/(5)
print("n1 =", n1)
n2 = 2*r+x/5
print("n2 =", n2,"\n")
p1 = 2*PI*r
print("p1 =", p1)
p2 = PI*r**2
print("p2 =", p2,"\n")