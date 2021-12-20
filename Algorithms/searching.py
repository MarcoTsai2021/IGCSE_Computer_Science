#what do we want to return - Boolean (True, exists) or index or value itself (?)
#return the index 
#What is the space and time complexity of this algorithm 

sorted_list = [1, 4, 6, 9, 11, 14, 15, 16, 18, 19, 20]
target = 14

def binary_search(sorted_list, target):
    middle_idx = len(sorted_list) / 2
    if(sorted_list[middle_idx] == target):
        return middle_idx
    elif(sorted_list[middle_idx] > target):
        middle_idx 
    