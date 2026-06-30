class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        #starting point sr,sc
        #change point's color to color
        #look lrud repeatedly for pixels that match original color, change to color


        initial_color = image[sr][sc]

        def dfs(image, sr, sc, color, initial_color, visited):

            if min(sr, sc) < 0 or sr == len(image) or sc == len(image[0]) or image[sr][sc] != initial_color or (sr, sc) in visited:
                return image
            
            # if sr == len(image) - 1 and sc == len(image[0]) - 1:
            #     if image[sr][sc] == initial_color:
            #         image[sr][sc] = color
            #     return image

            visited.add((sr,sc))

            image[sr][sc] = color

            dfs(image, sr + 1, sc, color, initial_color, visited)
            dfs(image, sr - 1, sc, color, initial_color, visited)
            dfs(image, sr, sc + 1, color, initial_color, visited)
            dfs(image, sr, sc - 1, color, initial_color, visited)
                
            visited.remove((sr,sc))


            return image
        
        return dfs(image, sr, sc, color, initial_color, set())