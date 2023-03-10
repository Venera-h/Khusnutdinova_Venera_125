# S - спрос
# D - предложение
import random
S = []
D = []
k = 0
for i in range(random.randint(30,70)):
    S.append(random.randint(1,40))
    D.append(random.randint(1, 40))
    if S[i]==D[i]:
        k+=1
        #print(S[i],D[i])

print("Рынок находился в состоянии равновесия ", k )

