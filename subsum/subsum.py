# Subset Sum Problem
# Input: A list of integers
# Output: A non-empty subset of the integers that sums to 0
# 
# NP-complete, but a reasonable polynomial-time solution can still be found
# when input values are polynomial
# see http://en.wikipedia.org/wiki/Subset_sum_problem for more details on the
# algorithm used here

import sys

n = int(sys.stdin.readline())
names = []
vals = [] 

P = 0 # sum of positive activities
N = 0 # sum of negative activities

Q = [] 
# 2D feasibility matrix indexed by i and s
# Q[i][s] = whether the subset vals[0:i] has a subsum of s

R = [] 
# pointers matrix with a number that should be interpreted as a bit vector
# LSB is whether the last val (vals[n-1]) was included or not in the solution
# for the corresponding subproblem recorded in Q
# bit representation is at most n bits, but leading zeros are suppressed

# read input
for i in range(n) :
	line = sys.stdin.readline()
	(name, val) = line.split(' ')
	val = int(val)
	names.append(name)
	vals.append(val)
	Q.append({})
	R.append({})

	if val > 0 :
		P += val
	elif val < 0 :
		N += val
	else : # value is 0 and so is a valid subset with sum 0
		print name
		sys.exit(0)

# need both positive and negative numbers to make subsum 0
if N == 0 or P == 0 :
	print "no solution"
	sys.exit(0)

# fill out feasibility matrix in bottom-up fashion
for s in range(N, P+1) :
	if (vals[0] == s) :
		Q[0][s] = True
		R[0][s] = 1
	else :
		Q[0][s] = False
		R[0][s] = 0 

for i in range(1, n) :
	for s in range(N, P+1) :
		diff = s - vals[i]
		if Q[i-1][s] :
			Q[i][s] = True
			R[i][s] = 2 * R[i-1][s]
		elif vals[i] == s :
			Q[i][s] = True
			R[i][s] = 1
		elif diff >= N and diff <= P and Q[i-1][diff] :
			Q[i][s] = True
			R[i][s] = 2 * R[i-1][diff] + 1
		else :
			Q[i][s] = False
			R[i][s] = 0 

if Q[-1][0] :
	ptr = R[-1][0]
	acts = []
	for i in range(1, n+1) :
		if ptr % 2 :
			acts.append(names[-i])
		ptr /= 2
	acts.sort()
	for act in acts :
		print act
else :
	print "no solution"		
