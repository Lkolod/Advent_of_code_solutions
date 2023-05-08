
crates = [
    ['S','L','F','Z','D','B','R','H'],
    ['R','Z','M','B','T'],
    ['S','N','H','C','L','Z'],
    ['J','F','C','S'],
    ['B','Z','R','W','H','G','P'],
    ['T','M','N','D','G','Z','J','V'],
    ['Q','P','S','F','W','N','L','G'],
    ['R','Z','M'],
    ['T','R','V','G','L','C','M'],
]

with open('ddata5.txt', 'r') as file:
    data = file.read().splitlines()

move = []
fromm = []
to = []

for ii in data:

    sth = ii.split()
    move.append(sth[1])
    fromm.append(sth[3])
    to.append(sth[5])


for i,j,k in zip(move,fromm,to): 

    Move = crates[int(j)-1][len(crates[int(j)-1])-int(i):]
    Move.reverse()
    deleted_Crates = crates[int(j)-1][len(crates[int(j)-1])-int(i):].pop()
    crates[int(k)-1] = crates[int(k)-1] + Move



solution = ''
for item in crates:

    solution += item[-1]

print(crates)
print(solution)

