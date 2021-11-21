def insertionsort(list1):
    n=len(list1)
    for i in range(1,n):
        cur_value=list1[i]
        pos=i 
        while cur_value<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos-=1
            
        list1[pos]=cur_value
    
    
list1=[10,4,25,1,5]
insertionsort(list1)
print(list1)
            
        