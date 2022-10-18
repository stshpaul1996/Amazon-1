# TASK-3
 # check all type conversions
  # int()........values like 1,2,3,4,...
  # float()......vlaues like 1.2,1.0,1.3,2.1......
  # bool().......1 for true and 0 for flase
  # complex()....3+2j(real+img).......

a=7.23
b=int(a)    #float--int-> higher date to lower data conversion called EXPLICIT
print(b)

a=7
b=float(a)  #int--float-> lower date to higher date conversion called IMPLICIT
print(b)
b=bool(a)   # int--bool
print(b)

a=3
b=complex(a) # int--complex
print(b)

a=3.2
b=complex(a) # float--complex
print(b)

a=7.30
b=bool(a)   # float--bool
print(b)

a=True
b=int(a)    # bool--int
print(b)
b=float(a)  # bool--float
print(b)

a=True
b=False
c=complex(a,b) # bool--complex
print(b,a)    

a=2+3j
b=bool(a)  # complex--bool
print(b)
print(type(a),type(b),type(c))

import keyword
print(keyword.kwlist)