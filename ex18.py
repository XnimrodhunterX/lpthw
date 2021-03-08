# this one is like your scripts with argv
def print_three(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1} arg2: {arg2} arg3: {arg3}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print(f"arg: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

def inputs():
    i1 = input("first: ")
    i2 = input("second: ")
    i3 = input("third: ")

    print_three(i1, i2, i3)

print_three("Zed","Shaw","LPTHW")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

'''
print("give me three things to print")
i1 = input("first thing: ")
i2 = input("second thing: ")
i3 = input("thrid thing: ")
'''

inputs()

# print_three(i1, i2, i3)