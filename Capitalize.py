# s is string
# For example, alison heck should be capitalised correctly as Alison Heck.

def solve(s):        
   return ' '.join(word.capitalize() for word in s.split(' '))
