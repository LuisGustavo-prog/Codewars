def update_light(current):
    traffic_lights = ['green', 'yellow', 'red']

    if current.lower() == 'green':
        return traffic_lights[1]
    elif current.lowe() == 'yellow':
        return traffic_lights[2]
    else:
        return traffic_lights[0]