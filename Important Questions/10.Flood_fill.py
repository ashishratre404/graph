# Leetcode: 733

class Solution:
    def floodfill(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            return image
        self.floodFill_helper()
        return image
    
    def floodFill_helper(self, image, r, c, newCol, oldCol):
        if (r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c] != oldCol):
            return 
        self.floodFill_helper(image, r+1, c, newCol, oldCol)
        self.floodFill_helper(image, r-1, c, newCol, oldCol)
        self.floodFill_helper(image, r, c+1, newCol, oldCol)
        self.floodFill_helper(image, r, c-1, newCol, oldCol)