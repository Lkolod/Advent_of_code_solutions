import pandas as pd

df = pd.read_csv('ddata.csv',skip_blank_lines=False)
df['numbers'] = df['numbers'].fillna(0).astype(int)



find_max = []
summ = 0
for row in df['numbers']:
    if row == 0:
        find_max.append(summ)
        summ = 0
    else:
        summ += row


find_max = sorted(find_max,reverse=True)
print(sum((find_max[0:3])))
