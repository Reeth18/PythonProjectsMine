'''
*****
****
***
**
*
'''

rows = int (input("Enter the Number of Rows:"))
begin = 0
for index1 in range (rows, begin, -1):
    for index2 in range (begin, index1):
        print("*", end = " ")
    print()