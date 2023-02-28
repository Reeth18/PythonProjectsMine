#1
#22
#333
#4444
#55555
#Pattern1

userInput = int (input("Enter the Number of Rows: "))
begin = 0
#Outer Loop checks the number of lines
for index1 in range(begin, userInput ):
    #Inner Loops checks the contents
    for index2 in range (begin, index1 + 1):
        print(index1, end ="")
    print()

