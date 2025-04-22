"""question: find and print the largest integer towards right, if not, print -1
eg: ip: [8,9,5,11,6,1,7,6]
op: [11,11,11,-1,7,7,-1,-1]
"""
def integer_sort_manipulation(arr_):
    pointer_index = 0
    highest_num = max(arr_)
    highest_int_pointer = arr_.index(highest_num)
    # flag = False

    while pointer_index < len(arr_)-1:
        
        # highest_num = max(arr_)
        # highest_int_pointer = arr_.index(highest_num)
        print(f"highest_int_pointer:{highest_int_pointer}")
        if pointer_index < highest_int_pointer:
            if arr_[pointer_index] < arr_[highest_int_pointer]:
                arr_[pointer_index] = arr_[highest_int_pointer]
            else:
                arr_[pointer_index] = -1
            pointer_index += 1
        else:
            highest_num = max(arr_[highest_int_pointer+1:])
            highest_int_pointer = arr_.index(highest_num)
    arr_[-1] = -1
    print(f"arr_::{arr_}")


        
        # else:
        #     # highest_num = max(arr_[highest_int_pointer+1:])
        #     highest_int_pointer = arr_.index(highest_num)


    # print(f"test:{max(arr_[highest_int_pointer+1:])}")
integer_sort_manipulation([8,9,5,11,6,1,7,6])