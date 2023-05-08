from collections import defaultdict
with open('ddata7.txt', 'r') as file:
    data = file.readlines()


    current_path = ['/']
    dictionary = defaultdict(int)

    for line in data:

        command = line.split()
        if command[0] == '$':
            if command[1] == 'cd':
                
                if command[2] == '/':
                    current_path = ['/']
                    
                elif command[2] == '..':
                    current_path.pop()

                else:
                    name_of_file = command[2]       
                    current_path.append(name_of_file)              
            elif command[1] == 'ls':               
                pass

        else:
            if command[0] == 'dir':
                pass

            else:                 
                try:
                    file_size = command[0]
                    for i in range(len(current_path)+1):
                        dictionary['/'.join(current_path[0:i])] += int(file_size)          #zapyrac kogos        
                except:
                    pass
       
        
solution = 0                  
for item in dictionary:
    if dictionary[item] <= 100000:
        solution += dictionary[item]
    
print('solution for part 1: ' + str(solution))

solutuion2 = []
for item in dictionary:
    solutuion2.append(dictionary[item])
    outer_dir = max(solutuion2)
    
space_unused = 70000000 - outer_dir
space_needed = 30000000 - space_unused


smallest_dict = lambda value: min(value for value in solutuion2 if value >= space_needed)
print('solution for part 2: ' + str(smallest_dict(solutuion2)))