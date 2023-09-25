x=int(input()) #1
y=int(input())
if(x<y):
    print(x)
else:
    print(y)



x=int(input()) #2
if(x>0):
    print(1)
elif(x<0):
    print(-1)
else:
    print(0)
    
x=int(input()) #3
y=int(input())
z=int(input())
e=int(input())
if((x+y+z+e)%2==0):
    print("YES")
else:
    print("NO")
    
x=int(input()) #4
if((x%4==0 and x%100!=0) or x%400==0):
    print("YES")
else:
    print("NO")
    
arr=[] #5
min=9e10
for i in range(3):
    x=int(input())
    arr.append(x)
    if(min>arr[i]):
        min=arr[i]
print(min)


arr=[] #6
i=0
for i in range(3):
    x=int(input())
    arr.append(x)
n=0
arr.sort()
max=0
for i in range(3):
    a=0
    for j in range(3):
        if(arr[i]==arr[j]):
            a=a+1
    if(a>max):
        max=a
    
if(max==1):
    print(0)
else:
    print(max)


x=int(input()) #7
y=int(input())
z=int(input())
w=int(input())
if(x==z or y==w):
    print("YES")
else:
    print("NO")
    

x=int(input()) #8
y=int(input())
z=int(input())
w=int(input())
if(z<=x+1 and z>=x-1 and w<=y+1 and w>=y-1):
    print("YES")
else:
    print("NO")
    
    
import math #9
x=int(input())
y=int(input())
z=int(input())
w=int(input())
if(abs(x-z)==abs(y-w)):
    print("YES")
else:
    print("NO")
    
    
import math #10
x=int(input())
y=int(input())
z=int(input())
w=int(input())
if(abs(x-z)==abs(y-w) or x==z or y==w):
    print("YES")
else:
    print("NO")
    
    
import math #11
x=int(input())
y=int(input())
z=int(input())
w=int(input())
if(abs(x-z)==1 and abs(y-w)==2 or abs(x-z)==2 and abs(y-w)==1):
    print("YES")
else:
    print("NO")
    
    
n=int(input()) #12
m=int(input())
k=int(input())
if(k<n*m and (k%m==0 or k%n==0)):
    print("YES")
else:
    print("NO")
    
    
n = int(input()) #13
m = int(input())
x = int(input())
y = int(input())
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y

if x < y:
    print(x)
else:
    print(y)
