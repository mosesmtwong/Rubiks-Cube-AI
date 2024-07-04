import numpy as np


class Cube:

    def __init__(self, size=3, state=None, colours=["y", "w", "o", "r", "b", "g"]):
        """
        Yellow on top, Blue in front, Red on right.
        state is array of faces: [U D L R F B]
        input to state is string: "yyyyyyyyywwwwwwwwwooooooooorrrrrrrrrbbbbbbbbbggggggggg"
        """
        if size != 3:
            raise NotImplementedError
        self.size = size
        self.colours = colours
        if state == None:
            self.reset()
        else:
            flat_state = np.array([*state])
            self.state = np.reshape(flat_state, (6, 3, 3))

    def is_solved(self) -> bool:
        """
        Returns True if cube is solved
        """
        for face in self.state:
            checking_set = set(face.flatten())
            if len(checking_set) != 1:
                return False
        return True

    def reset(self):
        """
        Set cube back to solved state
        """
        self.state = [
            [[colour for x in range(self.size)] for y in range(self.size)]
            for colour in self.colours
        ]
        self.state = np.array(self.state)

    def turn(self, face, direction):
        """
        face:       U D L R F B
        direction:  clock, anti
        """
        raise NotImplementedError

    def print_state(self):
        print(" " * 15, self.state[5][2][::-1])
        print(" " * 15, self.state[5][1][::-1])
        print(" " * 15, self.state[5][0][::-1])
        print(
            [self.state[2][i][0] for i in range(3)[::-1]],
            self.state[0][0],
            [self.state[3][i][2] for i in range(3)],
        )
        print(
            [self.state[2][i][1] for i in range(3)[::-1]],
            self.state[0][1],
            [self.state[3][i][1] for i in range(3)],
        )
        print(
            [self.state[2][i][2] for i in range(3)[::-1]],
            self.state[0][2],
            [self.state[3][i][0] for i in range(3)],
        )
        print(" " * 15, self.state[4][0])
        print(" " * 15, self.state[4][1])
        print(" " * 15, self.state[4][2])
        print(" " * 15, self.state[1][0])
        print(" " * 15, self.state[1][1])
        print(" " * 15, self.state[1][2])


# cube = Cube(state="abcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghi")
cube = Cube()
cube.print_state()

# print(cube.is_solved())
# print(cube.state)
