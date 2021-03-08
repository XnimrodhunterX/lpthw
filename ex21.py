def add(a, b):
    print("ADDING {} + {}".format(a, b))
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print("DIVIDING {} / {}".format(a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight,divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")



n1 = int(input("give me a number to add: "))
n2 = int(input("now give me a second number to add: "))

add = add(n1, n2)

print("the sum of both your numbers is {}". format(add))