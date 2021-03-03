cities = ['London', 'Paris', 'LA','SD']

for city in cities:
    print(city)

D = {'name': 'Sam', 'location': 'Iowa', 'age': 27}

for person in D:
    print(person, D[person])


# Small task

from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
story.close()
print(story_words)

text = 'testing the line of characters'
print(text.split())


