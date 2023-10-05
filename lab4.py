print(len(set(input().split())))  #1

print(len(set(input().split()) & set(input().split()))) #2

list = sorted(set([int(s) for s in input().split()])&set([int(s) for s in input().split()])) #3
for num in list:
    print(num, end = " ")
    
list = input().split() #4
st=set()
for i in range(0,len(list)):
    if(list[i] in st):
        print("YES")
    else:
        print("NO")
        st.add(list[i])
        

def sol(sol_set):  #5
    print(len(sol_set))
    print(*[str(s) for s in sorted(sol_set)])

NM=input().split()
Anya = set()
Borya = set()
for i in range(0,int(NM[0])):
    x = int(input())
    Anya.add(x)
for i in range(0,int(NM[1])):
    a = int(input())
    Borya.add(a)

sol(Anya & Borya)
sol(Anya - Borya)
sol(Borya - Anya)


s=int(input()) #6
sr=set()
for i in range(0,s):
    list = input().split(' ')
    for j in range(0,len(list)):
        sr.add(list[j])
print(len(sr))

n = int(input()) #7
sett = {str(i) for i in range(n+1)} - {'0'}
s = input()
while s[0] != 'H':
    p = input()
    if p == 'NO':
        sett = sett - {i for i in s.split()}
    else:
        sett = sett & {i for i in s.split()}
    s = input()
print(*sorted(sett))


n = int(input())  #8
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possible_nums & guess) > len(possible_nums) / 2:
        print('YES')
        possible_nums &= guess
    else:
        print('NO')
        possible_nums &= all_nums - guess
        
print(' '.join([str(x) for x in sorted(possible_nums)]))


s=int(input()) #9
list=[]
for i in range(0,s):
    x=int(input())
    list2=[]
    for j in range(0,x):
        o=input()
        list2.append(o)
    list.append(list2)
list=[set(x) for x in list]
kbe=set.intersection (*list)
kbs=set.union(*list)
print(len(kbe), '\n', *sorted(kbe))
print(len(kbs),'\n', *sorted(kbs))


N, K = [int(s) for s in input().split()] #10
work_days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
no_strikes = set(work_days)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    no_strikes -= {a + b*i for i in range(max_strikes)}
print(len(work_days) - len(no_strikes))