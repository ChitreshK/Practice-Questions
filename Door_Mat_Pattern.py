# Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
# N is odd number, M = N*3

N, M = map(int, input().split())

for i in range(N//2):
    print(((2*i+1)*'.|.').center(M,'-'))
    
print(('WELCOME').center(M, '-'))

for i in range(N//2,0,-1):
    print(((2*i-1)*'.|.').center(M,'-'))
