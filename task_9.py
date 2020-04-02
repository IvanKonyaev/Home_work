# Нужно написать генератор, который бы каждый раз возвращал новое случайное значение

# import random

# def gen_random():
# 	while True:
# 			yield random.randint(1, 5)

# x = gen_random()
# print(next(x))
# print(next(x))

# Нужно написать генератор, который бы работал как range()

# def gen_range(a, b, c = 1):
# 	d = []
# 	while a < b:
# 		d.append(a)
# 		a = a + c
# 	yield d

# x = gen_range(1, 5)
# print(next(x))

# Нужно написать генератор, который бы работал как map()

# def gen_map(a, b):
# 	while True:
# 		yield a(b)

# def function(int_list):
# 	new_list = []
# 	for i in int_list:
# 		i = i + 1
# 		new_list.append(i)

# 	return new_list

# some_list = [1, 2, 3]

# x = gen_map(function, some_list)
# print(next(x))
# print(next(x))

# Нужно написать генератор, который бы работал как enumerate()

# def gen_enumerate(a):
# 	while True:
# 		p = {}
# 		for i in range(len(a)):
# 			p[a[i]] = i
# 		yield p

# x = gen_enumerate('some')
# print(next(x))	

# Нужно написать генератор, который бы работал как zip()

# def gen_zip(a, b, c):
# 	l_len = len(a)
# 	for i in range(l_len):
# 		yield (a[i], b[i], c[i])

# x = gen_zip('some', [1, 2, 3], (None, True))
# print(next(x))
# print(next(x))