import math

num_criteria = int(input("Enter the number of criteria you are considering: "))
print()

criteria_list = []

for i in range(num_criteria):
    name = input(f"Enter name of criteria #{i + 1}: ")
    print()

    while True:
        weight = float(input(f"Enter weight for '{name}' (0-1): "))
        if weight != 1:
            break
        else:
            print("Weight must be equal to 1")
    print()  
  
    while True:
        direction = input(f"Should '{name}' be maximized or minimized? (Enter 'max' or 'min'): ").strip().lower()
        if direction in ('max', 'min'):
            break
        else:
            print("Invalid input. Please enter 'max' or 'min'.")
    print()

    criteria_list.append({
        'name': name,
        'weight': weight,
        'direction': direction
    })


print("Criteria you entered:\n")
for c in criteria_list:
  print(f"- {c['name']}: weight={c['weight']}, {c['direction']}")
  print()

print("your weight matrix is:")
print()
weight_matrix = [c['weight'] for c in criteria_list]
print(weight_matrix)

college_names = []
print()
print(f"Enter the names of {num_criteria} colleges you are considering:")
for i in range(num_criteria):
    college = input(f"College #{i + 1}: ")
    college_names.append(college)
    print()

performance_matrix = []

for college in college_names:
    print(f"Enter values for {college}:")
    row = []
    for criterion in criteria_list:
        value = int(input(f"  what is the {criterion['name']} at this college: "))
        row.append(value)
    performance_matrix.append(row)
    print()

print("Performance Matrix:")
for i, college in enumerate(college_names):
    print(f"{college}: {performance_matrix[i]}")

print()
transposed = list(zip(*performance_matrix))
z_score_matrix = []

for j, col in enumerate(transposed):
    mean = sum(col) / len(col)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in col) / len(col))

    if std_dev == 0:
        z_col = [0] * len(col)
    else:
        raw_z_col = [(x - mean) / std_dev for x in col]
        if criteria_list[j]['direction'] == 'min':
            z_col = [-z for z in raw_z_col]
        else:
            z_col = raw_z_col

    z_score_matrix.append(z_col)

z_score_matrix = list(zip(*z_score_matrix))
print("Adjusted Z-score Matrix:")
for i, college in enumerate(college_names):
    z_row = [round(val, 2) for val in z_score_matrix[i]]
    print(f"{college}: {z_row}")

result_matrix = []
for row in z_score_matrix:
    weighted_sum = 0
    for i, val in enumerate(row):
        weighted_sum += val * weight_matrix[i]
    result_matrix.append(weighted_sum)
print()
print("Final weighted scores per college:")
for college, score in zip(college_names, result_matrix):
    print(f"{college}: {round(score, 3)}")
