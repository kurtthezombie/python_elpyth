# Accept 5 numbers from the user
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Calculate the mode
mode = max(set(numbers), key=numbers.count)

# Display the numbers and mode
print("Numbers:", numbers)
print("Mode:", mode)