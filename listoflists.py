ip = [1,2,3,4,5,6,7,8,9,10]
"""op -> [[1,2,3], [4,5,6], [7,8,9]]"""

def rearrange_list(ip_list, split_value):
    return [ip_list[i:i+split_value] for i in range(0, len(ip_list), split_value)]

op = rearrange_list(ip, 5)
print(op)