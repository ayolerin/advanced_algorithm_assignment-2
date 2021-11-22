#Ayo-Fisher Oluwapamilerin 
# This program will allow the user to find the minimum spanning tree; 

# Here I created a variable for infinity called IFT and I declared it  
IFT = 9999999

# Here I created a variable for the vertices called Ver 
# Variable Ver stores the number of vertices in the graph which is 7
Ver = 7

# Here I created a variable called mat 
# Variable mat has a 2d array of size 7x7 for adjacency matrix to represent graph
mat = [[0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0 ],
    [0, 0, 12, 0, 22, 0, 18],
    [0, 0, 0, 22, 0, 25, 24],
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 34, 0, 0]]
    
# create an array varriable to track the selected vertex 
# if a vertex is selected will become true otherwise false
sel = [0, 0, 0, 0, 0, 0, 0]

# create a variable and set the number of edge to 0
edge_no = 0

# the number of egde in a minimum spanning tree will be always less than(Ver - 1)
# We select vertex 0 and make it True 
sel[0] = True


# print for edge and weight
print("EDGE : WEIGHT\n")

# While loop where it keeps looping if the edge_no is less than Ver - 1
while (edge_no < Ver - 1):
    
    # 
    mini = IFT
    a = 0
    b = 0
    
    # For loop to look for i in the vertices 
    for k in range(Ver):
        # If the vertices is in selected and there is an edge
        if sel[k]:
            for z in range(Ver):
                if ((not sel[z]) and mat[k][z]):  
                    # If the vertices is not in selected and there is an edge
                    if mini > mat[k][z]:
                        mini = mat[k][z]
                        a = k
                        b = z
                        
    # Print the minimum spanning tree 
    print("Node " + str(a+1) + " -" + " Node " + str(b+1) + " :  Weight " + str(mat[a][b]))
    
    #Set the sel as true 
    sel[b] = True
    # Increment the edge_no by 1
    edge_no += 1

# END OF CODE
