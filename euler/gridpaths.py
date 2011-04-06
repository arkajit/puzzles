# Project Euler Problem 15
N = 20
S = [[0 for i in range(N+1)] for j in range(N+1)] # scores table

# initialize table
S[0] = [1 for j in range(N+1)]
for i in range(N+1):
	S[i][0] = 1

# apply recurrence relation
for i in range(1,N+1):
	for j in range(1,N+1):
		S[i][j] = S[i-1][j] + S[i][j-1]

print S[N][N]
# also can confirm by checking that this is 40C20
# in general, the number of paths will be (2N)C(N) since there are 2N steps and
# we have to choose which N will be down (or right)
