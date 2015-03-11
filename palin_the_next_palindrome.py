t = input()
for i  in range(t):
    num = input()
    while True:
        num += 1
        if str(num) == str(num)[::-1]:
            print num
            break
