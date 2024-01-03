lowest_combination = ((0, 0, 1, 1, 1, 2), (0, 1, 1, 1, 2, 2))

def compute_combination(combination2):
    val_dict = {0:0, 1:0, 2:0, 3:0, 4:0}
    combinations_sum = [x + y for x in combination2[0] for y in combination2[1]]
    for element in combinations_sum:
        val_dict[element] += 1
    return {
        0: val_dict[0] / 36,
        1: val_dict[1] / 36,
        2: val_dict[2] / 36,
        3: val_dict[3] / 36,
        4: val_dict[4] / 36,
    }, val_dict


def diff_combinations(combination1, combination2):
    return sum([abs(combination1[x] - combination2[x]) for x in combination1.keys()])


target_combination = {
    0: 1/16,
    1: 1/4,
    2: 3/8,
    3: 1/4,
    4: 1/16,
}
computed = compute_combination(lowest_combination)
print(computed)
