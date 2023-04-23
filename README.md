# Project [Karnaugh-Map](https://en.wikipedia.org/wiki/Karnaugh_map)

By @Marloows

Creates a 2-D Array, which represents a mapping of $N$ binary inputs to $1$ binary output.

This visual representation is then used to minimize the number of the logic-gates needed to create the output.

My original idea was to write an algorithm for [TI Voyage 200](https://de.wikipedia.org/wiki/Voyage_200). The source code for that is also included. I hope that it still works.

---

## Understanding Limitation

Mapping more than 4 Input-Variable doesn't really make much sense in 2-D space!

### How-2 make KV-Map

KV-Map is a visual representation of specific function that return either $1$ or $0$, or to be more specific $True$, $False$ considering a $N$ binary input variable.

In boolean algebra any [function](https://en.wikipedia.org/wiki/Boolean_function) can be written in the [Disjunctive Normal Form](https://mathworld.wolfram.com/DisjunctiveNormalForm.html), which represents all possible input-combinations joined by an outer [Disjunction](https://en.wikipedia.org/wiki/Logical_disjunction), where each combination is joined by an inner [Conjunction](https://en.wikipedia.org/wiki/Logical_conjunction).

For Example when $N = 3$

$ f(A, B, C) = A B C + A B \overline C + A \overline B C + A \overline B \overline C + \overline A B C + \overline A B \overline C + \overline A \overline B C + \overline A \overline B \overline C $

#### Neighboring-Nodes

The KV-Map combine the Disjunctive Normal Form of the input space with the function output value of that specific combination. By grouping input-combinations where the output is $True$, into [#neighboring](https://www.oxfordlearnersdictionaries.com/definition/english/neighbour_2) nodes.

We say two input combination are neighbors, when differ in only one input-state.

For example:

$A \overline B C \overline D \overline E$ is a neighbor with $\overline A \overline B C \overline D \overline E$ almost the same combination difference is only $A$, $\overline A$

#### Reducing KV-Map

Having neighboring input-combinations present in the output function (#Having-True-Value) means that we can reduce these two nodes into one.

##### Reducing-Proof

Based this proof:

$(A \land B) \lor (A \land \overline B) = A \land (B \lor \overline B)$ [#Distributive-Axiom](https://mathworld.wolfram.com/BooleanAlgebra.html) Just applied backwards.

$B \lor \overline B = 1$ #Inverse-Element-Axiom

$A \land 1 = A$ #Neutral-Element-Axiom

And therefore $(A \land B) \lor (A \land \overline B) = A$

Any two Expressions (nodes/input-combination) that only differ in one input-state can be combined into on expression.

That means:

$A \overline B C \overline D \overline E + \overline A \overline B C \overline D \overline E$ can be written as $B C \overline D \overline E$

And if these two expressions are a part of the Disjunctive-Normal-Form of a function $f(A, B, C, D, E)$, we can say that the output of $f$ is independent from the state of the input-variable $A$.

##### Why-Even 2 reduce

The problem that we are trying to solve, is to reduce the number of **AND**, **OR** Logic-Gates need to generate the required output from the inputs-combination.

ABSOLUTE worst-case you need:

$2^n - 1$ $\lor$

$(n-1) \cdot 2^n$ $\land$

To get $1$ boolean value out of $N$ inputs!

To reduce the Disjunctive Normal Form

##### How-2 Reduce with KV-Map

Reducing the Disjunctive-Normal-Form with KV-Map is done by grouping nodes into bundles of $2^k$ where $k \in N$.

For this to work these nodes must be [#neighbors](#Neighboring-Nodes)!

### Limitation

In 2-D Space we visualize the KV-Map as [Matrix](<https://en.wikipedia.org/wiki/Matrix_(mathematics)>>). Where each node (#input-combination) is an element of that matrix with the output value $1$, $0$ of the function $f$.

The problem is that in this configuration you can have only 4 neighboring-nodes.

Up, Down, Left, Right.

If we have $N$ input that means that we have $2^N$ node and each one has $N$ neighbor.

So 2D-visual representation of KV-Map input-space with more 4 inputs require some imagination to get any useful insight out of it!

Nevertheless my algorithm extend the rules used to derive the first 4 KV-Map into any number of input variable regardless if useful or not!

Perhaps in the future I can work on a way to visualize the KV-Map as interactive graph with nodes and edges somewhat similar to [Obsidian-Graph-View](https://help.obsidian.md/Plugins/Graph+view)

## Disclaimer!!

#IN-THEORY This program can map **any number of inputs** but beware! Memory usage will grow exponentially.

And it won't even be useful!

But hopefully fun to try nevertheless :)

---

## Table of Content

### [karnaugh_map.py](./karnaugh_map.py)

Contains the actual implementations of the algorithm to create the Karnaugh-Map.

---

## Dependencies

### [math](https://docs.python.org/3/library/math.html)

Found in [The Python Standard Library](https://docs.python.org/3/library/index.html) and doesn't need to be installed separately.

### [copy](https://docs.python.org/3/library/copy.html)

Also a part of the [The Python Standard Library](https://docs.python.org/3/library/index.html).
