n = int(input())

def m():
    i=0
    while True:
        x=3**i
        if x>n:
            return -1
        if x==n:
            return i
        i+=1
print(m())
