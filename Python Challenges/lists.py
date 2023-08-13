'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

if __name__ == '__main__':
    N = int(input())
    
    list = []
    for _ in range(N):
        commend = input().split()
        
        if commend[0] == 'insert':
            list.insert(int(commend[1]), int(commend[2]))
        elif commend[0] == 'print':
            print(list)
        elif commend[0] == 'remove':
            list.remove(int(commend[1]))
        elif commend[0] == 'append':
            list.append(int(commend[1]))
        elif commend[0] == 'sort':
            list.sort()
        elif commend[0] == 'pop':
            list.pop()
        elif commend[0] == 'reverse':
            list.reverse()
        
