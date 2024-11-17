import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_parquet('train-00000-of-00001-b21313e511aa601a.parquet')

# Drop rows with any missing values
data = data.dropna(ignore_index=True)

# Display the first 5 rows of the data
data.head()

X = data[['title','abstract']]
Y = data['verified_uat_ids']

ids_and_labels = data[['verified_uat_ids','verified_uat_labels']]
print(ids_and_labels)
dict_ids_labels = dict

for i in range(0,len(ids_and_labels['verified_uat_ids'])):
    for j in range(0,len(ids_and_labels['verified_uat_ids'][i])):
        dict_ids_labels[ids_and_labels['verified_uat_ids'][i][j]] = ids_and_labels['verified_uat_labels'][i][j]