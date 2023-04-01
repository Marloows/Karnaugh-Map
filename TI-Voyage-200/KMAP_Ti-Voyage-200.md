# Karnaugh-Map Algorithm for Ti-Voyage 200

Functional Code! As of Saturday, 01 April 2023 08:48:42

Written for [TI Voyage 200](https://de.wikipedia.org/wiki/Voyage_200)

By [@Marloows](https://github.com/Marloows)

## Matrix-Algorithm

### kmapv

```basic

# return vector v to build the kmap

kmapv(n)

Func

If n < 2 Then

	Return {0, 1}

EndIf
If mod(n, 2) = 0 Then

	Return 2*kmapv(n-1)

EndIf

Local v, i, j

kmap(n-1) -> v0

2^(n-1) -> n

dim(v)->i
i+1->j

While i > 0:

	n+v[i]->v[j]

	i-1->i

	j+1->j

EndWhile

Return v

EndFunc



```

---

### kmapm

```basic

kmapm(n)
Func

If n < 2 Then

	Return [0, 1]

EndIf


Local v0, v, i, j, m

kmapv(n) -> v
kmapv(n-1) -> v0

dim(v0)->i
dim(v)->j

newMat(i, j)->map

While i>0:

	dim(v) -> j		#reset j

	While j > 0:

		v[j]+v0[i] -> m[i, j]

	EndWhile

	i-1 -> i

EndWhile

Return m

EndFunc



```

### kmap

```basic

kmapm(v, m)
Func

Local i, j, km

rowDim(m) -> i
colDim(m) -> j

newMat(i, j) -> km

While i > 0

	colDim(m) -> j

	While j > 0

	v[m[i, j]+1] -> km[i, j]	# index starts at 1

	j-1 -> j

	EndWhile


	i-1 -> i

EndWhile

Return km

EndFunc



```

---

## Vector-Algorithms

### lvec

```basic
# Generate a logical Vector

# column = 0 gives back x_0
# column = 1 gives bach x_1

lvec(bits, column)

Func

2^column -> column

2^bits -> bits

# reusing the variables

Local x, v, i, j

{} -> v

0 -> x
0 -> i

While i < bits

#	LoopVar, StartValue, EndValue, Loop-Increment/Decrement

	For j,1,column,1
		i+1	-> i
		x	-> v[i]
	EndFor

	x*-1 +1 -> x		# keeps flipping between 1 to 0

EndWhile

return v

EndFunc



```

### vec

```basic

# vectorize a number to bits
# if x in Hex it would be very easy to read from a table

vec(x, bits)
Func

Local i, v

newMat(1, bits) -> v

#	LoopVar, StartValue, EndValue, Loop-Increment/Decrement
# - is different simple on the calculator. There are two of them
# -> is the sto button!

#	LoopVar, StartValue, EndValue, Loop-Increment/Decrement
For i,bit,1,-1

	Mod(x, 2)	-> v[1, i]		# needs to be a matrix # pre-allocated-space
	Shift(x, -1)	-> x

EndFor

mat>list(v) -> v		# better to be a list

Return v

Endfunc



```
