n=int(input("enter the number of disks"))
def hanoi(n,source,destination,temp):
    if n==1:
        print("move disk 1 from rod",source,"to rod",destination)
        return
    elif(n>1):
        hanoi(n-1,source,temp,destination)
        print("move disk",n,"from rod",source,"to rod",destination)
        hanoi(n-1,temp,destination,source)
    
        
hanoi(n,'a','c','b')
