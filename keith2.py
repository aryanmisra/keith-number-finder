
def checker(num):
    stringnum = str(num)
    arraynum = list(map(int, stringnum))
    sumnum = sum(arraynum)

    while sumnum < num:
        arraynum = arraynum[1:] + [sumnum]
        sumnum = sum(arraynum)

    if (sumnum == num):
        print str(num)  + " is a keith number"
        
print "***DISCLAIMER***\nIF THE NUMBER IT IS CHECKING GOES ABOVE 100,000 YOU WILL EXPERIENCE INTENSE LAG"
count = int(raw_input("\nAt what number would you like to stop at?: "))
value = 9
while (value <= count):

    value += 1
    checker(value)
    

print "Done!"

