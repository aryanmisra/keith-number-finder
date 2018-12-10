## Kieth Number Finder 

# Description
### Program:

def checker(num):

    stringnum = str(num)
    
    arraynum = list(map(int, stringnum))
    
    sumnum = sum(arraynum)
    

    while sumnum < num:
    
        arraynum = arraynum[1:] + [sumnum]
        
        sumnum = sum(arraynum)
        
        

    if (sumnum == num):
    
        print str(num)  + " is a keith number"
        
        

        

count = int(raw_input("\nAt what number would you like to stop at?: "))

value = 9

while (value <= count):


    value += 1
    
    checker(value)
    


print "Done!"



### Explaining the Program:



    def checker(num)

This part creates a new function by the name of “checker” and it takes an input which is the number it will check to see if it’s keith number. The next 4 bottom parts are part of this function.


    stringnum = str(num)

    arraynum = list(map(int, stringnum))

    sumnum = sum(arraynum)


This part is where some variables get declared so it will be easier for us to use later on. The stringnum variable is taking the number that you inputed and converting it into a string from an integer. This is so that the next variable declaration will work, arraynum. This variable converts the integer that was inputted and turns each digit into parts of an array, now the variable that we are converting must be a string or it will not work, that is the purpose of the stringnum variable. This variable also converts the array into a integer format after it becomes an array so that the digits inside may be added up. The variable sumnum takes all of the digits in the array and adds them up so it can be used later on.

    while sumnum < num:

This part declares the opening of a “while loop” which only loops the code inside as long as the condition is met. In this case, the condition is as long as the variable, “sumnum” is smaller than the variable, “num” the loop will run. This is useful so if that sum of the the array becomes greater than the number we originally inputted, the computer knows that this number is not a keith number and moves on to the next.

    arraynum = arraynum[1:] + [sumnum]

    sumnum = sum(arraynum)

This is a very important part. What it does is it replaces the last value in the array with the sum of all the digits in the array, mind you this doesn’t increase the number of digits, it only replaces. This is why it will work with numbers that have even x digits because the number of numbers being added up is always in relation to the number inputted.


 For example: If number inputted is 197, then the array at first is, [1,9,7]. Then after the loop is run once, the array is [9,7,17]. This works just like the way we were taught in class in which we would write it out as:

    197 - 1 + 9 + 7 = 17

    9 + 7 + 17 = blah, blah, blah



    if (sumnum == num):

    print str(num)  + " is a keith number"
 
This is the part that actually validates if the number is a keith number by checking if the sum of all the numbers in the array equals to the starting number

    count = int(raw_input("\nAt what number would you like to stop at?: "))
    
This asks you, at which number would you like the program to stop running.

    value = 9
    
This sets the first number it checks to 9(technically 10, because in the loop 1 gets added to this variable before it gets checked) as keith numbers cannot be single-digit.

    while (value <= count):

        value += 1
       checker(value)
       
This is the main loop of the program which keeps increasing the value that it checks by one until it reaches the value you entered, at which point, it moves to the last point of the program and ends.


### Program’s Output:


At what number would you like to stop at?: 1000000000000000000000000000000000000000000

14 is a keith number

19 is a keith number

28 is a keith number

47 is a keith number

61 is a keith number

75 is a keith number

197 is a keith number

742 is a keith number

1104 is a keith number

1537 is a keith number

2208 is a keith number

2580 is a keith number

3684 is a keith number

4788 is a keith number

7385 is a keith number

7647 is a keith number

7909 is a keith number

31331 is a keith number

34285 is a keith number

34348 is a keith number

55604 is a keith number

62662 is a keith number

86935 is a keith number

93993 is a keith number

120284 is a keith number

129106 is a keith number

147640 is a keith number

156146 is a keith number

174680 is a keith number

183186 is a keith number

298320 is a keith number

355419 is a keith number


694280 is a keith number

925993 is a keith number

1084051 is a keith number

7913837 is a keith number

11436171 is a keith number

33445755 is a keith number

44121607 is a keith number

129572008 is a keith number

251133297 is a keith number


#### Number of keith numbers: 42
Duration: 5 hours
