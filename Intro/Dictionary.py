# thisdic = {}
# secdic = dict(name="Amy", Age=29)
#
#
# print(thisdic)
# print(secdic)
# final =[]
# words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]
# x=list(words[0])
# x.sort()
# print(list(words[0]))
# print(x)
# print(''.join(x))
# x.clear()
# print(x)
#
#
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(x)
x[7] = "3"
print(x)
x[7] =x[7]+"4"
print(x)
# for k, v in sorted(x.items(), key=lambda item: item[0]):
#     print(k,v)
#{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}


#final.append(list(words[0]))
#final.append(list(words[1]))
#(final[0].sort())
#(final[1].sort())
#print(''.join(final[0]))
#

myDic = dict()

myDic["name"] = ["sam"]
print(myDic)
if "name" in myDic:
    myDic["name"].append("Amy")
else:
    myDic["age"] = 23

print(myDic)
