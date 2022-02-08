def swap_case(s):
   
    l = [i for i in s]
    for i in range(len(l)):
        if l[i] >= 'A' and l[i] <= 'Z':
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()

    ans = "".join(l)
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    # input : HackerRank.com presents "Pythonist 2".
    # output : hACKERrANK.COM PRESENTS "pYTHONIST 2".
