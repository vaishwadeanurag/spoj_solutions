t = input()
for i in range(t):
    a,b = [long(x) for x in raw_input().split(" ")]
    print long(str(long(str(a)[::-1])+long(str(b)[::-1]))[::-1])
    
