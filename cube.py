import copy
import numpy as np


class Cube:

    def __init__(self, size=3, state=None, colours=["y", "w", "r", "o", "b", "g"]):
        """
        Yellow on top, Blue in front, Red on right.
        state is array of faces: [U D R L F B]
        input to state is string: "y y y y y y y y y w w w w w w w w w r r r r r r r r r o o o o o o o o o b b b b b b b b b g g g g g g g g g"
        """
        if size != 3:
            raise NotImplementedError
        self.size = size
        self.colours = colours
        self.state = np.full((5, 5, 5), None)
        if state == None:
            self.reset()
        else:
            raise NotImplementedError

    def solved_state(self) -> np.ndarray:
        state = np.full((5, 5, 5), None)
        state[0, 1:4, 1:4] = "y"
        state[4, 1:4, 1:4] = "w"
        state[1:4, 1:4, 4] = "r"
        state[1:4, 1:4, 0] = "o"
        state[1:4, 4, 1:4] = "b"
        state[1:4, 0, 1:4] = "g"
        return state

    def is_solved(self) -> bool:
        """
        Returns True if cube is solved
        """
        return self.state == self.solved_state()

    def reset(self):
        """
        Set cube back to solved state
        """
        self.state = self.solved_state()

    def print_state(self):
        up = self.state[0, 1:4, 1:4]
        down = self.state[4, 1:4, 1:4]
        right = self.state[1:4, 1:4, 4]
        left = self.state[1:4, 1:4, 0]
        front = self.state[1:4, 4, 1:4]
        back = self.state[1:4, 0, 1:4]

        print(" " * 13, back[0], "\n", " " * 12, back[1], "\n", " " * 12, back[2])
        print(left[0], up[0], right[0])
        print(left[1], up[1], right[1])
        print(left[2], up[2], right[2])
        print(" " * 13, front[0], "\n", " " * 12, front[1], "\n", " " * 12, front[2])
        print("")
        print(" " * 13, down[0], "\n", " " * 12, down[1], "\n", " " * 12, down[2])
        print(" ")


# cube = Cube(
#     state="y1 y2 y3 y4 y5 y6 y7 y8 y9 w1 w2 w3 w4 w5 w6 w7 w8 w9 r1 r2 r3 r4 r5 r6 r7 r8 r9 o1 o2 o3 o4 o5 o6 o7 o8 o9 b1 b2 b3 b4 b5 b6 b7 b8 b9 g1 g2 g3 g4 g5 g6 g7 g8 g9"
# )

# cube.print_state()
# cube.turn("R")
# cube.print_state()

# print(cube.is_solved())
cube = Cube()
# print(cube.state)
cube.print_state()
