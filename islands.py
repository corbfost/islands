import random

class Grid(object):
    def __init__(self, size, land, water):
        '''
        size = shape tuple
        e.g. (5, 3) for matrix with 5 rows, 3 columns
        '''
        self.size = size
        self.land = land
        self.water = water
        self.matrix = self.create_matrix()
        self.matrix2d = self.make2d()
        # Dictionary to store checked points in matrix
        self.checked = {}
        # Initialize num islands
        self.islands = 0

    def create_matrix(self):
        matrix = []
        for r in range(0, self.size[0]):
            for c in range(0, self.size[1]):
                matrix.append(random.choice([self.land, self.water]))
        return matrix

    def make2d(self):
        matrix2d = []
        i = 0
        for r in range(0, self.size[0]):
            matrix2d.append(self.matrix[i:i + self.size[0]])
            i += self.size[0]
        return matrix2d

    def num_islands(self):
        '''
        Strategy - begin upper left
        if value == 0 or does not exist, step right again
        If right == 0 or does not exist or checked, then step down
        If down == 0 or does not exist or checked, then step left
        If left == 0 or does not exist or checked, then step up
        If up == 0 or does not exist or checked, then islands += 1
        '''
        for i in range(0, self.size[0] + 1):
            for j in range(0, self.size[1] + 1):
                if self.checker((i, j)):
                    self.islands += self.search((i, j))
        return self.islands


    def search(self, location):
        r = location[0]
        c = location[1]
        poss = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for p in poss:
            if self.checker(p):
                self.search(p)
            else:
                continue
        return 1

    def checker(self, location):
        '''
        Helper function to check if current location exists in matrix, hasn't
        been checked, and is land.
        If these are all true, then return True. Else return False.
        '''
        r = location[0]
        c = location[1]
        # Begin annoying dictionary logic, and see if I already checked.
        if r in self.checked:
            if c in self.checked[r]:
                return False
            self.checked[r] += [c]
        else:
            self.checked[r] = [c]
        # ----
        # Begin check for existence in matrix (try .. except) and land value.
        try:
            if self.matrix2d[r][c] == self.land:
                return True
            else:
                return False
        except:
            return False

    def __str__(self):
        output = ""
        for m in range(self.size[1], len(self.matrix) + 1, self.size[1]):
            output += "  ".join([str(n) for n in self.matrix[m-self.size[1]:m]])
            output += "\n"
        return output
