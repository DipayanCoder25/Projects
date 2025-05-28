def make_sqaure(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    print("Even square values:")
    print(even_squares)
    
    print("\nOdd square values:")
    print(odd_squares)

# Example usage:
make_sqaure(1, 10)
