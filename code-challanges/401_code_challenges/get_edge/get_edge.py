from graphs.graph import Graph

def get_edges(g,verticies_list):
    sum=0
    for i in range(0, len(verticies_list)-1):
        found=False
        for neighbor in g.get_neighbors(verticies_list[i]):
            if verticies_list[i+1] == neighbor[0]:
                sum+=neighbor[1]
                found=True
        if found == False :
            return(False,0)            
    return (True, sum)
            
                