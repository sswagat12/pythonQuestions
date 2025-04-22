# """Write a Python function to reverse a string without using any built-in functions."""
def string_reversal(orig_str):
    reversed_str = ''
    for each_letter in range(len(orig_str)-1, -1, -1):
        reversed_str += orig_str[each_letter]
    return reversed_str

op = string_reversal("hello")
print(f"reversed str is {op}")
