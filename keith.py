from decimal import Decimal
from time import sleep

activator1 = 1

while (activator1 == 1):
    try:
        limit = int(raw_input("How many digits do you want me to stop at?"))
        activator1 = 0
    except ValueError:
        print "You did not enter an integer"
        

limitlist = []
activator2 = 1

while (activator2 <= limit):
    limitlist.append(activator2)
    activator2 += 1
    print limitlist
    
add1 = 0
add = 0
count = 9
while 1:
    sleep (0.1)
    
    
    numbers = list(str(count))
   
    for i in limitlist:
        if (i > 0) & (add < count):
            add = sum(Decimal(i) for i in numbers)
            lastnumber = int(numbers[-1])
            add1 = lastnumber+int(add)
            numbers.reverse()
            numbers.pop()
            numbers.append(add1)
            print add1
            print add
            print count
            print numbers
        if (add1 == count):
            print"________________________________"
            print add1
            print count

       # if (add == count):
          #  print"________________________________"
          #  print add
           # print count
        elif (i > 0) & (add > count):
            count += 1
            break
        
