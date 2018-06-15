map = {
    "size_x":7,
    "size_y":7
}

player = {
    "x": 3,
    "y": 2
}

boxes = [
    { "x": 1, "y":1},
    { "x": 2, "y":2},
    { "x": 3, "y":3}
]

destination = [
    { "x": 2, "y":1},
    { "x": 3, "y":2},
    { "x": 4, "y":3}
]

walls = [
    { "x": 4, "y":1},
    { "x": 2, "y":1},
    { "x": 3, "y":1}

]


while True:
    for y in range(map['size_y']):
        for x in range(map['size_x']):
            player_is_here= False
            box_is_here = False
            wall_is_here= False
            dest_is_here = False
            for wall in walls:
                if wall['x'] == x and wall['y'] == y:
                    wall_is_here = True

            for dest in destination:
                if dest['x'] == x and dest['y'] == y:
                    dest_is_here= True

            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    box_is_here = True

            if x == player['x'] and y == player['y']:
                   player_is_here= True


            if player_is_here is True:
                print("P ", end="")
            elif box_is_here is True:
                print("B ", end="")
            elif dest_is_here is True:
                print("D ", end="")
            elif wall_is_here is True:
                print("W ", end="")
            else:
                print("- ", end="")
        print()

    win = True
    for box in boxes:
        if box not in destination:
            win = False

    if win:
        print("you win")
        break

    move= input("Your move: ").upper()

    dx = 0
    dy = 0

    if move =="W":
       dy = -1
    elif move =="S":
         dy = 1
    elif move=="A":
         dx = -1
    elif move=="D":
         dx = 1
    else:
        print("Clgt ???")
        break

    if  0 <= player['x'] + dx < map['size_x'] \
        and 0 <= player['y'] + dy <=         map['size_y']:

        player['x'] +=dx
        player['y'] += dy

    for box in boxes:
        if player['x'] == box['x'] and \
            player['y'] == box['y']:
            box['x'] +=dx
            box['y'] +=dy

    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            player["x"] -= dx
            player["y"] -= dy

    for wall in walls:
        for box in boxes:
            if box['x'] == wall["x"] and box['y'] == wall["y"]:
                box['x'] -= dx
                box['y'] -= dy
                player["x"] -= dx
                player["y"] -= dy


            #break

