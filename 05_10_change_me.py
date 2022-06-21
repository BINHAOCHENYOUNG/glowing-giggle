def main():
    value = 99
    print("The value is", value)
    change_me(value)
    print("Back in main value is", value)

def change_me(arg):
    print("The value has changed as")
    arg = 0
    print("Now the value is", arg)

main()