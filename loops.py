numbers = [12, 7, 25, 18, 9, 30, 15]

even_numbers = []
odd_numbers = []
total = 0

for number in numbers:
    total += number

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Total:", total)
print("Average:", total / len(numbers))
