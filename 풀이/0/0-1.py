import math

def sign(input):
    if input >= 0:
        return input
    else:
        return -input

def square(input):
    output = input*input
    return math.sqrt(output)

a = 5
b = -5


print(square(sign(a)))
print(square(sign(b)))

