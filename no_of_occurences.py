"""Write a code to find the number of occurrences of each element in the array.
Input = [3,4,3,5,3,6] 
Expected Output={3:3,4:1,5:1,6:1} """

def occurrences(ip_list):
    data_dict = dict()
    for each in ip_list:
        if each not in data_dict:
            data_dict[each] = 1
        else:
            data_dict[each] += 1
    return data_dict

op = occurrences([3,4,3,5,3,6] )
print(op)