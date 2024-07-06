import twophase.solver as sv
import twophase.performance as pf


def main():
    cubestring = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
    print(sv.solve(cubestring, 19, 2))
    # pf.test(100, 0.3)


def ksolve(cubestring):
    return sv.solve(cubestring, 0, 0.4)


if __name__ == "__main__":
    main()
