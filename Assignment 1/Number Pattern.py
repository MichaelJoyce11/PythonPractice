#create a function for number pattern.
def number_pattern(n):
    #keep in range for 1 to 5. 
    for i in range(1, n+1):
        #on that number, print out the number for as many times there is i.
        for j in range(1, i+1):
            print(i, end="")
        print()

#get n, and then call number pattern.
num = int(input("Please enter an integer: "))
number_pattern(num)
