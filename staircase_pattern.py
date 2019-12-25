#double side stair-case pattern
def pattern(number):
  for i in range(1,number+1):
    c=i+1 if i%2!=0 else i

    for g in range(c,number):
      if g>=c:
        print(end=" ")
    for j in range(0,c):
      if j==c-1:
        print("*")
      else:
        print("*",end=" ")

pattern(10)
