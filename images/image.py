class Image:
    def __init__(self, width, height, x_offset=0, y_offset=0):
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.grid = [ [ " " for _ in range(self.height) ] for _ in range(self.width) ]
    def get_rect_at(self, x, y):
        return (
            int(x-self.x_offset),
            int(y-self.y_offset),
            self.width,
            self.height,
        )
    @classmethod
    def from_string(cls, string, x_offset=0, y_offset=0):
        """
        "\\nab\\ncd\\n" --> [ ["a", "c"], ["b", "d"] ]
        """
        if string[0] == "\n": string = string[1:]
        if string[-1] == "\n": string = string[:-1]
        lines = string.split("\n")
        width = len(lines[0])
        height = len(lines)
        image = cls(width, height, x_offset, y_offset)
        image.grid = [ [ lines[y][x] for y in range(image.height) ] for x in range(image.width) ]
        return image
    @classmethod
    def from_grid(cls, grid, x_offset=0, y_offset=0):
        """
        [ ["a", "b"], ["c", "d"] ] --> [ ["a", "c"], ["b", "d"] ]
        """
        width = len(grid[0])
        height = len(grid)
        image = cls(width, height, x_offset, y_offset)
        image.grid = [ [ grid[y][x] for y in range(image.height) ] for x in range(image.width) ]
        return image
    def draw_onto(self, image_to, x, y):
        for dx in range(self.width):
            for dy in range(self.height):
                X = x+dx-self.x_offset
                Y = y+dy-self.y_offset
                if X in range(image_to.width) and Y in range(image_to.height):
                    image_to.grid[X][Y] = self.grid[dx][dy]
