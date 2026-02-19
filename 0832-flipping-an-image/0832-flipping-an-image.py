class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        for r in range(m):
            for c in range(n//2):
                swapped_col = n - 1 -c

                image[r][c], image[r][swapped_col] = image[r][swapped_col], image[r][c]
        for r in range(m):
            for c in range(n):

                image[r][c] = int(not image[r][c])

        return image