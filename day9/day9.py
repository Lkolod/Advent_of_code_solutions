from collections import defaultdict


d = defaultdict(list)



with open('ddata9.txt', 'r') as file:
    data = file.read()
    
unique_pos = []
lines = []
T_pos = [0,0]
H_pos = [0,0]

for x in data.split('\n'):
    lines.append(x)

for line in lines:
    
    direction, value = line.split()
    value = int(value)
    for i in range(int(value)):
        if direction == 'R':
            H_pos[0] += 1
        
        elif direction == 'L':
            H_pos[0] -= 1
            
        elif direction == 'U':
            H_pos[1] += 1
        
        elif direction == 'D':
            H_pos[1] -= 1
            
        if H_pos[0] - T_pos[0] > 1:
            T_pos[0] = H_pos[0] -1
            T_pos[1] = H_pos[1]   
           
        
        elif T_pos[0] - H_pos[0] > 1:
            T_pos[0] = H_pos[0] +1
            T_pos[1] = H_pos[1]  
            
            
        elif H_pos[1] - T_pos[1] >1:
            T_pos[1] = H_pos[1] -1
            T_pos[0] = H_pos[0]   
           
        
        elif T_pos[1] - H_pos[1] >1:
            T_pos[1] = H_pos[1] +1
            T_pos[0] = H_pos[0]
        
        
        unique_pos += [[T_pos[0],T_pos[1]]]

solution = []
for item in unique_pos:
    if item not in solution:
        solution.append(item)

print(len(solution))

#PART2

unique_pos = []
lines = []
T_pos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
T_pos_current = []


for x in data.split('\n'):
    lines.append(x)
    
for line in lines:
    
    direction, value = line.split()
    value = int(value)
    for i in range(int(value)):
        if direction == 'R':
            T_pos[0][0] += 1  
            #print(T_pos[0][0])  
        elif direction == 'L':
            T_pos[0][0] -= 1
            
        elif direction == 'U':
            T_pos[0][1] += 1
        
        elif direction == 'D':
            T_pos[0][1] -= 1
        
        for ii in range(1,len(T_pos)):        
            if T_pos[ii-1][0] - T_pos[ii][0] > 1 and T_pos[ii][1] - T_pos[ii-1][1] == 0:
            
                T_pos[ii][0] = T_pos[ii-1][0] - 1
                                       
            elif T_pos[ii-1][0] - T_pos[ii][0] < -1 and T_pos[ii][1] - T_pos[ii-1][1] == 0:
                T_pos[ii][0] = T_pos[ii-1][0] + 1
                    
            elif T_pos[ii-1][1] - T_pos[ii][1] >1 and T_pos[ii][0] - T_pos[ii-1][0] == 0:           
                T_pos[ii][1] = T_pos[ii-1][1] -1
                             
            elif T_pos[ii-1][1]  - T_pos[ii][1] < -1 and T_pos[ii][0] - T_pos[ii-1][0] == 0:
                T_pos[ii][1] = T_pos[ii-1][1] + 1
                  
            elif T_pos[ii-1][0] - T_pos[ii][0] > 1 and T_pos[ii-1][1] - T_pos[ii][1] > 0:
                
                T_pos[ii][1] = T_pos[ii -1][1]
                T_pos[ii][0] = T_pos[ii -1][0] -1          
            
            elif T_pos[ii-1][0] - T_pos[ii][0] > 1 and T_pos[ii-1][1] - T_pos[ii][1] < 0:
                             
                T_pos[ii][1] = T_pos[ii -1][1] 
                T_pos[ii][0] = T_pos[ii -1][0] -1  
                
            elif T_pos[ii-1][0] - T_pos[ii][0] < -1 and T_pos[ii-1][1] - T_pos[ii][1] > 0:
    
                T_pos[ii][1] = T_pos[ii -1][1] 
                T_pos[ii][0] = T_pos[ii -1][0] +1 
            
            elif T_pos[ii-1][0] - T_pos[ii][0] < -1 and T_pos[ii-1][1] - T_pos[ii][1] < 0:
    
                T_pos[ii][1] = T_pos[ii -1][1] 
                T_pos[ii][0] = T_pos[ii -1][0] + 1 
            
            #skos
            elif T_pos[ii-1][0] - T_pos[ii][0] > 1 and T_pos[ii-1][1] - T_pos[ii][1] > 1:
    
                T_pos[ii][1] = T_pos[ii -1][1] -1
                T_pos[ii][0] = T_pos[ii -1][0] -1 
            
            elif T_pos[ii-1][0] - T_pos[ii][0] < -1 and T_pos[ii-1][1] - T_pos[ii][1] < -1:
    
                T_pos[ii][1] = T_pos[ii -1][1] +1
                T_pos[ii][0] = T_pos[ii -1][0] +1    
            
            elif T_pos[ii-1][0] - T_pos[ii][0] < -1 and T_pos[ii-1][1] - T_pos[ii][1] > 1:
    
                T_pos[ii][1] = T_pos[ii -1][1] -1
                T_pos[ii][0] = T_pos[ii -1][0] +1 
                   
            elif T_pos[ii-1][0] - T_pos[ii][0] >1 and T_pos[ii-1][1] - T_pos[ii][1] < -1:
    
                T_pos[ii][1] = T_pos[ii -1][1] +1
                T_pos[ii][0] = T_pos[ii -1][0] -1      
                
        for iii in range(len(T_pos)):
            unique_pos += [[T_pos[iii][0],T_pos[iii][1]]]

        print(T_pos)
        