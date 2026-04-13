"""a = [[3,6],[1,4],[8,10],[9,12]]
a.sort()
print(a)"""

def merge_appointments(ip_arr):
    ip_arr.sort()
    merged_op = [ip_arr[0]]
    current_index = 0
    for each_index in range(1, len(ip_arr)):
        if merged_op[current_index][1] > ip_arr[each_index][0]:
            merged_op[current_index] = [merged_op[current_index][0], ip_arr[each_index][1]]
            
        else:
            merged_op.append(ip_arr[each_index])
            current_index += 1
    return merged_op

op = merge_appointments([[3,6],[1,4],[8,10],[9,12]])
print(f"op:::::{op}")