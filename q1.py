import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the provided CSV file ‘data.csv’.
# https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing
df = pd.read_csv("Dataset/data.csv")

# 2. Show the basic statistical description about the data.
print(f"{pd.DataFrame.describe(df)}\n")

# 3. Check if the data has null values.
if df.isnull().values.any():
    print("Dataset contains a null value.\n")

# a. Replace the null values with the mean
mean = df["Calories"].mean()
df["Calories"].fillna(mean, inplace=True)

# 4. Select at least two columns and aggregate the data using: min, max, count, mean.
print(f"Aggregated values:\n"
      f"{df.agg({'Pulse': ['min', 'max', 'count', 'mean'],'Maxpulse': ['min', 'max', 'count', 'mean']})}\n")

# 5. Filter the dataframe to select the rows with calories values between 500 and 1000.
print(f"500-1000 Calories:\n"
      f"{df[(1000 > df['Calories']) & (df['Calories'] > 500)]}\n")

# 6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print(f"Above 500 Calories, Less than 100 Pulse:\n"
      f"{df[(df['Calories'] > 500) & (100 > df['Pulse'])]}\n")

# 7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = df[["Duration", "Pulse", "Calories"]]
print(f"df_modified:\n"
      f"{df_modified}\n")

# 8. Delete the “Maxpulse” column from the main df dataframe
df = df.drop(columns="Maxpulse")
print(f"Maxpulse removed:\n"
      f"{df}")

# 9. Convert the datatype of Calories column to int datatype.
df['Calories'] = df['Calories'].astype('int')
print(f"Calories as int:\n"
      f"{df}")

# 10. Using pandas create a scatter plot for the two columns (Duration and Calories).
df.plot.scatter(x='Duration', y='Calories')
plt.show()
