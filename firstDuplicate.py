def solution(a):
    # check if there is any duplicate in the list
    if len(a) == len(set(a)):
        print(-1)
        return -1
    # if there is a duplicate, print the first duplicate
    else:
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] == a[j]:
                    print(a[i])
                    return a[i]

    for values in a:
        print(values, end=" ")


a = [2, 1, 3, 5, 3, 2]
solution(a)
