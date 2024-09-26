

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Input string isn't defined, so I can only work with the given examples. Run the following checks:
    - Check input parameter is a string.
    - Check there are no characters besides A, B, C or D in the string.
    """
    
    if (type(skus) == str) and all([character in ['A','B','C','D','E','F'] for character in skus]):
        items = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0
        }
        
        for character in skus:
            if character in items:
                items[character] += 1
        
        costs = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0
        }
        
        B_to_buy = max([items['B'] - (items['E']//2), 0])
        costs['A'] = 200*(items['A']//5) + 130*((items['A'] % 5)//3) + 50*((items['A'] % 5) % 3)
        costs['B'] = 45*(B_to_buy//2) + 30*(B_to_buy % 2)
        costs['C'] = 20*items['C']
        costs['D'] = 15*items['D']
        costs['E'] = 40*items['E']
        costs['F'] = 20*(items['F']//3) + 10*(items['F'] % 3)
        
        total = sum(list(costs.values()))
        
        return int(total)
    
    else:
        
        return -1