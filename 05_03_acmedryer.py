#This pragram display step-by-step instructions for dissasembling an ACME dryer.
KEEP_GOINT ='y'

def main():
    KEEP_GOINT ='y'
    startup_message()
    while KEEP_GOINT =='y':
        step = int(input("Enter the number of step that you want to see: "))
        if step == 1:
            step1()
        elif step ==2:
            step2()
        elif step ==3:
            step3()
        else:
            step4()
        KEEP_GOINT = input("Do you want to see other step? (y for Yes)")
  

def startup_message():
    print("Hello, this program willl display step by step procedure for disassembeling an ACME dryer. There are 4 steps. Please input the number of the step you want to see: ")
    print()

def step1():
    print("Step1: Unpluging the dryer ad move it away from the wall")
    print()
def step2():
    print("Step2: Remove the six screws from te beck of the dryer")
    print()
def step3():
    print("Step3: Remove the back panel from the dryer")
    print()
def step4():
    print("Pull the top of the dryer straight up")
    print()



main()
