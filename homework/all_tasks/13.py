def remove_nums(list1):
    position = 3 - 1
    
    idx = 0
    
    len_list = len(list1)
    
    
    while len_list > 0:
        
        idx = (position + idx) % len_list
        
        print(list1.pop(idx))
        
        len_list -= 1


nums = [1, 2, 3, 6, 4, 98, 76, 23, 45]

remove_nums(nums)