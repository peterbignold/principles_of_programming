def isprime(n):
    if n==1: return False
    if n==2: return True
    if n==3: return True
    testno=3
    answer=True
    while testno*testno<n:
        if n % testno>0:
            testno=testno+2
        else:
            answer=False
            testno=n
    return answer


