class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
   # setting direction array
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]] 
    # assigning image value to colorTBC
        self.colorTBC = image[sr][sc] 
         # assinging color to fillwith
        self.fillWith = color
        self.image = image
        #the length of the row is stored
        self.m = len(image) 
        #column is stored as 0 th column
        self.n = len(image[0])
        
        
        # if color is equal to colorTBC
        if self.colorTBC == color: 
            return image 
        
        #  dfs function is recursively called
        self.dfs(sr,sc) 
        return self.image
    
    
    #the main dfs function
    def dfs(self,sr,sc):
        # assigning fillwith to image grid
        self.image[sr][sc] = self.fillWith 
        #  direction array
        for x,y in self.dirs: 
            nr = x+sr
            nc = y+sc
            
            # boundary check
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n and self.image[nr][nc] == self.colorTBC: 
                # calling dfs function recursively
                self.dfs(nr,nc) 
                
        return