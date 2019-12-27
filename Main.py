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
    def __init__(self, cube, depth, heuristic):
        self.cube = cube
        self.depth = depth
        self.cost = heuristic + depth


class Surface:
    def __init__(self, blocks):
        self.blocks = blocks


class Block:
    def __init__(self, color_number):
        self.color_number = color_number


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

    @staticmethod
    def is_same(cube1, cube2):
        for i in range(6):
            for j in range(4):
                if cube1.surfaces[i].blocks[j].color_number != cube2.surfaces[i].blocks[j].color_number:
                    return False
        return True

    @staticmethod
    def get_correct_cube():
        surfaces = []
        for i in range(1, 7):
            blocks = [Block(i), Block(i), Block(i), Block(i)]
            surfaces.append(Surface(copy.deepcopy(blocks)))
        return Cube(surfaces)


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


def dls(limit, cube):
    if limit == 0:
        return False
    if Moves(cube).is_correct():
        return True
    for i in range(6):
        child = Moves(copy.deepcopy(cube)).turns(i * 2)
        result = dls(limit - 1, child)
        if result:
            print("found")


def ids(cube, min_depth, max_depth):
    for i in range(min_depth, max_depth):
        result = dls(i, cube)
        if result:
            print("found")


def bfs(my_frontier, other_frontier, is_start):
    if is_start:
        for cube in my_frontier:
            if Moves(cube).is_correct:
                return True

    for my in my_frontier:
        for other in other_frontier:
            if Moves.is_same(my, other):
                return True
    parents = []
    for i in range(len(my_frontier)):
        parents.append(my_frontier.pop())

    for parent in parents:
        for i in range(6):
            child = Moves(copy.deepcopy(parent)).turns(i * 2)
            my_frontier.append(copy.deepcopy(child))
    return False


def bidirectional(cube1, depth):
    cube2 = Moves.get_correct_cube()
    frontier1 = [cube1]
    frontier2 = [cube2]
    while depth != 0:
        # from start to goal
        if bfs(frontier1, frontier2, True):
            print("found1")
        # from goal to start
        if bfs(frontier2, frontier1, False):
            print("found2")
        depth -= 1


def heuristic_finder(cube):
    surface_colors = []
    for surface in cube.surfaces:
        color_numbers = []
        for block in surface.blocks:
            color = block.color_number
            if color not in color_numbers:
                color_numbers.append(color)
        surface_colors.append(len(color_numbers))
    result = 0
    for i in range(6):
        if surface_colors[i] == 2:
            result += 1
        if surface_colors[i] == 3:
            result += 2
        if surface_colors[i] == 4:
            result += 4
    return result


def a_star(frontier, depth):
    min_cost = 1000
    min_cost_cube = None
    node = None
    for fro in frontier:
        if fro.cost < min_cost:
            min_cost_cube = fro
    if len(frontier) != 0:
        node = frontier.remove(min_cost_cube)

    if Moves(node.cube).is_correct():
        return True
    if node.depth == depth:
        return False

    for i in range(6):
        child = Moves(copy.deepcopy(min_cost_cube.cube)).turns(i * 2)
        child_node = Node(child, min_cost_cube.depth + 1, heuristic_finder(child))
        frontier.append(child_node)


def helper(cube, depth):
    heuristic = heuristic_finder(cube)
    root = Node(cube, 0, heuristic)
    frontier = [root]
    while True:
        if a_star(frontier, depth):
            print("found")
            break


def main():
    cube = get_input()
    print("start")

    # ids(cube, 6, 7)
    # bidirectional(cube, 6)
    helper(cube, 5)

    print("end")


main()
