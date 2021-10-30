list_1 = [1, 1, 2, 6, 6, 8, 12, 12, 12]
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print(x)
	return unique_list
      
unique(list_1)
print(unique_list)