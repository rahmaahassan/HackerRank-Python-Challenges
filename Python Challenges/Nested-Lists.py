'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
        
    def sorting(i):
        return (i[1], i[0])
    
    list.sort(key = sorting)
    
    for i in range(1, len(list)):
        if list[i][1] != list[i-1][1]:
            secondLowestAge = list[i][1]
            break
    
    for i in list:
        if i[1] == secondLowestAge:
            print(i[0])
