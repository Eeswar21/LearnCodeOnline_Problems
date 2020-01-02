n=int(input("New file size : "))
o=int(input("deleted file size : "))
f=int(input("Free size : "))
u=int(input("Used size : "))

Total_size = f+u
Current_Free_Space = Total_size+n-o

print("Current Free Space",Current_Free_Space)
