def recursion_fact(num):
    if num <= 1:
       return 1
    else:
       return num*recursion_fact(num-1)
num = int(input("The number please: "))

if num < 0:
    print("Sorry no negative numbers!")
elif num == 0:
    print("this number is 0 !")
else:
    print("The factorial of number is: ", recursion_fact(num))
