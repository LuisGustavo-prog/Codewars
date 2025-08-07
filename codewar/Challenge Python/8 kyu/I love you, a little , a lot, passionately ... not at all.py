def how_much_i_love_you(nb_petals):
    array = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    choice = ''

    for number in range(1, nb_petals + 1):
        choice = array[(nb_petals - 1) % len(array)] # o % faz com que a lista possa ser repetida várias vezes.
    
    return choice
                

        

    