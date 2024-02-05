grille = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


def add_random_number(grille):
    grille[0][0] = 2
    return grille


def move_right(row):
    for k, _ in enumerate(row):
        current_j = 3 - k
        if row[current_j] == 0:
            continue
        j = current_j
        while j < 3 and row[j + 1] == 0:
            j += 1
        row[j], row[current_j] = row[current_j], row[j]
    return row


def transpose(grille):
    grille_t = []
    for j in range(4):
        grille_t.append([grille[i][j] for i in range(4)])
    return grille_t


def compute_new_grid(grille, direction):
    if direction == "up":
        grille_t = transpose(grille)
        for i, row in enumerate(grille_t):
            grille_t[i] = move_right(row[::-1])[::-1]
        return transpose(grille_t)

    for i, row in enumerate(grille):
        if direction == "right":
            grille[i] = move_right(row)
        elif direction == "left":
            grille[i] = move_right(row[::-1])[::-1]

    return grille
