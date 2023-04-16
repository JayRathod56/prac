import matplotlib.pyplot as plt

def area_of_triangle(b,h):
  area = 0.5 * b * h
  return area

def area_of_trapezoid(a, b, h):
  area = 0.5 * (a + b) * h
  return area

def membership(x, l, c, r):
  
  if (l <= x) and (x < c):
    num = x - l
    den = c -l
    ans = num / den
    return ans
  
  elif (c < x) and (x <= r):
    num = r - x
    den = r - c
    ans = num / den
    return ans

  elif x == c:
    return 1

  else:
    return 0 


def extent_of_firing(lst):
  return min(lst)

def Crisp(lst_z, lst_a, lst_c):
  num_val = 0
  den_val = 0

  for i in range(len(lst_z)):
    val = lst_z[i] * lst_a[i] * lst_c[i]
    val2 = lst_z[i] * lst_a[i]

    num_val += val
    den_val += val2

  ans = num_val / den_val
  return ans

def Centroid(inp_tab):
  if len(inp_tab) == 3:
    return inp_tab[1]
  else:
    ans = (inp_tab[0]+inp_tab[-1])/2
    return ans

inp_tab = {
    "T":{"L":[-5,10,25],"BA":[15,30,45],"A":[40,50,60],"AA":[55,70,85],"H":[75,90,105]},
    "P":{"L":[0.25,1,1.75],"BA":[1.25,2.0,2.75],"A":[2,3,4],"AA":[3.25,4,4.75],"H":[4.25,5,5.75]},
    "HP":{"L":[0.5,1,1.5],"ML":[1.25,2,2.75],"M":[2.5,3,3.75],"MH":[3.5,4,4.5],"H":[4.25,5,5.75]}
}
inp_x = {
    "T":22.5,
    "P":1.5
}

# Find HP based on given T and P
T = 22.5
P = 1.5

# R1
T1 = [15,30,45]
P1 = [1.25,2.0,2.75]
HP1 = [3.5,4,4.5]

# R2
T2 = [-5,10,25]
P2 = [0.25,1,1.75]
HP2 = [4.25,5,5.75]

#Calculating area of triangle
Area_of_Triangle1 = area_of_triangle(HP1[-1]-HP1[0],1)

Area_of_Triangle2 = area_of_triangle(HP2[-1]-HP2[0],1)

#Area
A = []
A.append(Area_of_Triangle1)
A.append(Area_of_Triangle2)

print("A: ",A)

#Membership
Membership = []

# For R1
mem = membership(T,T1[0],T1[1],T1[2])
Membership.append(mem)
mem = membership(P,P1[0],P1[1],P1[2])
Membership.append(mem)

#Extent of Firing for R1 (z1)
Z1 = extent_of_firing(Membership)

Membership = []

# For R2
mem = membership(T,T2[0],T2[1],T2[2])
Membership.append(mem)
mem = membership(P,P2[0],P2[1],P2[2])
Membership.append(mem)

#Extent of Firing for R2 (z2)
Z2 = extent_of_firing(Membership)

Z = []
Z.append(Z1)
Z.append(Z2)

print("Z: ",Z)

#Centroid

C1 = Centroid(HP1)
C2 = Centroid(HP2)

C = []
C.append(C1)
C.append(C2)

print("C: ",C)

Crisp = Crisp(Z,A,C)
print("Crsip Value of Heating Power (HP) at Temperature (T): 22.5 and Pressure (P): 1.5 is: ", Crisp)

