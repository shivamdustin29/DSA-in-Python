def nextGreaterElementToLeft(arr, n):
	s = []
	v = []

	for i in range(0, n):
		while(len(s) != 0 and s[-1] <= arr[i]):
			s.pop()

		if len(s) == 0 :
			v.append(-1)

		else:
			v.append(s[-1])

		s.append(arr[i])

	return v

if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = nextGreaterElementToLeft(arr, len(arr))
	print(ans)
