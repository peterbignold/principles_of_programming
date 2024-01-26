def isprime(n):
    import math
    answer=True
    if n==1: return False
    if n==2: return True
    if n==3: return True
    if n==4: return False
    if n==5: return True
    if n==6: return False
    if n==7: return True
    if n==8: return False
    if n==9: return False
    testno=2
    while testno<=math.sqrt(n):
        if n % testno>0:
            testno=testno+1
        else:
            answer=False
            testno=n+1
        return answer


