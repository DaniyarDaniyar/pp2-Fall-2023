list = input().split()   #1
for i in range(0,len(list)):
    if(i==0 or i%2==0):
        print(list[i])
        

list = input().split()  #2
for i in range(0,len(list)):
    if(int(list[i]) % 2==0):
        print(list[i])

list = input().split()  #3
for i in range(1, len(list)):
    if(int(list[i])>int(list[i-1])):
        print(list[i], end=' ')

list = input().split()  #4
for i in range(0,len(list)-1):
    if(int(list[i])>0 and int(list[i+1])>0):
        print(list[i],' ',list[i+1])
        return 0
    elif(int(list[i])<0 and int(list[i+1])<0):
        print(list[i],' ',list[i+1])
        return 0


list = input().split()  #5
x=0
for i in range(1,len(list)-1):
    if(int(list[i])>int(list[i+1]) and int(list[i])>int(list[i-1])):
        x=x+1
print(x)

list = input().split() #6
max=-9e10
for i in range(0,len(list)):
    if(int(list[i])>max):
        max=int(list[i])
print(max, end=' ')
for i in range(0,len(list)):
    if(int(list[i])==max):
        print(i)
        break
    
list = input().split() #7
x=int(input())
c=1
for i in range(0,len(list)):
    if(x<=int(list[i])):
        c=c+1
    else:
        break
print(c)

list = input().split() #8
count=1
for i in range(1,len(list)):
    if(list[i] != list[i-1]):
        count=count+1
print(count)

list=input().split() #9
for i in range(0,len(list)):
    if((i+1)%2==0):
        list[i],list[i-1]=list[i-1],list[i]
for i in range(0,len(list)):
    print(list[i],' ')
    
list = [int(s) for s in input().split()] #10
imin = 0
imax = 0
for i in range(1, len(list)):
    if list[i] > list[imax]:
        imax = i
    if list[i] < list[imin]:
        imin = i
list[imin], list[imax] = list[imax], list[imin]
print(' '.join([str(i) for i in list]))

list = input().split() #11
k=int(input())
list.pop(k)
for i in range(0,len(list)):
    print(list[i],end=' ')
    
    
a = [int(s) for s in input().split()] #12
k, C = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))


list = [int(s) for s in input().split()] #13
counter = 0
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            counter += 1
print(counter)

list = input().split() #14
for i in range(0, len(list)):
    c=0
    for j in range(0, len(list)):
        if(list[i]==list[j]):
            c=c+1
    if(c==1):
        print(list[i],' ')
        
n, k = [int(s) for s in input().split()] #15
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))

n = 8  #16
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')