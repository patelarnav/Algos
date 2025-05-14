# implementing hmm algorithm

# sentence : The dog barks
# pos : noun determinant verb

# We need to design the emission probability,(b) transition probablity(a) and starting state probablities(pi)

pos = list(input("Enter the parts of speech in order ").split(" "))
words = list(input("Enter the sentence ").split(" "))

pi = list(map(float,input("Enter the starting state probabilities: ").split(" ")))

l = len(pos)
a = []
for i in range(l):
    v = list(map(float,input(f"Enter the transition probabilities for state {pos[i]}: ").split(" ")))
    a.append(v)

b = []

for i in range(l):
    v = list(map(float,input(f"Enter the emission probabilities for state {pos[i]}: ").split(" ")))
    b.append(v)

dp = [[-1 for _ in range(len(words))] for _  in range(l)]

for i in range(l):
    dp[i][0] = pi[i]*b[i][0]

for j in range(1,len(words)):
    for i in range(l): 
        val = 0
        for k in range(l):
            val = max(val,a[k][i]*dp[k][j-1])
        dp[i][j] = b[i][j]*val

# We can calculate the best previous state(pos) before reaching state Sm at location t

bps = [[-1 for _ in range(len(words))] for _ in range(l)]

for j in range(1,len(words)):
    for i in range(l):
        val = 0
        arg = -1
        for k in range(l):
            if dp[k][j-1]*a[k][i] > val:
                arg = k
                val = dp[k][j-1]*a[k][i]
        
        bps[i][j] = arg

a,b = map(int,input("Enter the position word and the position of state which we want to know the best state before for ").split(" "))
# a, b = map(int, input("Enter the position of word and the position of state (separated by space): ").split())

print(pos[bps[b][a]])



