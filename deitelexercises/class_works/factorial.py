user_input = int(input("enter a digit: "))
factorial = 1
counter = 1
while counter <= user_input:
    # factorial = factorial * counter
    factorial = factorial + counter
    counter += 1
print(factorial)
