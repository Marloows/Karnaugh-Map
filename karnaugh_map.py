from math import log

import copy


# #########################################################

#####################
# Make Karnaugh-Map #
#####################

# #########################################################

def kmapv(n = 3):
	"""

		Karnaugh-Map Vector

		returns the first row of the karnaugh matrix

		Used a seed to create the rest of the matrix
	"""

	if n < 1:
		return [0]

	v0 = kmapv(n-1) # recursive call to reduce the complexity of the task

	# when the matrix has a square form
	# horizontal mirroring
	if n%2 == 0: 
		return [2*x for x in v0]

	# odd power of 2 -> vertical mirroring

	m = 2**(n-1)

	n = (n+1)//2

	n = 2**n

	v = list(0 for _ in range(n))

	for i in range(n//2):
		v[i] = v0[i]//2			# half of n-1 row
		v[n -1 -i] = v[i] + m	# then duplicate and add 2**(n-1)

	return v


def kmapm(n = 3):
	"""

		Karnaugh-Map Matrix

		Generate a Karnaugh matrix filled with the decimal representation of the input ABCD...
	"""

	# I forget how figured it out :(

	v = kmapv(n)

	if n%2 == 0:
		n = 2**(n//2)
		m = n
		u = [x//2 for x in v]
	else:
		n = 2**((n+1)//2)
		m = n//2
		u = [2*x for x in v[:len(v)//2]]

	mre = [[0 for _ in range(n)] for _ in range(m)]

	for i in range(m):
		for j in range(n):
			mre[i][j] = v[j] + u[i]
	
	return mre


def kmap(v, m = None, n = None):
	"""
		Karnaugh-Map

		Need vector to be mapped! -> 2 a Matrix

		Generate a matrix mapping the output vector v to the Karnaugh map of the inputs

		Actual mapping of the input value to the proper square.
	"""

	if m is None:
		if n is None:
			n = int(log(len(v), 2))		# Everything is gonna be fine over here
		m = kmapm(n)
	else:
		m = copy.deepcopy(m)

	for i, row in enumerate(m):
		for j, _ in enumerate(row):
			row[j] = v[row[j]]
	
	return m


# #########################################################

#################################
# Print/Populate a Karnaugh Map #
#################################

# #########################################################


def show(m, sep = ' ', nline = '\n', verbose = False, binary = False):
	"""
		prints a matrix

		return a str of what being printed
			* set verbose to False to suppress screen print
			* binary to see numbers in binary
	"""

	L = len(m)*len(m[0])	# need 2 display bin

	f = (lambda x: str(x)) if not binary else (lambda x: format(x, f'0{int(log(L))+1}b'))

	S = nline.join(sep.join(f(x) for x in row) for row in m)

	if verbose:
		print(S)

	return S


def show_v(v, sep = ' ', verbose = False):
	"""
		return a str of the logic vector

		print a the vector
			* set verbose to True to print
	"""

	S = sep.join(str(x) for x in v)

	if verbose:
		print(S)

	return S


def show_sector(n_bit = 4, i = None, m = None):
	"""
		shows how the Karnaugh map would look when the output match the input
			- bits is the number of the input signals
			- i can be a specif input
				- if i is not provided, all possible combinations will be shown
	"""

	def show_n(m, n, i):	# local fucntion
		v = lvec(2**n, i)
		km = kmap(v, m)
		v_str = "".join(str(x) for x in v)
		print(f"\n\n{chr(65+n-i-1)}:\t{ v_str }\n")
		print(show(km))



	if m is None:
		m = kmapm(n_bit)

	print("\n\nKarnaugh-Diagram mapping the output to input\n\n")

	if i is not None:
		show_n(m, n_bit, i)
		return
	
	for i in range(n_bit-1, -1, -1):
		show_n(m, n_bit, i)


def show_table(*args, sep="\t"):

	for X in zip(*args):
		print(*X, sep=sep)


# #########################################################

########################
# Create Logic Vectors # 
########################

# #########################################################


def lvec(bits = 8, n = 0):
	"""
		Logic Vector

		returns a logic vector for x_n
	"""
	vre = [0 for _ in range(bits)]

	index = 0

	n = 2**n

	x = 0

	while index < bits:
		for _ in range(n):
			vre[index] = x
			index += 1
		x = 1 if x == 0 else 0
	
	return vre


def lvecs(n):
	"""

		Logic VectorS

		returns all logic combination of n bit input
			A, B, C, .... = lvecs(n) * n is number of inputs

			e.g.
				A, B, C, D, E = lvecs(5)
	"""
	return tuple(lvec(2**n, n-i-1) for i in range(n))


def vec(x, bits):
	"""

		vectorize

		returns vector representation of an output signal when given  as a number

		**input 0x before a number so that python interpret it as a hexadecimal number

			e.g. 85 = 0b_0101_0101 = 0x55
			e.g. 15 = 0b_0000_1111 = 0xF

	"""

	v = list()

	for _ in range(bits):
		v.append(x%2)
		x //= 2

	return v[::-1]


# #########################################################

##########################
# logic vector operation #
##########################

# #########################################################


def nicht(v):
	"""
		negates a logic vector
	"""

	return [1 if x == 0 else 0 for x in v]


def und(A, B):
	"""
		and operation on two logic vectors
	"""

	return [a and b for a, b in zip(A, B)]


def oder(A, B):
	"""
		or operation on two logic vectors
	"""

	return [a or b for a, b in zip(A, B)]


def xor(A, B):
	"""
		xor operation on two logic vectors
	"""

	return [ 0 if a == b else 1 for a, b in zip(A, B)]


