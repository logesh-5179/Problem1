def longestPalindrome(s): 
    temp = s[::-1] 
    substring = "" 
    max_substring = "" 
     
    for letter in s: 
        substring += letter 
        while substring not in temp: 
            substring = substring[1:] 
        else: 
            if substring == substring[::-1] and len(max_substring) < len(substring): 
                  max_substring = substring 
 
    return max_substring 
 
 
s = input() 
fin = longestPalindrome(s) 
print(fin) 