
def fibo(n):
    if n<=2:
        return 1
    return fibo(n-2) + fibo(n-1)

if __name__=="__main__":
    n = int(input("sequence number :  "))
    print(fibo(n))


def fizzbuzz():
    for i in range(1, 100+1):
        if i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        elif i%15==0:
            print("fizzbuzz")
        else:
            print(i)

if __name__=="__main__":
    fizzbuzz()