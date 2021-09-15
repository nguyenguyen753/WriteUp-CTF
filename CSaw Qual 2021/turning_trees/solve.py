import pathlib

import numpy as np

from .defs import Tiles
from .map import Map
from z3 import Bool, And, Or, Solver, Not


def is_rock(m, x, y):
    return np.asscalar(m.dat[y][x] == Tiles.LAND_ROCK)


def make_cell(top_inputs, left_inputs):
    v1 = And(left_inputs[0], left_inputs[3])
    v2 = And(left_inputs[1], left_inputs[5])
    v3 = And(left_inputs[2], left_inputs[4])
    v4 = And(left_inputs[0], left_inputs[4])
    v5 = And(left_inputs[1], left_inputs[3])
    v6 = And(left_inputs[2], left_inputs[5])
    v7 = And(left_inputs[0], left_inputs[5])
    v8 = And(left_inputs[1], left_inputs[4])
    v9 = And(left_inputs[2], left_inputs[3])

    v10 = Or(v1, v2, v3)
    v11 = Or(v4, v5, v6)
    v12 = Or(v7, v8, v9)

    v13 = And(top_inputs[0], v10)
    v14 = And(top_inputs[1], v12)
    v15 = And(top_inputs[0], v11)
    v16 = And(top_inputs[1], v10)
    v17 = And(top_inputs[0], v12)
    v18 = And(top_inputs[1], v11)

    v19 = Or(v13, v14)
    v20 = Or(v15, v16)
    v21 = Or(v17, v18)

    v22 = And(left_inputs[1], left_inputs[4])
    v23 = And(left_inputs[0], left_inputs[3])
    v24 = And(left_inputs[0], left_inputs[4])
    v25 = And(left_inputs[1], left_inputs[3])
    v26 = And(left_inputs[1], left_inputs[5])
    v27 = And(left_inputs[2], left_inputs[4])
    v28 = And(left_inputs[2], left_inputs[5])
    v29 = And(left_inputs[1], left_inputs[4])

    v30 = Or(left_inputs[0], left_inputs[3], v22)
    v31 = Or(v23, v24, v25)
    v32 = Or(v26, v27, v28)
    v33 = Or(left_inputs[2], left_inputs[5], v29)

    v34 = And(top_inputs[0], v30)
    v35 = And(top_inputs[1], v31)
    v36 = And(top_inputs[0], v32)
    v37 = And(top_inputs[1], v33)

    v38 = Or(v34, v35)
    v39 = Or(v36, v37)

    v40 = And(top_inputs[3], v19)
    v41 = And(top_inputs[2], left_inputs[0])
    v42 = And(top_inputs[3], v20)
    v43 = And(top_inputs[2], left_inputs[1])
    v44 = And(top_inputs[3], v21)
    v45 = And(top_inputs[2], left_inputs[2])

    v46 = Or(v40, v41)
    v47 = Or(v42, v43)
    v48 = Or(v44, v45)

    return [v38, v39, top_inputs[2], top_inputs[3]], [v46, v47, v48, left_inputs[3], left_inputs[4], left_inputs[5]]


def generate_cells(m: Map):
    clauses = []

    # Calculate grid dimensions
    pair_count_x = m.width // 270  # number of cell pairs per full row
    cell_count_y = (m.height - 100) // 141

    print(f"{pair_count_x}x{cell_count_y}")

    # Make top variables for cells
    top_variables = []
    for i in range(pair_count_x):
        name_stub = f"top_vars_pair{i}:"

        v1 = is_rock(m, (i * 270) + 84, 5)
        v2 = is_rock(m, (i * 270) + 91, 5)
        assert v1 or v2
        assert not (v1 and v2)

        v5 = is_rock(m, (i * 270) + 218, 5)  # Bool(name_stub + "cell_2_fixed_1")
        v6 = is_rock(m, (i * 270) + 225, 5)  # Bool(name_stub + "cell_2_fixed_2")
        assert v5 or v6
        assert not (v5 and v6)

        a = Bool(name_stub + "1")
        b = Bool(name_stub + "2")
        c = Bool(name_stub + "3")

        clauses.append(Or(And(a, Not(b), Not(c)),
                          And(b, Not(a), Not(c)),
                          And(c, Not(b), Not(a)),
                          And(Not(c), Not(b), Not(a))))  # Only one can be selected

        v3 = a
        v4 = Or(b, c)
        v7 = Or(a, b)
        v8 = c

        top_variables.append([v1, v2, v3, v4, v5, v6, v7, v8])

    # Make side variables for cells
    side_variables = []
    for i in range(cell_count_y):
        v1 = is_rock(m, 6, (i * 141) + 73)
        v2 = is_rock(m, 6, (i * 141) + 80)
        v3 = is_rock(m, 6, (i * 141) + 87)
        assert v1 or v2 or v3
        assert not (v1 and v2 and v3)

        v4 = is_rock(m, 6, (i * 141) + 101)
        v5 = is_rock(m, 6, (i * 141) + 108)
        v6 = is_rock(m, 6, (i * 141) + 115)
        assert v4 or v5 or v6
        assert not (v4 and v5 and v6)

        side_variables.append([v1, v2, v3, v4, v5, v6])

    # Make cells
    last_row_pair_rhs = {}
    for y in range(cell_count_y):
        row_side_variables = side_variables[y]
        row_pair_count = min(y + 1, pair_count_x)
        print()
        for x in range(row_pair_count):
            print(x, end=", ")
            cell_bottom_1, cell_right_1 = make_cell(top_variables[x][0:4], row_side_variables)
            cell_bottom_2, cell_right_2 = make_cell(top_variables[x][4:8], cell_right_1)

            top_variables[x] = [*cell_bottom_1, *cell_bottom_2]
            assert len(top_variables[x]) == 8

            brought_down = last_row_pair_rhs[x] if x < row_pair_count - 1 else (False, False, False)
            row_side_variables = [*cell_right_2[:3], *brought_down]
            assert len(row_side_variables) == 6

            last_row_pair_rhs[x] = cell_right_2[3:6]

        # Target outputs
        if is_rock(m, 13302, (y * 141) + 73):
            clauses.append(row_side_variables[0])
        elif is_rock(m, 13302, (y * 141) + 80):
            clauses.append(row_side_variables[1])
        elif is_rock(m, 13302, (y * 141) + 87):
            clauses.append(row_side_variables[2])
        else:
            assert False  # No target variable

    return clauses


def main():
    s = Solver()
    for clause in generate_cells(Map.load(str(pathlib.Path(__file__).parent / 'levels/level2.npy'), 2, 2)):
        s.add(clause)

    print(s.check())
    m = s.model()
    print(m)
    vs = {}
    for c in m.decls():
        print(c.name())
        print(bool(m[c]))
        vs[c.name()] = bool(m[c])

    print(vs)

    print('Congrats! Here is your flag:')
    z = 0
    for i in range(48, -1, -1):
        a = vs[f"top_vars_pair{i}:1"]
        b = vs[f"top_vars_pair{i}:2"]
        c = vs[f"top_vars_pair{i}:3"]

        print(f"a: {a}, b: {b}, c: {c}")

        d = 0
        if b:
            d = 1
        elif c:
            d = 2

        z = (z * 3) + d  # len(m.em.at((270*i)+129,8)) + len(m.em.at((270*i)+133,8))
    f = ''
    while z > 0:
        f = chr(z & 0x7f) + f
        z >>= 7
    print('flag{%s}' % f)


if __name__ == '__main__':
    main()