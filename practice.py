'''
In this file i will write my projects

name1=input("Enter your 1st friend's name: ")
age1=input("Enter your 1st friend's age: ")
date_of_born1=input("Enter your 1st friend's date of born: ")
name2=input("Enter your 2nd friend's name: ")
age2=input("Enter your 2nd friend's age: ")
date_of_born2=input("Enter your 2nd friend's date of born: ")
name3=input("Enter your 3th friend's name: ")
age3=input("Enter your 3th friend's age:")
date_of_born3=input("Enter your 3th friend's date of born")
name4=input("Enter your 4th friend's name: ")
age4=input("Enter your 4th friend's age:")
date_of_born4=input("Enter your 4th friend's date of born:")
name5=input("Enter your 5th friend's name: ")
age5=input("Enter your 5th friend's age: ")
date_of_born5=input("Enter your 5th friend's date of born:")

print(f"Your 1st friend's name is {name1} and his date of born is {date_of_born1}")
print(f"Your 2nd friend's name is {name2} and his date of born is {date_of_born2}")
print(f"Your 3th friend's name is {name3} and his date of born is {date_of_born3}")
print(f"Your 4th friend's name is {name4} and his date of born is {date_of_born4}")
print(f"Your 5th friend's name is {name5} and his date of born is {date_of_born5}")



laptop_name=input("Enter your laptop name")
release_date=input("Enter your laptpo's release date ")
laptop_brand=input("Enter your laptop's brand name")
laptop_price=input("enter your laptop price")
release_date=int(release_date)
laptop_price=int(laptop_price)
print(type(laptop_name))
print(type(release_date))
print(type(laptop_brand))
print(type(laptop_price))

#Indexing
str="Raihan Islam Dipayan "
print(len(str))

 # print("First word",str[0])
print("Full word",str[12:20])

total_st2=input("Toal student number ")
total_s3=str + total_st2
print(total_s3)
print(total_s3.lower())
print(total_s3.upper())
search_word=input("Word that you want to find")
position=str.find(search_word)
if position!=-1:
    print(f"{search_word} is found in {position}")
else:
    print(f"{search_word} is not found ")
    '''
def check_character(char):
    if char.isalpha():
        print(f"{char} is an alphabet.")
    elif char.isdigit():
        print(f"{char} is a number.")
    elif char.isalnum():
        print(f"{char} is an alphanumeric character.")
    else:
        print(f"{char} is a special character.")

# Taking user input
char = input("Enter a character: ")

# Checking if the input is a single character
if len(char) == 1:
     if char.isalpha():
        print(f"{char} is an alphabet.")
     elif char.isdigit():
        print(f"{char} is a number.")
            
else:
    print("Please enter a single character.")