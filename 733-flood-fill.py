class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        source_color = image[sr][sc]
        if source_color == color:
            return image

        self.fill(image, sr, sc, color, source_color)
        return image

    def fill(self, image, row, column, color, old_color):
        #  chach if it goes out of bound and if the current pixel is not the same color as the source
        if row < 0 or column < 0 or row >= len(image) or column >= len(image[0]) or old_color != image[row][column]:
            return

        image[row][column] = color

        self.fill(image, row + 1, column, color, old_color)  # down
        self.fill(image, row - 1, column, color, old_color)  # up
        self.fill(image, row, column + 1, color, old_color)  # right
        self.fill(image, row, column - 1, color, old_color)  # left
