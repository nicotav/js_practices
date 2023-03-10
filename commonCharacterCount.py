def solution(s1, s2):
    common_chars = {}  # dictionary key: char, value: count

    for character in s1:
        if character in s2:
            # check if key exists
            if character not in common_chars:
                common_chars[character] = 1
            else:
                common_chars[character] += 1

    # get all the items in the dictionary
    items = common_chars.items()

    return items


print(solution("abca", "xyzbac"))
