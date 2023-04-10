import random

#MAZE ALGORITHM
def hunt_n_kill(width, height):
    #Inititalize 2d list
    maze=[[0 for i in range(width*2-1)] for j in range(height*2-1)]
    #Start with first cell
    x=width-1
    y=0
    maze[x][y]=1
    path_length=0
    found = True
    while True:
        #finding univisited neighbors
        unvisited=[]
        #North
        if y>0: #Unvisited
            if maze[x][y-1]==0 and maze[x][y-2]==0:
                unvisited.append('N')
        #South
        if y<((height*2)-2): #Unvisited
            if maze[x][y+1]==0 and maze[x][y+2]==0:
                unvisited.append('S')
        #West
        if x>0: #Unvisited
            if maze[x-1][y]==0 and maze[x-2][y]==0:
                unvisited.append('W')
        #East
        if x<((width*2)-2): #Unvisited
            if maze[x+1][y]==0 and maze[x+2][y]==0:
                unvisited.append('E')
        #Check if there are unvisited neighbors
        if len(unvisited)>0:
            path_length+=1
            direction = random.choice(unvisited)
            if direction=='N':
                maze[x][y+2]=1
                maze[x][y+1]=1
                y+=2
            if direction=='S':
                maze[x][y-2]=1
                maze[x][y-1]=1
                y-=2
            if direction=='W':
                maze[x-2][y]=1
                maze[x-1][y]=1
                x-=2
            if direction=='E':
                maze[x+2][y]=1
                maze[x+1][y]=1
                x+=2
        #If no unvisited neighbors, Find new x,y path starting cell
        else:
            print(path_length)
            path_length=0
            found = False
            # y = i, x = j
            for i in range(height):
                for j in range(height):
                    #move on if a connector cell
                    if i%2!=1 and j%2!=1:
                        continue
                    elif maze[j][i]==0:
                        neighbors=[]
                        if i>0:
                            if maze[x][y-2]==1:
                                neighbors.append('N')
                        if i<((height*2)-2):
                            if maze[x][y+2]==1:
                                neighbors.append('S')
                        if j>=0:
                            if maze[x][y]==1:
                                neighbors.append('W')
                        if j<((width*2)-2):
                            if maze[x][y]==1:
                                neighbors.append('E')
                        #if there are nearby existing paths
                        if len(neighbors)>0:
                            direction=random.choice(neighbors)
                            x=j
                            y=i
                            found=True
                            break
                if found:
                    break
        if not found:
            break
            
    return maze
                        

#PRINT MAZE
def print_maze(maze):
    print(len(maze), "x", len(maze[0]))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            print(maze[x][y], end=" ")
        print("")

#MAIN
if __name__ == "__main__":
    width = 5
    height = 5
    maze = hunt_n_kill(width, height)
    print_maze(maze)