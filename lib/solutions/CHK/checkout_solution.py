

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Input string isn't defined, so I can only work with the given examples. Run the following checks:
    - Check input parameter is a string.
    - Check there are no characters besides A, B, C or D in the string.
    """
    
    if (type(skus) == str) and all([character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for character in skus]):

        items = {character: 0 for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        
        for character in skus:
            if character in items:
                items[character] += 1
        
        costs = {character: 0 for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        
        bulk_discount_count = [items[character] for character in 'STXYZ']
        costs['multi'] = 45*(bulk_discount_count//3)
        bulk_discount_included = sum(bulk_discount_count) - (bulk_discount_count % 3)
        for character in 'ZSTYX':
            remaining_characters = min(bulk_discount_included, items[character])
            items[character] -= remaining_characters
            bulk_discount_included -= remaining_characters
        
        non_offer_coeffs = {'C': 20, 'D': 15, 'E': 40, 'G': 20, 'I': 35, 'J': 60, 'L': 90, 'N': 40, 'O': 10, 'R': 50, 'S': 20, 'T': 20, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21}
        for non_offer_char in 'CDEGIJLNORSTWXYZ':
            costs[non_offer_char] = non_offer_coeffs[non_offer_char]*items[non_offer_char]
        
        costs['A'] = 200*(items['A']//5) + 130*((items['A'] % 5)//3) + 50*((items['A'] % 5) % 3)
        B_to_buy = max([items['B'] - (items['E']//2), 0])
        costs['B'] = 45*(B_to_buy//2) + 30*(B_to_buy % 2)
        costs['F'] = 20*(items['F']//3) + 10*(items['F'] % 3)
        costs['H'] = 80*(items['H']//10) + 45*((items['H'] % 10)//5) + 10*((items['H'] % 10) % 5)
        costs['K'] = 120*(items['K']//2) + 70*(items['K'] % 2)
        costs['M'] = 15*max([items['M'] - (items['N']//3), 0])
        costs['P'] = 200*(items['P']//5) + 50*(items['P'] % 5)
        Q_to_buy = max([items['Q'] - (items['R']//3), 0])
        costs['Q'] = 80*(Q_to_buy//3) + 30*(Q_to_buy % 3)
        costs['U'] = 120*(items['U']//4) + 40*(items['U'] % 4)
        costs['V'] = 130*(items['V']//3) + 90*((items['V'] % 3)//2) + 50*((items['V'] % 3) % 2)
        
        bulk_discount_count = [items[character] for character in 'STXYZ']
        costs['multi'] = 45*(bulk_discount_count//3)
        
# | K    | 70    | 2K for 120                      |
        
        total = sum(list(costs.values()))
        
        return int(total)
    
    else:
        
        return -1
