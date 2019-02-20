lookup_table_keys = [(0, 12), (13, 37), (38, 62), (63, 87), (88, 112), 
    (113, 137), (138, 162), (163, 187), (188, 212), (213, 237), (238, 9999)]

lookup_table = {
    'upset': {
        lookup_table_keys[0]: 8,
        lookup_table_keys[1]: 10,
        lookup_table_keys[2]: 13,
        lookup_table_keys[3]: 16,
        lookup_table_keys[4]: 20,
        lookup_table_keys[5]: 25,
        lookup_table_keys[6]: 30,
        lookup_table_keys[7]: 35,
        lookup_table_keys[8]: 40,
        lookup_table_keys[9]: 45,
        lookup_table_keys[10]: 50
    },
    'expected_result': {
        lookup_table_keys[0]: 8,
        lookup_table_keys[1]: 7,
        lookup_table_keys[2]: 6,
        lookup_table_keys[3]: 5,
        lookup_table_keys[4]: 4,
        lookup_table_keys[5]: 3,
        lookup_table_keys[6]: 2,
        lookup_table_keys[7]: 2,
        lookup_table_keys[8]: 1,
        lookup_table_keys[9]: 1,
        lookup_table_keys[10]: 0
    }
}

def get_adjustment(winner_rating, loser_rating):
    key = 'upset' if winner_rating < loser_rating else 'expected_result'
    score_differential = abs(winner_rating - loser_rating)
    for k, v in lookup_table[key].items():
        if score_differential in range(k[0], k[1] + 1):
            return v
