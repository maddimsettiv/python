x=input("Enter Dog Breed Option1: ")
y=input("Enter Dog Breed Option2: ")
if(x==y) :
    print("You like", x)
    print("Buy next year --", x)
if(x!=y) :
    print("Your first preference is ", x, "then", y)
    print("Check with others what to buy")
    print("Also check prices of", x,"and", y, "in 4 seconds")
    print("Your time is getting over")
z=input("Do you want to want the dog: yes or no?")
if(z=="yes") :
    print("you have 3 seconds")
    a=input("If you want the dog: Type the price in number less than 10 Rupees:  ")
    a=int(a)
    if(a>10) :
        print("you entered a number bigger than 10 rupees, no money avlbl, you will get no dog")
        print('i am done with you')
if(z!="yes") :
    print("your time is up")
print("all done")
