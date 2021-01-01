# The SAT problem
### Resume
The SAT (satisfaction) problem is an np problem 
(which has no actual way to resolve it in polynomial time)

Imagine a club which recruit new members.\
They've a list of candidates and each members of 
the club can have demands like this candidates have to be accept
or this one have to be refused.

The problem is NP resolvable but P complexity check, basicly if 
u propose a list of new members from the candidates list it is simple to check if this list fit at least 
one of each member demand.

But in the way to resolve it, it depends on the number of candidates and the maximum number of members demands.

To make this problem as general as possible we'll use different length of members's demands list.
If there is all same some exception can be avoid but the problem should be resolve at general case to prove that P = NP
has a solution.

<a href="https://en.wikipedia.org/wiki/AKS_primality_test">
Recently Indians researcher prove that the primality test can be made in polynomial time.</a>

These major advance in P = NP problem is not efficient enough because primality test is simpler
than number factorisation and this precise problem of factorisation is the base of most of the web security.

If the SAT problem can be resolved in polynomial time too, and because it is a NP complete problem,
it should prove than all NP problem can be translate in a P problem and then 
(obviously but this precision is for the layman) resolved in a polynomial time instead of an exponential one. 

### Why choose SAT instead another NP complete problem?

This problem seems to be the most simpler NP complete problem to be resolve, but this first glance is maybe false.\
Because of my low knowledge on the algorithm already made to resolve this problem I would like to make another approach
using python tools and objects to simulate the problem.

The SAT problem need less math than factorisation or the "sudoku resolver" problem.

And to be honest this problem is my favourite one and I wished to try to resolve it.

### First made the objects we'll need 

