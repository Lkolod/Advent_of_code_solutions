
with open('ddata6.txt', 'r') as file:
    data = file.read()


# firt_part
def unique(s):
    uchars = set()
    for c in s:
        if c in uchars:
            return False
        uchars.add(c)
    return True


for i in range(len(data)-3): # subtrac 3 in order to not go out of range 
    group = [data[i],data[i+1],data[i+2],data[i+3]]
    if unique(group) == True:
        print(i+4) # in order to find first marker we add 3 to acces last element of group and 1 since we iterating from 0
        break

#second part

for ii in range(len(data)-13): # group consist of 14 characters so we need to substract 13
    group = [data[ii+x] for x in range(14)]
    if unique(group) == True:
        print(ii+14) 
        break



