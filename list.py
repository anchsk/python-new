numbers = list(range(1,6))
print(numbers)
# [1, 2, 3, 4, 5]

even_numbers = list(range(2,11,2))
print(even_numbers)

""" print(min(numbers))
print(max(numbers))
print(sum(numbers)) """


def skip_elements(elements):
	# code goes here
	result = []
	for i, el in enumerate(elements):
		if i%2 == 0:
			result.append(el)

	
	return result
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(skip_elements(letters)) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def skip_elements_2(elements):
    # result = []
    result = [x for (i,x) in enumerate(elements) if i%2 == 0]
    return result

print(skip_elements_2(letters))