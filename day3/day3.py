import pandas as pd

alphaa = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 
'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

df = pd.read_csv('ddata3.txt', names=["letters"])

count = 0
count2 = 0
solution = []
solution2 = []

#first part

for row in df['letters']:
    first_half = row[:len(row)//2]
    second_half = row[len(row)//2:]

    for n in first_half:
        if n in second_half:
            solution.append(n)
            break

for n in solution:
    if n.isupper():
        n = n.lower()
        count += alphaa[n] + 26
    else:
        count += alphaa[n]

#second part

for i in range(0,len(df['letters']),3):
    badge1 = df['letters'].iloc[i]
    badge2 = df['letters'].iloc[i+1]
    badge3 = df['letters'].iloc[i+2]

    for item in badge1:
        if item in badge2 and item in badge3:
            solution2.append(item)
            break

for n in solution2:
    if n.isupper():
        n = n.lower()
        count2 += alphaa[n] + 26
    else:
        count2 += alphaa[n]

print('solution for part1:' + str(count))
print('solution for part2:' + str(count2))
    
