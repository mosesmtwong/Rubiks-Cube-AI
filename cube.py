import copy
import numpy as np

COLOURS = ["y", "w", "r", "o", "b", "g"]


class Cube:

    def __init__(self, size=3, input_string=None) -> None:
        """
        Yellow on top, Blue in front, Red on right.
        state is 5x5x5 3d array
        input_string: "y y y y y y y y y w w w w w w w w w r r r r r r r r r o o o o o o o o o b b b b b b b b b g g g g g g g g g"
        """
        if size != 3:
            raise NotImplementedError
        self.size = size
        self.colours = COLOURS
        self.state = np.full((5, 5, 5), None)
        if input_string == None:
            self.reset()
        else:
            state_lst = list(input_string.split(" "))
            for i, colour in enumerate(state_lst[0:9]):
                self.state[0, 1:4, 1:4][i // 3][i % 3] = colour  # up
            for i, colour in enumerate(state_lst[9:18]):
                self.state[4, 1:4, 1:4][i // 3][i % 3] = colour  # down
            for i, colour in enumerate(state_lst[18:27]):
                self.state[1:4, 1:4, 4][i // 3][i % 3] = colour  # right
            for i, colour in enumerate(state_lst[27:36]):
                self.state[1:4, 1:4, 0][i // 3][i % 3] = colour  # left
            for i, colour in enumerate(state_lst[36:45]):
                self.state[1:4, 4, 1:4][i // 3][i % 3] = colour  # front
            for i, colour in enumerate(state_lst[45:54]):
                self.state[1:4, 0, 1:4][i // 3][i % 3] = colour  # back

    # Returns a 5x5x5 matrix where the cube is solved
    def solved_state(self) -> np.ndarray:
        state = np.full((5, 5, 5), None)
        state[0, 1:4, 1:4] = COLOURS[0]  # up
        state[4, 1:4, 1:4] = COLOURS[1]  # down
        state[1:4, 1:4, 4] = COLOURS[2]  # right
        state[1:4, 1:4, 0] = COLOURS[3]  # left
        state[1:4, 4, 1:4] = COLOURS[4]  # front
        state[1:4, 0, 1:4] = COLOURS[5]  # back
        return state

    # Returns True if cube is solved
    def is_solved(self) -> bool:
        return self.state == self.solved_state()

    # Set cube back to solved state
    def reset(self) -> None:
        self.state = self.solved_state()

    def print_state(self, d) -> None:
        """
        d is the number of space to put before to align the matrix
        12 for normal
        15 for numbered colours
        """
        up = self.state[0, 1:4, 1:4]
        down = self.state[4, 1:4, 1:4]
        right = self.state[1:4, 1:4, 4].T
        left = np.rot90(self.state[1:4, 1:4, 0], axes=(1, 0))
        front = self.state[1:4, 4, 1:4]
        back = self.state[1:4, 0, 1:4][::-1]

        print(" " * (d + 1), back[0], "\n", " " * d, back[1], "\n", " " * d, back[2])
        print(left[0], up[0], right[0])
        print(left[1], up[1], right[1])
        print(left[2], up[2], right[2])
        print(" " * (d + 1), front[0], "\n", " " * d, front[1], "\n", " " * d, front[2])
        print("")
        print(" " * (d + 1), down[0], "\n", " " * d, down[1], "\n", " " * d, down[2])
        print(" ")

    def turn(self, action):
        """
        actions: U D R L F B U_p D_p R_p L_p F_p B_p
        """
        match action:
            case "U":
                self.state[:2] = np.rot90(self.state[:2], axes=(2, 1))
            case "U_p":
                self.state[:2] = np.rot90(self.state[:2], axes=(1, 2))
            case "D":
                self.state[3:] = np.rot90(self.state[3:], axes=(1, 2))
            case "D_p":
                self.state[3:] = np.rot90(self.state[3:], axes=(2, 1))
            case "R":
                self.state[:, :, 3:] = np.rot90(self.state[:, :, 3:], axes=(0, 1))
            case "R_p":
                self.state[:, :, 3:] = np.rot90(self.state[:, :, 3:], axes=(1, 0))
            case "L":
                self.state[:, :, :2] = np.rot90(self.state[:, :, :2], axes=(1, 0))
            case "L_p":
                self.state[:, :, :2] = np.rot90(self.state[:, :, :2], axes=(0, 1))
            case "F":
                self.state[:, 3:] = np.rot90(self.state[:, 3:], axes=(2, 0))
            case "F_p":
                self.state[:, 3:] = np.rot90(self.state[:, 3:], axes=(0, 2))
            case "B":
                self.state[:, :2] = np.rot90(self.state[:, :2], axes=(0, 2))
            case "B_p":
                self.state[:, :2] = np.rot90(self.state[:, :2], axes=(2, 0))

    def sequence(self, seq: list):
        for action in seq:
            action = action.replace("'", "_p")
            self.turn(action)


cube = Cube(
    input_string="y1 y2 y3 y4 y5 y6 y7 y8 y9 w1 w2 w3 w4 w5 w6 w7 w8 w9 r1 r2 r3 r4 r5 r6 r7 r8 r9 o1 o2 o3 o4 o5 o6 o7 o8 o9 b1 b2 b3 b4 b5 b6 b7 b8 b9 g1 g2 g3 g4 g5 g6 g7 g8 g9"
)

cube.sequence(["F"])
# print(cube.state)
cube.print_state(d=15)


# print(cube.is_solved())
# cube = Cube()
# print(cube.state)
# cube.print_state()
