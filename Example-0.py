import karnaugh_map as KM

def demo3(n = 3):
	KM.show_sector(n)

def demo4():
	KM.show_sector(4)

def demo5():
	KM.show_sector(5)

def demo6():
	KM.show_sector(6)


def demo():
	"""
		This is ment to be an example how to use this code
	"""

	demo3()

	# Anzahl der Eingänge
	n = 3

	# Eingang Signals
	S, X1, X0 = KM.lvecs(3)

	# S  : 0 0 0 0 1 1 1 1
	# X1 : 0 0 1 1 0 0 0 0
	# X0 : 0 1 0 1 0 1 0 1

	print(
	"""
\n
    In this demo

    A is representing S
    B is representing X1
    C is representing X0
\n
	"""
	)

	print(f"X0:\t{KM.show_v(X0)}")
	print(f"X1:\t{KM.show_v(X1)}")
	print(f"S:\t{KM.show_v(S)}")

	print('\n')

	# f = ((not S) and X0) or (S and X1)		;)

	f = KM.oder(

		KM.und(
			KM.nicht(S), X0
			),

		KM.und(
			S, X1
		)
	)

	# Karnaugh map mit Dezimalzahlen
	m = KM.kmapm(n)

	# Karnaugh-Diagram der Ausgangssignal
	km = KM.kmap(f, m)

	KM.show(km)

def main():

	demo()

	demo4()

	demo5()

	demo6()


if __name__ == "__main__":

	main()


