n = int(input())
m = int(input())
x = 0
y = 0
if n == m:
	x = n
	print(x)
elif n > m:
	y = n - m
	if y == 1:
		x = (n + 1) * 2
		print(x)
	else:
		x = m * 2
		print(x)
elif m > n:
	y = m - n
	if y == 1:
		x = (m + 1) * 2
		print(x)
	else:
		x = n*2
		print(x)