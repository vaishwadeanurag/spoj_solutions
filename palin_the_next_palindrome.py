import re
t = input()
for i  in range(t):
    num = input()
    snum = str(num)
    if len(snum) == 1:
        print num+1
    if snum == snum[::-1]:
        if not re.match(r"[0-8]", snum):
            print num+2
            continue
        if len(snum)%2 == 0:
            place = str(long(snum[:len(snum)/2])+1)
            print place+place[::-1]
            continue
        else:
            left = snum[:len(snum)/2]
            right = snum[len(snum)/2:]
            if right[0] == '9':
                rplace = str(long(right[::-1])+1)[::-1]
                left = list(left)
                right = list(right)
                left[-1]=rplace[-1]
                right[0]=rplace[0]
                right[1]=rplace[1]
                print "".join(left+right)
                continue
            else:
                rplace = str(long(right[::-1])+1)[::-1]
                print left+rplace
                continue
    else:
        if len(snum)%2 == 0:
             place = str(long(snum[:len(snum)/2])+1)
             print place + place[::-1]
        else:
             place = str(long(snum[:len(snum)/2+1])+1)
             print place + place[1::-1]
