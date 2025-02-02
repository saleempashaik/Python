'''
def solution(str):
    x = list(str)



    mydict = {}
    for no in x:
        if no not in mydict:
            mydict[no] = 1
        else:
            mydict[no] += 1
    for x in mydict:
        print(x)


    #sorted_by_values_desc = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
    #return sorted_by_values_desc.keys()


((solution("aaaaaabbbbcc")))
'''
''' 
def solution(str):
    x = list(str)
    disct = set (x)
    for letter in x:
        if letter in disct:
            disct.remove(letter)
        else:
            return letter
    return "_"

print(solution("abc"))
'''
'''
def solution(squares, rects):
    sq = list[squares]
    rt = list[rects]
    o=0
    for no in sq:
        if no in rt:
            o += 1
    return o

print(solution("abc","ab"))
'''
'''

def solution(words):
    d = {}
    r = {}
    o = []
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    print(d)

    dd = (sorted(d.items(), key=lambda item: item[1], reverse=True))
    print("sorted dic",dd)
    p= (dd[0][1])
    print(p)


    for x, y in d.items():
        if y == p:
            o.append(x)

    for word in o:
        r[word] = len(word)
    print(o)
    print(r)
    rr = sorted(r.items(), key=lambda item: item[1], reverse=True)
    print(rr[len(rr)-1][0])


    #r = sorted(r.items(), key=lambda item: item[1])
    #return next(iter(d.values()))


arr= ["major", "book", "major", "book","book"]

print(solution(arr))

'''
'''
def earliestFellows(fellowTimes):
    earliest = sorted(fellowTimes.items(), key=lambda item: item[1])
    print(earliest)
    o=[]
    l = (earliest[0][1])
    for i,j in fellowTimes.items():
        if j ==l:
            o.append(i)
    print(o)


fellowTimes = {"oliver": 3, "tobey": 1}
earliestFellows(fellowTimes)
'''
'''
commands = [
  "cd dir1",
  "touch fileA",
  "cd dir2",
  "touch fileB",
  "touch fileB",
  "cd dir1",
  "touch fileC"
]
dict={}
i=''
for x in commands:
    if x.split()[0] == "cd":
        i=(x.split()[1])
        # print(i)
    if x.split()[0] == "touch":
        # print(x.split()[1])
        print("current dir",i)
        # print(dict[i])
        if (x.split()[1]) not in dict:
            dict[i] = x.split()[1]
        else:
            dict[i] = dict[i]+x.split()[1]
    print(dict)


    # else:
    #     print(1)
    #     #print(dict[i])
    #     dict[i] = dict[i]+[(x.split()[1])]

# print(dict)

'''


# family= [
#   ["James", "Ben", "Lisa"],
#   ["George", "Taylor", "Fred"],
#   ["Jen", "Ben", "Gloria"]
# ]
# def parentToChild(relations):
#     parentdic = {}
#     for member in family:
#         ChildToParent(member[0],member[1],parentdic)
#         ChildToParent(member[0],member[2],parentdic)
#     print(parentdic)
#
#
# def ChildToParent(child,parent,parentdic):
#     if parent in parentdic:
#         parentdic[parent].append(child)
#     else:
#         parentdic[parent] = [child]
#     print(parentdic)
#
# print(parentToChild(family))


# def solution(str):
#     str_split = list(str)
#     print(str_split)
#     for x in range(len(str_split)):
#         for y in range(x + 1, len(str_split)):
#             print(f"{x} :x value, {y}: y value")
#             if str_split[x] == str_split[y]:
#                 return
#     return "_"
#
#
# print(solution("abca"))

def solution(array):
    if len(array) == 0:
        return 0

    dup = dict()
    print(dup)

    for x in array:
        print(f"{x} x value")
        if x in dup.keys():
            dup[x] = dup[x] + 1
        else:
            dup[x] = 1
    x = 0
    for k, v in dup.items():
        if v > 1:
            x += 1
    return x

print(solution([1,2,3,3,3,2]))



