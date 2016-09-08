def checker(n):
    c = str(n)
    a = list(map(int, c))
    b = sum(a)
    #print("{0} = {1}".format("+".join(map(str, a)), b))

    while b < n:
        a = a[1:] + [b]
        b = sum(a)
        #print("{0} = {1}".format("+".join(map(str, a)), b))
        if b == n:
            print (n)

num = int(input("Number of numbers: "))

for i in range (0, num):
    checker(i)
