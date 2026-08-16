class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        if m == 0: 
            return image
        n = len(image[0])

        repColor = image[sr][sc]

        def recurse(img, i, j):
            if i < 0: return img
            if i > m - 1: return img
            if j < 0: return img
            if j > n - 1: return img

            val = img[i][j]
            if val != repColor or val == color: 
                return img

            img[i][j] = color

            img = recurse(img, i + 1, j) # Right
            img = recurse(img, i - 1, j) # Left
            img = recurse(img, i, j + 1) # Up
            img = recurse(img, i, j - 1) # Down

            return img

        return recurse(image, sr, sc)
