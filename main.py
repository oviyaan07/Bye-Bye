valid=False
while not valid:
    try:
        num=int(input("enter a number"))
        while num%2==0:
            print("bye")
        valid=True
    except ValueError as er:
        print("there was an error", er)