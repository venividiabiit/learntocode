for value in range(1,5): # remember this will return 1 up to 5. if we need the 5, we should include 1 number(6) in this.
    print(value)
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2)) # this will use the range() function to start with value 2 and add 2 till the count of 11.
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# the above can also be done more conscisely like this
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)