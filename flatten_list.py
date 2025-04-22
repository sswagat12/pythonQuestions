"""Write python program to flatten it. - input_list = [ [1,2], [3,4], [[4] , [6]] ] - output_list = [1,2,3,4,4,6] """
# flat_list = list()
# def flatten_list(ip_list):
#     print(f"ip_list::::::::{ip_list}")
#     for each in ip_list:
#         print(f"each::::::::{ip_list}")

#         if isinstance(each, list):
#             flatten_list(each)
#         else:
#             flat_list.append(each)
#     return flat_list
def flatten_list(input_list):
    flat_list = []
    for item in input_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
op_list = flatten_list([ [1,2], [3,4], [[4] , [6]] ])
print(f"op is ::::{op_list}")