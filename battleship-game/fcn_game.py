import random

# AI attacks function.
# Randomly selects a cell to attack.
# Weights influence the pick. Weight values should be:
# - 0 for cells that have already been hit.
# - 1 for cells that have no priority.
# - 99 for cells that have priority.
# - 1000 for cells that are near a hit ship.
def ai_attack(field, ships):
    test_hit = False
    while test_hit is False:
        cells = [
        ((r, c), cell)
        for r, row in enumerate(field)
        for c, cell in enumerate(row)
        ]

        positions = [pos for pos, cell in cells]
        weights = [cell.ai_weight for pos, cell in cells]

        print(positions)
        print(weights)

        pos = random.choices(positions, weights=weights, k=1)[0]
        x = pos[0]
        y = pos[1]
        
        if field[x][y].is_hit is False:
            field[x][y].is_hit = True
            field[x][y].ai_weight = 0
            test_hit = True
    
    hit_value = True

    print(f"AI attacks position: {pos}")
    if field[x][y].ship > 0:
        if field[x][y].ship == 1:
            print("AI hit your Battleship!")
            ships[0] -= 1
            if ships[0] == 0:
                print("Your Battleship has been sunk!")
                hit_value = False
        elif field[x][y].ship == 2:
            print("AI hit your Cruiser!")
            ships[1] -= 1
            if ships[1] == 0:
                print("Your Cruiser has been sunk!")
                hit_value = False
        elif field[x][y].ship == 3:
            print("AI hit your Submarine!")
            ships[2] -= 1
            if ships[2] == 0:
                print("Your Submarine has been sunk!")
                hit_value = False
        elif field[x][y].ship == 4:
            print("AI hit your Destroyer!")
            ships[3] -= 1
            if ships[3] == 0:
                print("Your Destroyer has been sunk!")
                hit_value = False
    elif field[x][y].ship == 0:
        print("AI missed!")
        hit_value = False


        