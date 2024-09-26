

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Input string isn't defined, so I can only work with the given examples. Run the following checks:
    - Check input parameter is a string.
    - Check there are no '-' characters.
    - Check there are no lowercase a, b, c, d characters. (It seems the letter x should be skipped)
    """
    
    if (type(skus) == str) and ('-' not in skus) and not any([letter in skus for letter in ['a','b','c','d']]):
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
        
        return int(total)
    
    else:
        
        return -1


