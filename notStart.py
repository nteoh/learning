import random
from pprint import pprint as pprint

a = [1, 7, 15, 4, 5, 12, 0, -2]
b = []
d = [1,2,3,4,5]
c = [8,9]
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



# for i in range(len(test_array)):
# 	print(i)
# 	bubblesort(test_array[i])
	# assert test_array[i] == sorted(test_array[i]), "{} is not sorted".format(test_array[i])
	# assert False

# print(test_array)

def merge(list1, list2):
	i1 = 0
	i2 = 0
	res = []

	for _ in range(0,len(list1)+len(list2)):
		# compare element in list 1 to element in list 2
		# if list 2 is over, append list 1
		# if list 1 is over, append list 2
		# if list 1 element is lower or equals, put in list 1 element, increment list 1
		# if list 2 element is lower or equals, put in list 2 element, increment list 2
		

		if i1 >= len(list1) or i2 < len(list2) and list2[i2] <= list1[i1]: # short circuiting won't check second condition in "and" "or" if the first one passes/fails
			print("just list2 append")
			print("i2", i2)
			res.append(list2[i2])
			i2 += 1
		else: # i2 >= len(list2) or list1[i1] <= list2[i2]:
			print("just list1 append")
			print("i1", i1)
			res.append(list1[i1])
			i1 += 1
		# elif list1[i1] <= list2[i2]:
		# 	res.append(list1[i1])
		# 	print("i1", i1)
		# 	i1 += 1
		# elif list2[i2] <= list1[i1]:
		# 	res.append(list2[i2])
		# 	print("i2", i2)
		# 	i2 += 1
		
		print(res)

	return res

pprint(merge(c, d))