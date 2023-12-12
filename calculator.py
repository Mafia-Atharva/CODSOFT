def calculate(x,y,op):
    match op:
        case 1:
            return(f"Result = {x+y}")
        case 2:
            return(f"Result = {x-y}")
        case 3:
            return(f"Result = {x*y}")
        case 4:
            return(f"Result = {x/y}")
        case 5:
            return(f"Result = {x**y}")
        case 6:
            return -1
        
def menu():
    op=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Power\n6.Exit\nEnter operation(1/2/3/4/5/6):"))
    if(op==6):
        print("Thank you for using this program!")
        exit(0)
    a=int(input("Enter 1st number:"))
    b=int(input("Enter second number:"))
    return calculate(a,b,op)

print("***************Caclulator***************")
while True:
    result=menu()
    print(f"----------------\n{result}\n----------------")