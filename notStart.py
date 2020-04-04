import random
from pprint import pprint as pprint

a = [1, 7, 15, 4, 5, 12, 0, -2]
b = []
c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
d = [7, 4, 200, 120]
e = [-1, 4, 120000000, 23, -988888888]
f = [100, -4]
test_array = [a, b, c, d, e, f]

# fixed_rand = random.Random(1)  # Seeded with 3
variable_rand = random.Random()  # Variable seed

# test_array.append([fixed_rand.randint(-10000000, 10000000) for _ in range(0, 20)])

# fixed_rand = random.Random(2)
# test_array.append([fixed_rand.randint(-10000000, 10000000) for _ in range(0, 200)])

fixed_rand = random.Random(3)
test_array.append([fixed_rand.randint(-10000000, 10000000) for _ in range(0, 20000)])
test_array.append([variable_rand.randint(-10000000, 10000000) for _ in range(0, 20000)])

def bubblesort(a_list): # BAD BECAUSE OF N^2 TIME COMPLEXITY
	for j in a_list:
		for i in range(len(a_list)-1):
			if (a_list[i] > a_list[i+1]):
				temp = a_list[i]
				a_list[i] = a_list[i+1]
				a_list[i+1] = temp



for i in range(len(test_array)):
	print(i)
	bubblesort(test_array[i])
	# assert test_array[i] == sorted(test_array[i]), "{} is not sorted".format(test_array[i])
	# assert False

# print(test_array)