import random 

HEAD =1 
TAILS = 2 
TOSSES = 10 

def main():
    for toss in range(TOSSES):
        if random.randint(HEAD,TAILS) == HEAD:
            print("Head")
        else:
            print("Tails")


main()