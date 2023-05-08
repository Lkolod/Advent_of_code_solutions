import pandas as pd

df = pd.read_csv('ddata8.txt',header=None,names=['tree_'])
new_df = df.tree_.apply(lambda x: pd.Series(list(str(x)))).astype(int)
df_to_iterate = new_df.drop(df.tail(1).index,inplace=False).drop(df.head(1).index,inplace=False).drop(columns=new_df.columns[-1], inplace=False).drop(columns=new_df.columns[0], inplace=False).astype(int)


visible_trees = 0

# PART 1 

for i in range(1,len(df_to_iterate[1])+1):
    for j in range(1,len(df_to_iterate[1])+1):
 
        # condition for collumns 
        
        if all(item < df_to_iterate[i][j] for item in list(new_df[i].values)[j+1:]) or all(item < df_to_iterate[i][j] for item in list(new_df[i].values)[:j]):
            visible_trees += 1 

        # condition for rows 
        
        elif (all(item < df_to_iterate[i][j] for item in list(new_df.iloc[j].values)[i+1:])) or (all(item < df_to_iterate[i][j] for item in list(new_df.iloc[j].values)[:i])):
            visible_trees += 1 

  
#trees on the edges 
left_edge = len(df_to_iterate[1])
right_edge = len(df_to_iterate.iloc[:, -1])
top_edge = len(new_df.iloc[0, :])
bottom_edge = len(new_df.iloc[-1, :])

visible_trees = visible_trees + left_edge + right_edge + top_edge + bottom_edge

print(visible_trees)     

# PART 2
visible_trees_down = 0
visible_trees_up = 0
visible_trees_left = 0
visible_trees_right = 0

visibility = 0
visibility_list = []



for i in range(1,len(df_to_iterate[1])+1):
    for j in range(1,len(df_to_iterate[1])+1):
        
        #looking down  
        for item in list(new_df[i].values)[j+1:]:            
            if item >= df_to_iterate[i][j]:    
                visible_trees_down += 1
                break
            else:
                visible_trees_down += 1   
           
        #looking up      
        new_list = list(new_df[i].values)[:j]
        new_list.reverse()
        for item in new_list:               
            if item >= df_to_iterate[i][j]:
                visible_trees_up += 1
                break
            else:
                visible_trees_up += 1
          
                
        #looking right
        for item in list(new_df.iloc[j].values)[i+1:]:
            if item < df_to_iterate[i][j]:
                visible_trees_right += 1
            elif item >= df_to_iterate[i][j]:
                visible_trees_right += 1
                break
        
        new_list = list(new_df.iloc[j].values)[:i]
        new_list.reverse()
        #looking left
        for item in new_list:
            if item < df_to_iterate[i][j]:
                visible_trees_left += 1
            elif item >= df_to_iterate[i][j]:
                visible_trees_left += 1
                break
                
   
        visibility = visible_trees_up* visible_trees_down* visible_trees_right* visible_trees_left
        visibility_list.append(visibility)
        
        visible_trees_up = 0
        visible_trees_down = 0
        visible_trees_right = 0
        visible_trees_left = 0
        

print(max(visibility_list))