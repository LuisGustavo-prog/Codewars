def points(games):
    point = 0

    for game in games:
        x, y = games.split(':')
        x = int(x)
        y = int(y)

        if x > y:
            point += 3
        elif x < y:
            point += 0
        else:
            point += 1
    
    
    return point

