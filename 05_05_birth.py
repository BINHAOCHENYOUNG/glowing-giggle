#This program demoonstrates two functions that have local varibles with the same name 

def main():
    Wenzhou()
    Hangzhou()

def Wenzhou():
    bridge = 1000
    print("Wenzhou has", bridge, "bridges")

def Hangzhou():
    bridge = 5000
    print("Hangzhou has", bridge, "bridges")

main()