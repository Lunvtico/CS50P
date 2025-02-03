def insert_coin():

    cents={25,10,5}


    sum=int(50)

    while sum>0:
        print(f"Amount Due: {sum}")
        n=int(input("insert coin: "))
        if n in cents:
            sum -=n
        else:
            continue
        if sum <= 0:
           print (f"Change Owed: {sum*-1}")
           break

insert_coin()
