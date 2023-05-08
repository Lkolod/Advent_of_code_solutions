import pandas as pd

df = pd.read_csv('ddata2.txt', sep=" ",names=["action", "response"])

# A-rock B - paper C- Scissors
# X - rock Y - paper Z-scissors
# lose - 0 draw -3 win - 6

print(df)

sum = 0

for index, row in df.iterrows():
        if row['action'] == 'A' and row['response'] == 'X':
            sum += 3

        elif row['action'] == 'A' and row['response'] == 'Y':
            sum += 4

        elif row['action'] == 'A' and row['response'] == 'Z':
            sum += 8

        elif row['action'] == 'B' and row['response'] == 'Y':
            sum += 5
        
        elif row['action'] == 'B' and row['response']== 'Z':
            sum += 9

        elif row['action'] == 'B' and row['response']== 'X':
            sum += 1

        elif row['action'] == 'C' and row['response'] == 'Z':
            sum += 7

        elif row['action'] == 'C' and row['response'] == 'X':
            sum += 2
        
        elif row['action'] == 'C' and row['response'] == 'Y':
            sum += 6

        else:
            pass
print(sum)