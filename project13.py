
num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]

fruits = ['apple', 'banana', 'mango', 'grape']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]


print("\nOdd numbers below", num, ":", odd_numbers)
print("Capitalized fruits:", capitalized_fruits)
