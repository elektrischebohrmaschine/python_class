#!/usr/bin/env python3

list= [2, 8, 9, 48, 8, 22, -12, 2]
new_list= []
    
for x in list:
     if x >5: 
        new_list.append(x+2)


print("Original list: ", list)
print("Eddited list: ", set(new_list))
