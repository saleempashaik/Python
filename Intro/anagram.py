def solution(words):
    sortedletter = []
    for word in words:
        x = list(word)
        x.sort()
        sortedletter.append(''.join(x))
        x.clear()

    return sortedletter

words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]
print(solution(words))

