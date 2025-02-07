def pairStars(word,index=0) -> str:
    # if len(word) == 0 or len(word) == 1:
    #     print(word)
    # while index+1 < len(word):
    #     if word[index] == word[index+1]:
    #         word = word[:index+1] +'*'+word[index+1:]
    #     index += 1
    # print(word)
    if index+1 >= len(word) :
        return word
    if word[index] == word[index+1]:
        word = word[:index+1] +'*'+word[index+1:]
    return pairStars(word,index+1)


# pairStars("hello")
# pairStars("AAo")
# pairStars("luluu")
# pairStars("a")

print(pairStars("aa"))
print(pairStars("luluu"))
print(pairStars("AAo"))
print(pairStars("hello"))

