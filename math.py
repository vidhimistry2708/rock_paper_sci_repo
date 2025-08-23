while(1):
    print("*********************************")
    print("press 1 for circle")
    print("press 2 for rectangle")
    print("press 3 for square")
    print("press 4 for triangle")
    print("press 5 for exit")
    ch=int(input("Enter your choice: "))
    
    if(ch==1):
        r=float(input("Enter radius: "))
        area=3.14*r*r
        print("Area of circle: ",area)
    elif(ch==2):
        l=float(input("Enter length: "))
        b=float(input("Enter breath: "))
        area=l*b
        print("Area of rectangle: ",area)
    elif(ch==3):
        l=float(input("Enter length: "))
        area=l*l
        print("Area of square: ",area)
    elif(ch==4):
        l=float(input("Enter length: "))
        h=float(input("Enter height: "))
        area=1/2*l*h
        print("Area of triangle: ",area)
    elif(ch==5):
        break
    else:
        print("invaild choice...")

