def longest_substring(ip_str):
    last_seen = {}
    start = max_length = 0
    max_sub_str = ""

    for i in range(len(ip_str)):  # Iterate over the indices of the string
        char = ip_str[i]  # Get the character at the current index
        
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        
        last_seen[char] = i
        
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_sub_str = ip_str[start:i + 1]

    return max_sub_str, max_length

# Testing the function
longest_sub_str, length = longest_substring("adcabcdecbe")
print(f"Longest substring with non-repeating characters: {longest_sub_str}")
print(f"Length of the longest substring: {length}")
