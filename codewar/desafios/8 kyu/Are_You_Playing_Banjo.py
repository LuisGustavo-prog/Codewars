def are_you_playing_banjo(name):
    for i in name[0].lower():
        if i == 'r':
            return name + ' plays banjo'
        else:
            return name + ' does not play banjo'

# print(are_you_playing_banjo('Raissa'))