def solution(inputArray):
    longest = 0
    newArray = []

    for element in inputArray:
        if (len(element) > longest):
            longest = len(element)
    for element in inputArray:
        if (len(element) == longest):
            newArray.append(element)

    return newArray


print(solution(["aba", "aa", "ad", "vcd", "aba"]))
# solution(["aa"])
