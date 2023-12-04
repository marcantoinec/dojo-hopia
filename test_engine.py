from engine import add_random_number, compute_new_grid


def test_add_random_number():
    grille = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    grille = add_random_number(grille)
    somme = sum(sum(row) for row in grille)
    assert somme == 2 or somme == 4


def test_no_move():
    grille = [[2, 0, 0, 0],
              [2, 0, 0, 0],
              [2, 0, 0, 0],
              [2, 0, 0, 0]]
    new_grille = compute_new_grid(grille, "left")
    assert new_grille == grille


def test_move_right():
    grille = [[2, 0, 0, 0],
              [2, 0, 0, 0],
              [2, 0, 0, 0],
              [2, 0, 0, 0]]
    new_grille = compute_new_grid(grille, "right")
    assert new_grille == [[0, 0, 0, 2],
                          [0, 0, 0, 2],
                          [0, 0, 0, 2],
                          [0, 0, 0, 2]]


def test_move_right2():
    grille = [[0, 4, 2, 0],
              [0, 4, 2, 0],
              [0, 0, 0, 0],
              [2, 4, 2, 4]]
    new_grille = compute_new_grid(grille, "right")
    assert new_grille == [[0, 0, 4, 2],
                          [0, 0, 4, 2],
                          [0, 0, 0, 0],
                          [2, 4, 2, 4]]


def test_move_left():
    grille = [[0, 0, 0, 4],
              [0, 0, 0, 4],
              [0, 0, 0, 4],
              [0, 0, 0, 4]]
    new_grille = compute_new_grid(grille, "left")
    assert new_grille == [[4, 0, 0, 0],
                          [4, 0, 0, 0],
                          [4, 0, 0, 0],
                          [4, 0, 0, 0]]


def test_move_left2():
    grille = [[0, 4, 2, 0],
              [0, 4, 2, 0],
              [0, 0, 0, 0],
              [2, 4, 2, 4]]
    new_grille = compute_new_grid(grille, "left")
    assert new_grille == [[4, 2, 0, 0],
                          [4, 2, 0, 0],
                          [0, 0, 0, 0],
                          [2, 4, 2, 4]]


def test_move_up():
    grille = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 4],
              [2, 2, 8, 0]]
    new_grille = compute_new_grid(grille, "up")
    assert new_grille == [[2, 2, 8, 4],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
