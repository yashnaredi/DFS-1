#flood fill
#dfs
#time complexity: O(n) where n are number of pixels in the image
#space complexity:O(N)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image==None or image[sr][sc]==newColor:
            return image
        self.fill(image,sr,sc,image[sr][sc],newColor)
        return image
    
    
    #DFS
    def fill(self,image,r,c,initial,newColor):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c] !=initial:
            return
        image[r][c] = newColor
        self.fill(image,r+1,c,initial,newColor)#down
        self.fill(image,r-1,c,initial,newColor)#up
        self.fill(image,r,c+1,initial,newColor)#right
        self.fill(image,r,c-1,initial,newColor)#left

    
        
        
        