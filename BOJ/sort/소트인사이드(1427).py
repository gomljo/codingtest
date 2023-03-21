numbers = [int(x) for x in list(input())]
numbers.sort(reverse=True)
numbers = [str(x) for x in numbers]
print(''.join(numbers))