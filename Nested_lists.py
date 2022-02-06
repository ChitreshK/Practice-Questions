# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line

if __name__ == '__main__':
  
    Result = []
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        Result.append([name,score])
        scorelist.append(score)
        
    target=sorted(list(set(scorelist)))[1] 
    for name,score in sorted(Result):
        if score == target:
            print(name)
