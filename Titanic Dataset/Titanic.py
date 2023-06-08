# Add Titanic Code here

data = {
    'Sex': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [25, 62, 45, 18, 95, 27, 40, 22, 36, 7, 19, 30, 54, 87, 38],
    'Survived': [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
}


df = pd.DataFrame(data)

df.to_csv('Titanic_dummy.csv', index=False)
df = pd.DataFrame(data)

df.to_csv('Titanic_dummy.csv', index=False)

df_read = pd.read_csv('Titanic_dummy.csv')

print(df_read)

df = pd.read_csv('Titanic_dummy.csv')

print(df.columns)

print(df.info())
print(df.describe())

print(df.head())

import numpy as np

df = pd.read_csv('Titanic_dummy.csv')

df_with_missing = df.mask(np.random.random(df.shape) < 0.2)

missing_values = df_with_missing.isna().sum()
print("Missing values:")
print(missing_values)

mean_age = df_with_missing['Age'].mean()
df_filled = df_with_missing.fillna({'Age': mean_age})

missing_values_after_fill = df_filled.isna().sum()
print("\nMissing values after filling:")
print(missing_values_after_fill)

import unittest

class TestTitanicOperations(unittest.TestCase):
    def test_dataset_read(self):
        df = pd.read_csv('Titanic_dummy.csv')

        self.assertEqual(df.shape, (15, 3))

    def test_count_women(self):
        def count_women(df):
            return df[df['Sex'] == 'Female'].shape[0]

        df = pd.read_csv('Titanic_dummy.csv')

        count = count_women(df)

        self.assertEqual(count, 5)

    def test_average_age(self):
        def calculate_average_age(df):
            return df['Age'].mean()

        df = pd.read_csv('Titanic_dummy.csv')

        average_age = calculate_average_age(df)

        self.assertAlmostEqual(average_age, 35.6, places=1)

if name == 'main':
    unittest.main()
    
# Titanic Train CSV file

df = pd.read_csv('train.csv')

num_rows = df.shape[0]
num_cols = df.shape[1]

print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

missing_values = df.isna().sum().sum()

    if missing_values > 0:
        print("There are missing values in the dataset.")
    else:
        print("There are no missing values in the dataset.")
  
num_women = df[df['Sex'] == 'female'].shape[0]

 
print("Number of women:", num_women)
    
average_age = df['Age'].mean()

  
print("Average age of passengers:", average_age)

survival_rate_by_sex = df.groupby('Sex')['Survived'].mean()

higher_survival_sex = survival_rate_by_sex.idxmax()

print("Sex with a higher chance of surviving:", higher_survival_sex)

