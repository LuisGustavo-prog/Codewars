def invert(lst):
    new_lst = [] # lista onde eu vou colocar os novos números.
    number = 0 # essa variável precisa receber um valor antes que eu possa usar ela.

    for x in lst:
        number = x * -1 # Pode ser usado para trocar se o número é positivo ou negativo.
        new_lst.append(number) # colocando os novos números dentro de uma nova lista.
    
    return new_lst # retornando a lista.