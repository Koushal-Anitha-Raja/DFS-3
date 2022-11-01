class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the row of the grid
        self.m = len(grid) 
        #n denotes the column of the grid
        self.n = len(grid[0])
        #initialize the count value to zero
        self.count = 0
        #the direction array of four dierction
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        # creating result array
        self.result = [] 
        
        #iterate through the m and n grid values
        for i in range(self.m):
            for j in range(self.n):
                # creating island empty array
                self.island = [] 
                # if grid value is equal to 1
                if grid[i][j] == "1": 
                    #recursive call of function
                    self.dfs(grid,i,j) 
                    # appending island value to result
                    self.result.append(self.island) 
                    self.count +=1 
        #return the cvcount value            
        return self.count 
     
        #the main dfs function
    def dfs(self,grid,i,j):
        #if the grid value is 0 return
        if grid[i][j]=="0":
            return
        
        # appending the i and j value in island array
        self.island.append((i,j)) 
        grid[i][j]="0"
        # iterate through directions array
        for x,y in self.dirs: 
            nr = x+i
            nc = y+j
            
            # boundary check
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n: 
                # dfs function recursion
                self.dfs(grid,nr,nc) 
        