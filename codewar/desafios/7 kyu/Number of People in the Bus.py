def number(bus_stops):
    result = 0

    for x in bus_stops:
        result += x[0]

    for i in bus_stops:
        result -= i[1]

    return result


print(number([[10,0],[3,5],[5,8]]))