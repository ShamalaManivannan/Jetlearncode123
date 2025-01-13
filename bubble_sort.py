mylist = [3,6,1,5,4]
mylist.sort(reverse=True)
print(mylist)
mylist.sort(reverse=False)
print(mylist)


#time complexity = O(n^2)
bubble_list = [12,34,2,5,7]
for i in range(0,len(bubble_list)):
    for j in range(i,len(bubble_list)):
        if bubble_list[i]<bubble_list[j]:
            bubble_list[i],bubble_list[j]= bubble_list[j],bubble_list[i]

print(bubble_list)
    
    

