x=input("Enter a value for X:  ")
try :
    x=int(x)
    if(x<2) :
        print("X is small")
    elif (x<10) :
        print("X is medium")
    elif (x<20) :
        print("X is large")
    else :
        print("X is giant robotic Odh")
    print("All done")
except :
    x="Invalid input, enter an integer value"
    print(x)
    
