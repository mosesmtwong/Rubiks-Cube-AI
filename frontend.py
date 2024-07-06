from ursina import *
from backend.cube import *

app = Ursina()

cube_colors = [
    color.red,  # right
    color.orange,  # left
    color.yellow,  # top
    color.white,  # bottom
    color.green,  # back
    color.blue,  # front
]

# make a model with a separate color on each face
combine_parent = Entity(enabled=False)
for i in range(3):
    dir = Vec3(0, 0, 0)
    dir[i] = 1

    e = Entity(
        parent=combine_parent,
        model="plane",
        origin_y=-0.5,
        texture="white_cube",
        color=cube_colors[i * 2],
    )
    e.look_at(dir, "up")

    e_flipped = Entity(
        parent=combine_parent,
        model="plane",
        origin_y=-0.5,
        texture="white_cube",
        color=cube_colors[(i * 2) + 1],
    )
    e_flipped.look_at(-dir, "up")

combine_parent.combine()


# place 3x3x3 cubes
cubes = []
for x in range(3):
    for y in range(3):
        for z in range(3):
            e = Entity(
                model=copy(combine_parent.model),
                position=Vec3(x, y, z) - (Vec3(1, 1, 1)),
                texture="white_cube",
            )
            cubes.append(e)


# rotate a side when we click on it
collider = Entity(model="cube", scale=3, collider="box", visible=False)


def collider_input(key):
    if mouse.hovered_entity == collider:
        if key == "left mouse down":
            rotate_side(mouse.normal, 1)
        elif key == "right mouse down":
            rotate_side(mouse.normal, -1)


collider.input = collider_input


rotation_helper = Entity()


def rotate_side(normal, direction=1, speed=0.7):
    if normal == Vec3(1, 0, 0):
        # right
        [setattr(e, "world_parent", rotation_helper) for e in cubes if e.x > 0]
        rotation_helper.animate(
            "rotation_x",
            90 * direction,
            duration=0.15 * speed,
            curve=curve.linear,
            interrupt="finish",
        )
        cube.turn("R" if direction == 1 else "R_p")
    elif normal == Vec3(-1, 0, 0):
        # left
        [setattr(e, "world_parent", rotation_helper) for e in cubes if e.x < 0]
        rotation_helper.animate(
            "rotation_x",
            -90 * direction,
            duration=0.15 * speed,
            curve=curve.linear,
            interrupt="finish",
        )
        cube.turn("L" if direction == 1 else "L_p")
    elif normal == Vec3(0, 1, 0):
        # up
        [setattr(e, "world_parent", rotation_helper) for e in cubes if e.y > 0]
        rotation_helper.animate(
            "rotation_y",
            90 * direction,
            duration=0.15 * speed,
            curve=curve.linear,
            interrupt="finish",
        )
        cube.turn("U" if direction == 1 else "U_p")
    elif normal == Vec3(0, -1, 0):
        # down
        [setattr(e, "world_parent", rotation_helper) for e in cubes if e.y < 0]
        rotation_helper.animate(
            "rotation_y",
            -90 * direction,
            duration=0.15 * speed,
            curve=curve.linear,
            interrupt="finish",
        )
        cube.turn("D" if direction == 1 else "D_p")
    elif normal == Vec3(0, 0, 1):
        # back
        [setattr(e, "world_parent", rotation_helper) for e in cubes if e.z > 0]
        rotation_helper.animate(
            "rotation_z",
            -90 * direction,
            duration=0.15 * speed,
            curve=curve.linear,
            interrupt="finish",
        )
        cube.turn("B" if direction == 1 else "B_p")
    elif normal == Vec3(0, 0, -1):
        # front
        [setattr(e, "world_parent", rotation_helper) for e in cubes if e.z < 0]
        rotation_helper.animate(
            "rotation_z",
            90 * direction,
            duration=0.15 * speed,
            curve=curve.linear,
            interrupt="finish",
        )
        cube.turn("F" if direction == 1 else "F_p")

    invoke(reset_rotation_helper, delay=0.2 * speed)

    if speed:
        collider.ignore_input = True

        @after(0.25 * speed)
        def _():
            collider.ignore_input = False


def reset_rotation_helper():
    [setattr(e, "world_parent", scene) for e in cubes]
    rotation_helper.rotation = (0, 0, 0)


def print_state():
    cube.print_state()


print_button = Button(
    text="print state", color=color.azure, position=(0.7, -0.4), on_click=print_state
)
print_button.fit_to_text()

window.color = color._16
EditorCamera()

cube = Cube()

app.run()
