"""l1 = [1,4,4,5,6]
x = sum of 2 nos. (distinct)--->True"""

def sum_decider(ip_list, num):
    count_dict = dict()
    bool = False
    for each in ip_list:
        if each not in count_dict:
            count_dict[each] = 1
        else:
            count_dict[each] += 1
    print(f"count_dict:::::{count_dict}")
    for k,v in count_dict.items():
        num_required = num - k
        if num_required in count_dict:
            if num_required == k:
                if v == 1:
                    bool = False
                else:
                    bool = True
            else:
                bool = True
    return bool
op = sum_decider([1,4,4,5,6], 8)
print(f"op::::{op}")

"""sharding"""