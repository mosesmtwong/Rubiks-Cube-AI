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
        if state == None:
            self.reset()
        else:
            flat_state = np.array(list(state.split(" ")))
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

    def U_E_D(self, row: int, direction: int):
        """
        direction as viewed from top, 1 for clockwise, -1 for anti
        """

        if direction == 1:
            # One whole face
            if row == 0:
                self.state[0] = np.rot90(self.state[0], axes=(1, 0))
            elif row == 2:
                self.state[1] = np.rot90(self.state[1], axes=(1, 0))

            # Four side rows
            (
                self.state[4][row],
                self.state[3][row],
                self.state[5][row],
                self.state[2][row],
            ) = copy.deepcopy(
                (
                    self.state[2][row],
                    self.state[4][row],
                    self.state[3][row],
                    self.state[5][row],
                )
            )

        elif direction == -1:
            # One whole face
            if row == 0:
                self.state[0] = np.rot90(self.state[0], axes=(0, 1))
            elif row == 2:
                self.state[1] = np.rot90(self.state[1], axes=(0, 1))

            # Four side rows
            (
                self.state[4][row],
                self.state[3][row],
                self.state[5][row],
                self.state[2][row],
            ) = copy.deepcopy(
                (
                    self.state[3][row],
                    self.state[5][row],
                    self.state[2][row],
                    self.state[4][row],
                )
            )

    def R_M_L(self, column: int, direction: int):
        """
        direction as viewed from left, 1 for clockwise, -1 for anti
        column start count from left
        """
        if direction == 1:
            # One whole face
            if column == 0:
                self.state[3] = np.rot90(self.state[3], axes=(1, 0))
            elif column == 2:
                self.state[2] = np.rot90(self.state[2], axes=(0, 1))

            # Four side rows

        elif direction == -1:
            # One whole face
            if column == 0:
                self.state[3] = np.rot90(self.state[3], axes=(0, 1))
            elif column == 2:
                self.state[2] = np.rot90(self.state[2], axes=(1, 0))

            # Four side rows

    def turn(self, actions):
        """
        actions: U D R L F B U_p D_p R_p L_p F_p B_p
        """
        match actions:
            case "U":
                self.U_E_D(0, 1)
            case "U_p":
                self.U_E_D(0, -1)
            case "D":
                self.U_E_D(2, -1)
            case "D_p":
                self.U_E_D(2, 1)
            case "R":
                self.R_M_L(2, -1)
            case "R_p":
                self.R_M_L(2, 1)
            case "L":
                self.R_M_L(0, 1)
            case "L_p":
                self.R_M_L(0, -1)
            case "F":
                pass
            case "F_p":
                pass
            case "D":
                pass
            case "D_p":
                pass

    def print_state(self):
        print(" " * 18, self.state[5][2][::-1])
        print(" " * 18, self.state[5][1][::-1])
        print(" " * 18, self.state[5][0][::-1])
        print(
            [self.state[3][i][0] for i in range(3)[::-1]],
            self.state[0][0],
            [self.state[2][i][2] for i in range(3)],
        )
        print(
            [self.state[3][i][1] for i in range(3)[::-1]],
            self.state[0][1],
            [self.state[2][i][1] for i in range(3)],
        )
        print(
            [self.state[3][i][2] for i in range(3)[::-1]],
            self.state[0][2],
            [self.state[2][i][0] for i in range(3)],
        )
        print(" " * 18, self.state[4][0])
        print(" " * 18, self.state[4][1])
        print(" " * 18, self.state[4][2])
        print("")
        print(" " * 18, self.state[1][0])
        print(" " * 18, self.state[1][1])
        print(" " * 18, self.state[1][2])
        print("")


cube = Cube(
    state="y1 y2 y3 y4 y5 y6 y7 y8 y9 w1 w2 w3 w4 w5 w6 w7 w8 w9 r1 r2 r3 r4 r5 r6 r7 r8 r9 o1 o2 o3 o4 o5 o6 o7 o8 o9 b1 b2 b3 b4 b5 b6 b7 b8 b9 g1 g2 g3 g4 g5 g6 g7 g8 g9"
)

cube.print_state()
cube.turn("R")
cube.print_state()

# print(cube.is_solved())
# print(cube.state)
