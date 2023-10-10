import csv
with open("insurance.csv", newline = '') as insurance_file:
    reader = csv.DictReader(insurance_file)
    ages_smokers_costs = []
    for row in reader:
        new_row = {
            "age": row['age'],
            "smoker": row["smoker"],
            "charges": row["charges"]
        }
        ages_smokers_costs.append(new_row)


def calculate_smoker_cost(dataset):
    total_cost = 0
    total_smokers = 0
    for row in dataset:
        if(row['smoker'] == 'yes'):
            total_cost += float(row['charges'])
            total_smokers += 1 

    return round(total_cost/total_smokers, 2)


def calculate_non_smoker_cost(dataset):
    total_cost = 0
    total_non_smokers = 0
    for row in dataset:
        if(row['smoker'] == 'no'):
            total_cost += float(row['charges'])
            total_non_smokers += 1 

    return round(total_cost/total_non_smokers, 2)


smoker_cost = calculate_smoker_cost(ages_smokers_costs)
non_smoker_cost = calculate_non_smoker_cost(ages_smokers_costs)

print("The average cost for a smoker is: ${}".format(smoker_cost))
print("The average cost for a non-smoker is: ${}".format(non_smoker_cost))
