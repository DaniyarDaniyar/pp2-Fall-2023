n = int(input())
hours = n//60
while(hours>23):
    hours=hours-24
    
    
print(hours, n%60)
