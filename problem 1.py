print("Enter hight between")
User_Number = int(input())
while User_Number not in range (1,9):
    print("enter a number between 1 - 8")
    User_Number = int(input())
else:
    for i in range(User_Number):
        for j in range(User_Number-i-1):
            print(" ", end='')
        for j in range (i+1):
            print("#",end="")
        print("  ",end="")
        for k in range (i+1):
            print("#",end="")
        print("")
