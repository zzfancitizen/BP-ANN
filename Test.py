import pandas as pd

input_value   = []
training_sets = []
expect_value  = []
training_set  = []

data = pd.read_csv("poker-hand-training-true.csv")
rows = data.count()

for i in range(0, rows[0]):
    for j in range(0,10):
        input_value.append(data.values[i][j])
    expect_value.append(data.values[i][10])
    training_set.append(input_value)
    training_set.append(expect_value)
    training_sets.append(training_set)
    input_value = []
    expect_value = []
    training_set = []

print(training_sets)