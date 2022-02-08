# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left


def count_substring(string, sub_string):
    count = 0
    
    for i in range(len(string)):
        if sub_string[:] == string[i:len(sub_string)+i]:
            count += 1
            
    return count

if __name__ == '__main__':
    string = input().strip()         #"ABCDCDC"
    sub_string = input().strip()     #"CDC"
    
    count = count_substring(string, sub_string)
    print(count)   #2
