try:
    age = int(input("Enter an age: "))
    
    if age <= 0 or age > 100:
        raise ValueError
except ValueError as e:
    print("Enter a valid age \n Age must be between 1 and 100.")
      

def start_work(age):
    if age % 2 != 0:
        print("Age is Odd ")
    else:
        print("Age is Even")

start_work(age)

