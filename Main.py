import copy


class Cube:
    def __init__(self, surfaces):
        self.surfaces = surfaces


class Node:
    def __init__(self, cube, depth):
        self.cube = cube
        self.depth = depth
        self.cost = depth


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
        # counter clockwise
        self.cube.surfaces[0].blocks[0] = copy.deepcopy(temp.surfaces[0].blocks[1])
        self.cube.surfaces[0].blocks[1] = copy.deepcopy(temp.surfaces[0].blocks[3])
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[0].blocks[0])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[0].blocks[2])

        # clockwise
        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[4].blocks[2])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[4].blocks[0])
        self.cube.surfaces[4].blocks[2] = copy.deepcopy(temp.surfaces[4].blocks[3])
        self.cube.surfaces[4].blocks[3] = copy.deepcopy(temp.surfaces[4].blocks[1])

    def turn_left(self):
        temp = copy.deepcopy(self.cube)

        # change surfaces
        self.cube.surfaces[2] = copy.deepcopy(temp.surfaces[3])
        self.cube.surfaces[1] = copy.deepcopy(temp.surfaces[2])
        self.cube.surfaces[5] = copy.deepcopy(temp.surfaces[1])
        self.cube.surfaces[3] = copy.deepcopy(temp.surfaces[5])

        # rotate surfaces
        # clockwise
        self.cube.surfaces[0].blocks[0] = copy.deepcopy(temp.surfaces[0].blocks[2])
        self.cube.surfaces[0].blocks[1] = copy.deepcopy(temp.surfaces[0].blocks[0])
        self.cube.surfaces[0].blocks[2] = copy.deepcopy(temp.surfaces[0].blocks[3])
        self.cube.surfaces[0].blocks[3] = copy.deepcopy(temp.surfaces[0].blocks[1])

        # counter clockwise
        self.cube.surfaces[4].blocks[0] = copy.deepcopy(temp.surfaces[4].blocks[1])
        self.cube.surfaces[4].blocks[1] = copy.deepcopy(temp.surfaces[4].blocks[3])
        self.cube.surfaces[4].blocks[2] = copy.deepcopy(temp.surfaces[4].blocks[0])
        self.cube.surfaces[4].blocks[3] = copy.deepcopy(temp.surfaces[4].blocks[2])

    def turn_up(self):
        temp = copy.deepcopy(self.cube)

        # change surfaces
        self.cube.surfaces[0] = copy.deepcopy(temp.surfaces[2])
        self.cube.surfaces[2] = copy.deepcopy(temp.surfaces[4])

        # rotate surfaces
        # counter clockwise
        self.cube.surfaces[1].blocks[0] = copy.deepcopy(temp.surfaces[1].blocks[1])
        self.cube.surfaces[1].blocks[1] = copy.deepcopy(temp.surfaces[1].blocks[3])
        self.cube.surfaces[1].blocks[2] = copy.deepcopy(temp.surfaces[1].blocks[0])
        self.cube.surfaces[1].blocks[3] = copy.deepcopy(temp.surfaces[1].blocks[2])

        # clockwise
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
        # clockwise
        self.cube.surfaces[1].blocks[0] = copy.deepcopy(temp.surfaces[1].blocks[2])
        self.cube.surfaces[1].blocks[1] = copy.deepcopy(temp.surfaces[1].blocks[0])
        self.cube.surfaces[1].blocks[2] = copy.deepcopy(temp.surfaces[1].blocks[3])
        self.cube.surfaces[1].blocks[3] = copy.deepcopy(temp.surfaces[1].blocks[1])

        # counter clockwise
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
        if turn_number == 2:
            Moves.rotate_clockwise(self)
            return self.cube

        # if turn_number == 8:
        #     Moves.rotate_counter_clockwise(self)
        #     return self.cube

        if turn_number == 1:
            Moves.turn_right(self)
            Moves.rotate_clockwise(self)
            Moves.turn_left(self)
            return self.cube

        # if turn_number == 7:
        #     Moves.turn_right(self)
        #     Moves.rotate_counter_clockwise(self)
        #     Moves.turn_left(self)
        #     return self.cube

        if turn_number == 3:
            Moves.turn_left(self)
            Moves.rotate_clockwise(self)
            Moves.turn_right(self)
            return self.cube

        # if turn_number == 9:
        #     Moves.turn_left(self)
        #     Moves.rotate_counter_clockwise(self)
        #     Moves.turn_right(self)
        #     return self.cube

        if turn_number == 4:
            Moves.turn_up(self)
            Moves.rotate_clockwise(self)
            Moves.turn_down(self)
            return self.cube

        # if turn_number == 10:
        #     Moves.turn_up(self)
        #     Moves.rotate_counter_clockwise(self)
        #     Moves.turn_down(self)
        #     return self.cube

        if turn_number == 0:
            Moves.turn_down(self)
            Moves.rotate_clockwise(self)
            Moves.turn_up(self)
            return self.cube

        # if turn_number == 6:
        #     Moves.turn_down(self)
        #     Moves.rotate_counter_clockwise(self)
        #     Moves.turn_up(self)
        #     return self.cube

        if turn_number == 5:
            Moves.turn_right(self)
            Moves.turn_right(self)
            Moves.rotate_clockwise(self)
            Moves.turn_left(self)
            Moves.turn_left(self)
            return self.cube

        # if turn_number == 11:
        #     Moves.turn_right(self)
        #     Moves.turn_right(self)
        #     Moves.rotate_counter_clockwise(self)
        #     Moves.turn_left(self)
        #     Moves.turn_left(self)
        #     return self.cube

    @staticmethod
    def is_correct(cube):
        for i in cube.surfaces:
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
            blocks = [Block(str(i)), Block(str(i)), Block(str(i)), Block(str(i))]
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


def dls(limit, cube, path, generated_nodes, explored_nodes, number_of_nodes, max_number_of_nodes):
    if limit == 0:
        number_of_nodes -= 1
        return [False, cube, path, generated_nodes, explored_nodes, number_of_nodes, max_number_of_nodes]
    if Moves.is_correct(cube):
        number_of_nodes -= 1
        return [True, cube, path, generated_nodes, explored_nodes, number_of_nodes, max_number_of_nodes]
    for i in range(6):
        child = Moves(copy.deepcopy(cube)).turns(i)
        number_of_nodes += 1
        if number_of_nodes > max_number_of_nodes:
            max_number_of_nodes = number_of_nodes
        generated_nodes += 1
        path.append(i + 1)
        result = dls(limit - 1, child, path, generated_nodes, explored_nodes, number_of_nodes, max_number_of_nodes)
        generated_nodes = result[3]
        explored_nodes = result[4]
        if result[0]:
            return result
        path.pop()
    explored_nodes += 1
    number_of_nodes -= 1
    return [False, cube, path, generated_nodes, explored_nodes, number_of_nodes, max_number_of_nodes]


def ids(cube, min_depth, max_depth):
    for i in range(min_depth, max_depth):
        path = []
        generated_nodes = 0
        explored_nodes = 0
        number_of_nodes = 0
        max_number_of_nodes = 0
        result = dls(i, cube, path, generated_nodes, explored_nodes, number_of_nodes, max_number_of_nodes)
        if result[0]:
            print()
            print("############")
            print("ids ")
            print("moves : ")
            print("*clockwise")
            for j in range(len(result[2])):
                print("surface number : " + str(result[2][j]))
            print()
            print("generated nodes : " + str(result[3]))
            print("explored nodes : " + str(result[4]))
            print("result depth : " + str(len(result[2])))
            print("max number of nodes in memory : " + str(result[6]))
            break


def bfs(my_frontier, other_frontier, frontier_path, other_frontier_path, information):
    for i, my in enumerate(my_frontier):
        for j, other in enumerate(other_frontier):
            if Moves.is_same(my, other):
                return [True, my_frontier, other_frontier, frontier_path, other_frontier_path, i, j, information]

    parents = []
    parent_path = []
    for i in range(len(my_frontier)):
        parents.append(my_frontier.pop())
        parent_path.append(frontier_path.pop())

    information[1] += len(parents)

    for i in range(len(parents)):
        for j in range(6):
            child = Moves(copy.deepcopy(parents[i])).turns(j)
            information[0] += 1
            my_frontier.append(copy.deepcopy(child))
            this_parent_path = copy.deepcopy(parent_path[i])
            this_parent_path.append(j + 1)
            frontier_path.append(this_parent_path)

    information[2] = information[0] - information[1]
    return [False, my_frontier, other_frontier, frontier_path, other_frontier_path, -1, -1, information]


def bidirectional(cube1, depth):
    cube2 = Moves.get_correct_cube()
    frontier1 = [copy.deepcopy(cube1)]
    frontier2 = [copy.deepcopy(cube2)]
    frontier1_path = [[0]]
    frontier2_path = [[0]]
    information = [2, 0, 0]  # generated node # explored node # max node in memory
    result = [False, frontier1, frontier2, frontier1_path, frontier2_path, -1, -1, information]
    while depth != 0:
        # from start to goal
        res = copy.deepcopy(result)
        result = bfs(res[1], res[2], res[3], res[4], res[7])
        if result[0]:
            path1 = result[3][result[5]]
            path2 = result[4][result[6]]
            print()
            print("############")
            print("bidirectional ")
            print("moves : ")
            print("*clockwise")
            for idx in range(1, len(path1)):
                print("surface number : " + str(path1[idx]))
            print("*counterclockwise")
            for idx in reversed(range(1, len(path2))):
                print("surface number : " + str(path2[idx]))
            print()
            print("generated nodes : " + str(result[7][0]))
            print("explored nodes : " + str(result[7][1]))
            print("result depth : " + str(len(path1) + len(path2) - 2))
            print("max number of nodes in memory : " + str(result[7][2]))
            break
        # from goal to start
        res = copy.deepcopy(result)
        result = bfs(res[2], res[1], res[4], res[3], res[7])
        if result[0]:
            path1 = result[3][result[5]]
            path2 = result[4][result[6]]
            print()
            print("############")
            print("bidirectional ")
            print("moves : ")
            print("*clockwise")
            for idx in range(1, len(path2)):
                print("surface number : " + str(path2[idx]))
            print("*counterclockwise")
            for idx in reversed(range(1, len(path1))):
                print("surface number : " + str(path1[idx]))
            print()
            print("generated nodes : " + str(result[7][0]))
            print("explored nodes : " + str(result[7][1]))
            print("result depth : " + str(len(path1) + len(path2) - 2))
            print("max number of nodes in memory : " + str(result[7][2]))
            break
        depth -= 1


def ucs_search(frontier, depth, frontier_path, information, explored):
    while len(frontier) != 0:
        min_cost = 1000
        min_cost_node = None
        for fro in frontier:
            if fro.cost < min_cost:
                min_cost = fro.cost
                min_cost_node = fro

        idx = frontier.index(min_cost_node)
        node = frontier.pop(idx)
        parent_path = frontier_path.pop(idx)

        information[1] += 1
        explored.append(node)

        if Moves.is_correct(node.cube):
            return [True, parent_path, information]
        if node.depth == depth:
            continue

        for i in range(6):
            child = Moves(copy.deepcopy(node.cube)).turns(i)
            child_node = Node(copy.deepcopy(child), node.depth + 1)
            founded = False
            for val in frontier:
                if Moves.is_same(val.cube, child):
                    founded = True
                    break
            for val in explored:
                if Moves.is_same(val.cube, child):
                    founded = True
                    break
            if founded:
                continue
            information[0] += 1
            par_path = copy.deepcopy(parent_path)
            par_path.append(i + 1)
            frontier_path.append(copy.deepcopy(par_path))
            frontier.append(copy.deepcopy(child_node))

        information[2] = information[0] - information[1]
    return [False, parent_path, information]


def ucs(cube, depth):
    root = Node(cube, 0)
    frontier = [root]
    explored = []
    frontier_path = [[0]]
    information = [1, 0, 0]  # generated node # explored node # max node in memory

    result = ucs_search(frontier, depth, frontier_path, information, explored)
    if result[0]:
        print()
        print("############")
        print("ucs ")
        print("moves : ")
        print("*clockwise")
        for idx in range(1, len(result[1])):
            print("surface number : " + str(result[1][idx]))
        print()
        print("generated nodes : " + str(result[2][0]))
        print("explored nodes : " + str(result[2][1]))
        print("result depth : " + str(len(result[1]) - 1))
        print("max number of nodes in memory : " + str(result[2][2]))


def main():
    cube = get_input()
    print("start")

    # ids(cube, 4, 5)
    # bidirectional(cube, 5)
    ucs(cube, 4)

    print("end")


main()
