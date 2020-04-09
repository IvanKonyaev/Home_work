# Написать декоратор, который отменяет выполнение любой декорированной функций 
# и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!


# def canceler(func):
# 	def cancel_wrap(text):
# 		print(func.__name__, 'is canceled!')
# 	return cancel_wrap

# @canceler
# def test_funck(text):
# 	print('Funk going to say -', text)	

# test_funck('Hello World!')


# Реализовать декоратор, который измеряет скорость выполнения функций.


# from time import time

# def timer(func):
#     def timer_wrap(*args, **kwargs):
#         start = time()
#         func_return = func(*args, **kwargs)
#         end = time()
#         print('{} is working for {} seconds'.format(func.__name__, (end-start)))
#         return func_return

#     return timer_wrap

# @timer
# def medium(value, *modificators):
#     result = value
#     for m in modificators:
#         result *= m

#     return result

# print(medium(1,2,3,4,5,6,7))   


# Реализовать декоратор, который будет считать, сколько раз выполнялась функция


# def counter(func):
# 	def real_counter(n):
# 		count = 0
# 		while n != 3:
# 			func_return = func(n)
# 			n += 1
# 			count += 1
# 		print(count, 'count')	
# 	return real_counter 

# @counter
# def some_thing(n):
# 	print(n, 'func')

# some_thing(1)


# Реализовать декоторатор, который будет логгировать процесс выполнения функции: 
# создан декоратор, начато выполнение функции, закончено выполнение функции


# log = []
# create = 'Создан декоратор'
# begain = 'Начато выполнение функции'
# ending = 'Окончено выполнение функции'

# def counter(func):
# 	log.append(create)
# 	def real_counter(n):
# 		count = 0
# 		while n != 3:
# 			log.append(begain)
# 			func_return = func(n)
# 			log.append(ending)	
# 			n += 1
# 			count += 1
# 		print('Total count =',count)	
# 	return real_counter 

# @counter
# def some_thing(n):
# 	# print(n, 'func')
# 	pass

# some_thing(1)
# print(log)


# Реализовать декоратор, который будет перехватывать все исключения в функции. 
# Если они случились, нужно просто писать в консоль сообщение об ошибке.


# def counter(func):
# 	def real_counter(n, word):
# 		try:
# 			func_return = func(n, word)
# 		except TypeError:
# 			print('Wrong! TypeError!')
# 		except ZeroDivisionError:
# 			print('Wrong! ZeroDivisionError!')	
					
# 	return real_counter 

# @counter
# def some_thing(n, word):
# 	s = n/0

# @counter
# def some_thing1(n, word):
# 	s = n/word

# some_thing(1, 'car')
# some_thing1(1, 'car')


# При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]


# def work(number):
# 	return number % 5

# l = [1, 4, 5, 30, 99]
# m = map(work, l)

# print(list(m))	


# При помощи map превратить все числа из массива [3, 4, 90, -2] в строки


# def work(number):
# 	return str(number)

# l = [3, 4, 90, -2]
# m = map(work, l)

# print(list(m))


# При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки

# s = ['some', 1, 'v', 40, '3a', str]

# a = list(filter(lambda x: not isinstance(x, str), s))
# print(a)

# При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']

from functools import reduce

result = reduce(lambda x, y: x + y, list(map(lambda x: len(x), ['some', 'other', 'value'])))

print(result)