"""remove all occurences of char from a given string"""
def char_removal(ip_string, char):
    op_str = ''.join([each_str for each_str in ip_string if each_str != char])
    # op_str = ""
    # for each_str in ip_string:
    #     if each_str != char:
    #         op_str += each_str
    print(f"{ip_string}---->{op_str}")
    return op_str
char_removal("hello", "l")