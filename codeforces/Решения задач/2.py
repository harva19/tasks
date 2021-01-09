a = int(input()) - 1
b = int(input()) + 1
k = int(input())
x = 1
z = a
for d in range(1, b):
	for i in range(d):
		if i < k and d > a:
			print(x, end=" ")
		x += 1
	print("")