# Color numbers
# orange = 1
# green = 2
# white = 3
# blue = 4
# red = 5
# yellow = 6
import copy


class Cube:
    def __init__(self, surfaces):
        self.surfaces = surfaces


class Node:
    def __init__(self, cube, depth):
        self.cube = cube
        self.depth = depth
        self.children = []


class Moves:
    def __init__(self, cube):
        self.cube = cube

    def rotate_clockwise(self):
        temp = copy.deepcopy(self.cube)

        # first surface
        self.cube.surfaces[2].blocks[0] = copy.deepcopy(temp.surfaces[2].blocks[2])
        self.cube.surfaces[2].blocks[1] = copy.deepcopy(temp.surfaces[2].blocks[0])
        self.cube.surfaces[2].blocks[2] = copy.deepcopy(temp.surfaces[2].blocks[3])
        self.cube.surfaces[2].blocks[3] = copy.deepcopy(temp.surfaces[2].blocks[1])

        # other surfaces
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[1].blocks[3])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[1].blocks[1])

        self.cube.surfaces[3].blocks[0] = copy.deepcopy(temp.surfaces[0].blocks[2])
        self.cube.surfaces[3].blocks[2] = copy.deepcopy(temp.surfaces[0].blocks[3])

        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[3].blocks[2])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[3].blocks[0])

        self.cube.surfaces[1].blocks[1] = copy.deepcopy(temp.surfaces[4].blocks[0])
        self.cube.surfaces[1].blocks[3] = copy.deepcopy(temp.surfaces[4].blocks[1])

    def rotate_counter_clockwise(self):
        temp = copy.deepcopy(self.cube)

        # first surface
        self.cube.surfaces[2].blocks[0] = copy.deepcopy(temp.surfaces[2].blocks[1])
        self.cube.surfaces[2].blocks[1] = copy.deepcopy(temp.surfaces[2].blocks[3])
        self.cube.surfaces[2].blocks[2] = copy.deepcopy(temp.surfaces[2].blocks[0])
        self.cube.surfaces[2].blocks[3] = copy.deepcopy(temp.surfaces[2].blocks[2])

        # other surfaces
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[3].blocks[0])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[3].blocks[2])

        self.cube.surfaces[3].blocks[0] = copy.deepcopy(temp.surfaces[4].blocks[1])
        self.cube.surfaces[3].blocks[2] = copy.deepcopy(temp.surfaces[4].blocks[0])

        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[1].blocks[1])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[1].blocks[3])

        self.cube.surfaces[1].blocks[1] = copy.deepcopy(temp.surfaces[0].blocks[3])
        self.cube.surfaces[1].blocks[3] = copy.deepcopy(temp.surfaces[0].blocks[2])

    def turn_right(self):
        temp = copy.deepcopy(self.cube)

        # change surfaces
        self.cube.surfaces[2] = copy.deepcopy(temp.surfaces[1])
        self.cube.surfaces[3] = copy.deepcopy(temp.surfaces[2])
        self.cube.surfaces[1] = copy.deepcopy(temp.surfaces[5])
        self.cube.surfaces[5] = copy.deepcopy(temp.surfaces[3])

        # rotate surfaces
        self.cube.surfaces[0].blocks[0] = copy.deepcopy(temp.surfaces[0].blocks[1])
        self.cube.surfaces[0].blocks[1] = copy.deepcopy(temp.surfaces[0].blocks[3])
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[0].blocks[0])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[0].blocks[2])

        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[4].blocks[1])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[4].blocks[3])
        self.cube.surfaces[4].blocks[2] = copy.deepcopy(temp.surfaces[4].blocks[0])
        self.cube.surfaces[4].blocks[3] = copy.deepcopy(temp.surfaces[4].blocks[2])

    def turn_left(self):
        temp = copy.deepcopy(self.cube)

        # change surfaces
        self.cube.surfaces[2] = copy.deepcopy(temp.surfaces[3])
        self.cube.surfaces[1] = copy.deepcopy(temp.surfaces[2])
        self.cube.surfaces[5] = copy.deepcopy(temp.surfaces[1])
        self.cube.surfaces[3] = copy.deepcopy(temp.surfaces[5])

        # rotate surfaces
        self.cube.surfaces[0].blocks[0] = copy.deepcopy(temp.surfaces[0].blocks[2])
        self.cube.surfaces[0].blocks[1] = copy.deepcopy(temp.surfaces[0].blocks[0])
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[0].blocks[3])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[0].blocks[1])

        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[4].blocks[2])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[4].blocks[0])
        self.cube.surfaces[4].blocks[2] = copy.deepcopy(temp.surfaces[4].blocks[3])
        self.cube.surfaces[4].blocks[3] = copy.deepcopy(temp.surfaces[4].blocks[1])

    def turn_up(self):
        temp = copy.deepcopy(self.cube)

        # change surfaces
        self.cube.surfaces[0] = copy.deepcopy(temp.surfaces[2])
        self.cube.surfaces[2] = copy.deepcopy(temp.surfaces[4])

        # rotate surfaces
        self.cube.surfaces[1].blocks[0] = copy.deepcopy(temp.surfaces[1].blocks[2])
        self.cube.surfaces[1].blocks[1] = copy.deepcopy(temp.surfaces[1].blocks[0])
        self.cube.surfaces[1].blocks[2] = copy.deepcopy(temp.surfaces[1].blocks[3])
        self.cube.surfaces[1].blocks[3] = copy.deepcopy(temp.surfaces[1].blocks[1])

        self.cube.surfaces[3].blocks[0] = copy.deepcopy(temp.surfaces[3].blocks[2])
        self.cube.surfaces[3].blocks[1] = copy.deepcopy(temp.surfaces[3].blocks[0])
        self.cube.surfaces[3].blocks[2] = copy.deepcopy(temp.surfaces[3].blocks[3])
        self.cube.surfaces[3].blocks[3] = copy.deepcopy(temp.surfaces[3].blocks[1])

        # special surfaces
        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[5].blocks[3])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[5].blocks[2])
        self.cube.surfaces[4].blocks[2] = copy.deepcopy(temp.surfaces[5].blocks[1])
        self.cube.surfaces[4].blocks[3] = copy.deepcopy(temp.surfaces[5].blocks[0])

        self.cube.surfaces[5].blocks[0] = copy.deepcopy(temp.surfaces[0].blocks[3])
        self.cube.surfaces[5].blocks[1] = copy.deepcopy(temp.surfaces[0].blocks[2])
        self.cube.surfaces[5].blocks[2] = copy.deepcopy(temp.surfaces[0].blocks[1])
        self.cube.surfaces[5].blocks[3] = copy.deepcopy(temp.surfaces[0].blocks[0])

    def turn_down(self):
        temp = copy.deepcopy(self.cube)

        # change surfaces
        self.cube.surfaces[2] = copy.deepcopy(temp.surfaces[0])
        self.cube.surfaces[4] = copy.deepcopy(temp.surfaces[2])

        # rotate surfaces
        self.cube.surfaces[1].blocks[0] = copy.deepcopy(temp.surfaces[1].blocks[1])
        self.cube.surfaces[1].blocks[1] = copy.deepcopy(temp.surfaces[1].blocks[3])
        self.cube.surfaces[1].blocks[2] = copy.deepcopy(temp.surfaces[1].blocks[0])
        self.cube.surfaces[1].blocks[3] = copy.deepcopy(temp.surfaces[1].blocks[2])

        self.cube.surfaces[3].blocks[0] = copy.deepcopy(temp.surfaces[3].blocks[1])
        self.cube.surfaces[3].blocks[1] = copy.deepcopy(temp.surfaces[3].blocks[3])
        self.cube.surfaces[3].blocks[2] = copy.deepcopy(temp.surfaces[3].blocks[0])
        self.cube.surfaces[3].blocks[3] = copy.deepcopy(temp.surfaces[3].blocks[2])

        # special surfaces
        self.cube.surfaces[0].blocks[0] = copy.deepcopy(temp.surfaces[5].blocks[3])
        self.cube.surfaces[0].blocks[1] = copy.deepcopy(temp.surfaces[5].blocks[2])
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[5].blocks[1])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[5].blocks[0])

        self.cube.surfaces[5].blocks[0] = copy.deepcopy(temp.surfaces[4].blocks[3])
        self.cube.surfaces[5].blocks[1] = copy.deepcopy(temp.surfaces[4].blocks[2])
        self.cube.surfaces[5].blocks[2] = copy.deepcopy(temp.surfaces[4].blocks[1])
        self.cube.surfaces[5].blocks[3] = copy.deepcopy(temp.surfaces[4].blocks[0])

    # turns with number
    def turns(self, turn_number):
        if turn_number == 0:
            Moves.rotate_clockwise(self)
            return self.cube

        if turn_number == 1:
            Moves.rotate_counter_clockwise(self)
            return self.cube

        if turn_number == 2:
            Moves.turn_right(self)
            Moves.rotate_clockwise(self)
            Moves.turn_left(self)
            return self.cube

        if turn_number == 3:
            Moves.turn_right(self)
            Moves.rotate_counter_clockwise(self)
            Moves.turn_left(self)
            return self.cube

        if turn_number == 4:
            Moves.turn_left(self)
            Moves.rotate_clockwise(self)
            Moves.turn_right(self)
            return self.cube

        if turn_number == 5:
            Moves.turn_left(self)
            Moves.rotate_counter_clockwise(self)
            Moves.turn_right(self)
            return self.cube

        if turn_number == 6:
            Moves.turn_up(self)
            Moves.rotate_clockwise(self)
            Moves.turn_down(self)
            return self.cube

        if turn_number == 7:
            Moves.turn_up(self)
            Moves.rotate_counter_clockwise(self)
            Moves.turn_down(self)
            return self.cube

        if turn_number == 8:
            Moves.turn_down(self)
            Moves.rotate_clockwise(self)
            Moves.turn_up(self)
            return self.cube

        if turn_number == 9:
            Moves.turn_down(self)
            Moves.rotate_counter_clockwise(self)
            Moves.turn_up(self)
            return self.cube

        if turn_number == 10:
            Moves.turn_right(self)
            Moves.turn_right(self)
            Moves.rotate_clockwise(self)
            Moves.turn_left(self)
            Moves.turn_left(self)
            return self.cube

        if turn_number == 11:
            Moves.turn_right(self)
            Moves.turn_right(self)
            Moves.rotate_counter_clockwise(self)
            Moves.turn_left(self)
            Moves.turn_left(self)
            return self.cube

    def is_correct(self):
        for i in self.cube.surfaces:
            surface_color = i.blocks[0].color_number
            for j in i.blocks:
                if j.color_number != surface_color:
                    return False
        return True

    def is_same(self, cube2):
        for i in range(6):
            for j in range(4):
                if self.cube.surfaces[i].blocks[j].color_number != cube2.surfaces[i].blocks[j].color_number:
                    return False
        return True


class Surface:
    def __init__(self, blocks):
        self.blocks = blocks


class Block:
    def __init__(self, color_number):
        self.color_number = color_number


def get_input():
    blocks = []
    surfaces = []
    for i in range(5):
        string = input().split(" ")
        blocks.clear()
        for j in range(4):
            block = Block(string[j])
            blocks.append(block)
        surface = Surface(blocks)
        surfaces.append(copy.deepcopy(surface))
    # change the 6th surface
    string = input().split(" ")
    blocks.clear()
    block1 = Block(string[3])
    block2 = Block(string[2])
    block3 = Block(string[1])
    block4 = Block(string[0])
    blocks = [block1, block2, block3, block4]
    surface = Surface(blocks)
    surfaces.append(copy.deepcopy(surface))
    return Cube(surfaces)


def dls(limit, frontier, explored):
    if limit == 0 or len(frontier) == 0:
        return False
    parent = frontier.pop()
    if Moves(parent).is_correct():
        return True
    explored.append(parent)
    for i in range(6):
        child = Moves(copy.deepcopy(parent)).turns(i * 2)
        for exp in explored:
            if Moves(child).is_same(exp):
                continue
        for fro in frontier:
            if Moves(child).is_same(fro):
                continue
        frontier.append(copy.deepcopy(child))
        result = dls(limit - 1, frontier, explored)
        if result:
            print("found")


def ids(cube, min_depth, max_depth):
    for i in range(min_depth, max_depth):
        frontier = [cube]
        explored = []
        result = dls(i, frontier, explored)
        if result:
            print("found")


def get_correct_cube():
    surfaces = []
    for i in range(1, 7):
        blocks = [Block(i), Block(i), Block(i), Block(i)]
        surfaces.append(copy.deepcopy(blocks))
    return Cube(surfaces)


def bfs(frontier1, explored1, frontier2):
    if len(frontier1) == 0:
        return False
    parent = frontier1.pop()
    if Moves(parent).is_correct():
        return True
    explored1.append(parent)
    for i in range(6):
        child = Moves(copy.deepcopy(parent)).turns(i * 2)
        for exp in explored1:
            if Moves(child).is_same(exp):
                continue
        for fro in frontier1:
            if Moves(child).is_same(fro):
                continue
        frontier1.append(copy.deepcopy(child))
        result = dls(frontier1, explored1 ,frontier2)
        if result:
            print("found")


def bidirectional(cube):
    cube2 = get_correct_cube()
    forward1 = [cube]
    forward2 = [cube2]
    explored1 = []
    explored2 = []
    while True:
        if bfs(forward1, explored1, forward2):
            break
        if bfs(forward2, explored2, forward1):
            break


def main():
    cube = get_input()
    print("start")
    ids(cube, 6, 8)
    #bidirectional(cube)
    print("end")


main()
