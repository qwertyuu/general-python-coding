import itertools
from embarrassing import embarrassing

# Définir les valeurs possibles et le nombre d'éléments
values = [0, 1, 2]
num_elements = 6

# Générer toutes les combinaisons possibles
combinations = list(itertools.product(values, repeat=num_elements))
combinations2 = list(itertools.product(combinations, repeat=2))


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
    }

def parallel_compute(combination2):
    computed = compute_combination(combination2)
    diff = diff_combinations(computed, target_combination)
    return combination2, diff

def diff_combinations(combination1, combination2):
    return sum([abs(combination1[x] - combination2[x]) for x in combination1.keys()])


print(len(combinations2))
target_combination = {
    0: 1/16,
    1: 1/4,
    2: 3/8,
    3: 1/4,
    4: 1/16,
}
count = 0

l = embarrassing(combinations2, parallel_compute, 36)

lowest_diff = 100
lowest_combination = None
for combination in l:
    if combination[1] < lowest_diff:
        lowest_diff = combination[1]
        lowest_combination = combination[0]

print("Lowest combination: ")
print(lowest_combination)
print(lowest_diff)