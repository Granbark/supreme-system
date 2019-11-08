import time

#fibonacci recursive
#N = 35 without memoization = 9.9 Seconds
#N = 35 with memoization =

mem_dict = {"0": 0, "1": 1, "2": 1, "3": 2} #...

def fibonacci(n):
	try:
		return mem_dict[n]
	except:
		pass
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		number = fibonacci(n-1) + fibonacci (n-2)
		mem_dict[n] = number #Creates a "cache"
		
		
		return number
		

value = int(input())

time_1 = time.time()
print(fibonacci(value))
time_2 = time.time()
print(time_2 - time_1)

	