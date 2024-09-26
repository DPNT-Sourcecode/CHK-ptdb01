

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Input string isn't defined, so I can only work with the given examples. Run the following checks:
    - Check input parameter is a string.
    - Check there are no characters besides A, B, C or D in the string.
    """
    
    if (type(skus) == str) and all([character in ['A','B','C','D','E'] for character in skus]):
        order = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0
        }
        
        for character in skus:
            if character in order:
                order[character] += 1
        
        B_to_buy = max([order['B'] - order['E']//2, 0])
        A_cost = 200*(order['A']//5) + 130*((order['A'] % 5)//3) + 50*((order['A'] % 5) % 3)
        B_cost = 45*(B_to_buy//2) + 30*(B_to_buy % 2)
        C_cost = 20*order['C']
        D_cost = 15*order['D']
        E_cost = 40*order['E']
        
        total = A_cost + B_cost + C_cost + D_cost + E_cost
        
        return int(total)
    
    else:
        
        return -1