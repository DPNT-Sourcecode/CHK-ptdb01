

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Input string is not defined. ignore characters that aren't A, B, C or D.
    """

    order = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }
    
    for character in skus:
        if character in order:
            order[character] += 1
    
    total = 130*(order['A']//3) + 50*(order['A'] % 3) + 45*(order['B']//2) + 30*(order['B'] % 2) + 20*order['C'] + 15*order['D']
    
    return total
