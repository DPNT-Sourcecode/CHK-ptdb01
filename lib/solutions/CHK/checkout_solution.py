

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
        
        non_offer_coeffs = {'C': 20, 'D': 15, 'E': 40, 'G': 20, 'I': 35, 'J': 60, 'L': 90, 'N': 15, 'O': 10, 'R': 50, 'S': 30, 'T': 20, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50}
        for non_offer_char in 'CDGIJLMOSTWXYZ':
            costs[non_offer_char] = non_offer_coeffs[non_offer_char]*items[non_offer_char]
        
        costs['A'] = 200*(items['A']//5) + 130*((items['A'] % 5)//3) + 50*((items['A'] % 5) % 3)
        B_to_buy = max([items['B'] - (items['E']//2), 0])
        costs['B'] = 45*(B_to_buy//2) + 30*(B_to_buy % 2)
        costs['F'] = 20*(items['F']//3) + 10*(items['F'] % 3)
        costs['H'] = 80*(items['H']//10) + 45*((items['H'] % 10)//5) + 10*((items['H'] % 10) % 5)
        costs['K'] = 150*(items['K']//2) + 80*(items['K'] % 2)
        costs['M'] = 20*max([items['M'] - (items['N']//3), 0])
        costs['P'] = 200*(items['P']//5) + 50*(items['P'] % 5)
        Q_to_buy = max([items['Q'] - (items['R']//3), 0])
        costs['Q'] = 80*(Q_to_buy//3) + 30*(Q_to_buy % 3)
        costs['U'] = 80*(items['U']//3) + 40*(items['U'] % 3)
        costs['V'] = 130*(items['V']//3) + 90*((items['V'] % 3)//2) + 50*((items['V'] % 3) % 2)
        
        total = sum(list(costs.values()))
        
        return int(total)
    
    else:
        
        return -1