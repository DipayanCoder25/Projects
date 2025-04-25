# this code transfers a decimal number to binary number
'''
decimal_number = int(input("Enter a decimal number: "))

binary_number = ""
number = decimal_number 


while number > 0:
    remainder = number % 2
    binary_number = str(remainder) + binary_number
    number = number // 2

if binary_number == "":
    binary_number = "0"

print(f"Binary of {decimal_number} is {binary_number}")
'''


rows = int(input("Please Enter the Total Number of Rows  : "))

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()