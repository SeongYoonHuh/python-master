def fibo(n):
    if n<= 2:
        return 1

    return fibo(n-2) + (fibo-1)

if __name__=="__main__":
    n = int(input("sequence number: "))
    print(fibo(n))
