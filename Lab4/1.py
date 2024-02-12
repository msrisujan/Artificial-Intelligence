class puzzle:
    def __init__(self):
        self.initial_state=[[1,2,3],[4,5,6],[0,7,8]]
        self.goal_state=[[1,2,3],[4,5,6],[7,8,0]]
        self.directions=[[0,1],[1,0],[-1,0],[0,-1]]
    def find_zero(self,state):
        for i in range(3):
            for j in range(3):
                if state[i][j]==0:
                    return i,j
   
    def is_goal_state(self,state):
        return self.goal_state==state
   
    def dfs(self):
        visited=[]
        stack=[self.initial_state]
       
        while(stack):
            current_state=stack.pop()
            if current_state not in visited:
                visited.append(current_state)
            if self.is_goal_state(current_state):
                return visited
            k,m=self.find_zero(current_state)
            for x in self.directions:
                new=[x.copy() for x in current_state]
                if k+x[0]<3 and m+x[1]<3 and k+x[0]>-1 and m+x[1]>-1:
                    i=x[0]
                    j=x[1]
                    temp=new[k][m]
                    new[k][m]=new[k+i][m+j]
                    new[k+i][m+j]=temp
                    if new not in visited:
                        stack.append(new)
                       
    def bfs(self):
        visited=[]
        queue=[self.initial_state]
       
        while(queue):
            current_state=queue.pop(0)
            if current_state not in visited:
                visited.append(current_state)
            if self.is_goal_state(current_state):
                return visited
            k,m=self.find_zero(current_state)
            for x in self.directions:
                new=[x.copy() for x in current_state]
                if k+x[0]<3 and m+x[1]<3 and k+x[0]>-1 and m+x[1]>-1:
                    i=x[0]
                    j=x[1]
                    temp=new[k][m]
                    new[k][m]=new[k+i][m+j]
                    new[k+i][m+j]=temp
                    if new not in visited:
                        queue.append(new)

t=puzzle()
x=t.bfs()
print("BFS: ",len(x))
y = t.dfs()
print("DFS: ",len(y))