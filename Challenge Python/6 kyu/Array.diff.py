def array_diff(a, b):
    return [x for x in a if x not in b] # Estou criando uma nova lista e colocando um filtro nela para que entre apenas os itens desejados, eu poderia colocar em uma variável, mas no caso não é preciso.


print(array_diff([1, 2, 3], [1, 2]))