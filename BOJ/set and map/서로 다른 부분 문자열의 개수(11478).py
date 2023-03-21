string = input()
length = len(string)

subString = set()

for i in range(1, length+1):

    for j in range(0, length):
        subString.add(string[j:j+i])
print(len(subString))