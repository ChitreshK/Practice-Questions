#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


def print_rangoli(size):
    # your code goes here
   size = n
   l = list(map(chr,range(97,123)))
   string = l[n-1::-1]+l[1:n]
   width = len('-'.join(string))
   
   for i in range(n-1):
       print('-'.join(l[n-1:n-(i+1):-1]+l[n-(i+1):n]).center(width,'-'))
    
   for i in range(n):
       print('-'.join(l[n-1:i:-1]+l[i:n]).center(width,'-'))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
