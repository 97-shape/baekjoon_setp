import sys

stack = []

for _ in range(int(sys.stdin.readline())):
	com = list(sys.stdin.readline().split())
	if com[0] == "push":
		stack.append(com[1])
	elif com[0] == "pop":
		try:
			a = stack.pop()
			print(a)
		except:
			print(-1)
	elif com[0] == "size":
		print(len(stack))
	elif com[0] == "empty":
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	elif com[0] == "top":
		try:
			print(stack[-1])
		except:
			print(-1)
