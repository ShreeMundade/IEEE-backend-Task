# Number of rows
row = 5

# Upper part of hollow diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        ch = chr(64+i)
        if j==1 or j==2*i-1:
            print(ch, end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            ch = chr(64+i)
            print(ch, end="")
        else:
            print(" ", end="")
    print()

