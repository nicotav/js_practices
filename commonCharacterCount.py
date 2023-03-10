def solution(s1, s2):
    count = 0
    for letter in s1:
        if letter in s2:
            count += 1
            s2 = s2.replace(letter, '', 1)
    return count


print(solution("abca", "xybzac"))
