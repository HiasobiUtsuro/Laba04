def is_monotonic(nums):
	N = nums[1:-1]
	F = (N.split(','))
	i = iter(F)
	B = list(iter(lambda: int(next(i)), None))
	L=[]
	L.extend(B)
	R=[]
	R.extend(B)
	L.sort()
	R.reverse()
	if B == L:
		return True
	elif L == R:
		return True
	else:
		return False
nums = []
print ('Список вводится, начиная со знака [ и заканчивая знаком ], через запятую, без пробелов')
nums = input('nums = ')
print (is_monotonic (nums))
