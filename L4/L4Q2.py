def factors(n) :
    for x in range(1, n + 1):
        if n % x == 0:
            print("%d divides %d" % (x, n))
n = int(input("Please input a number\n"))
factors(n)
