number = (int(input()))
counter = number
factorial = 1

while number > 1:
    factorial *= number
    number = number - 1

print(factorial)



