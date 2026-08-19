import pandas as pd
import numpy as np

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR'],
    'Salary': [55000, 75000, 70000, 65000, 58000],
    'Years of Experience': [3, 5, 4, 6, 2]
}

df = pd.DataFrame(data)

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', None)

summary = df.groupby('Department').agg(
    Employees=('Employee', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Total_Salary=('Salary', 'sum')
).round(2)

print(df)
print("\nSUMMARY BY DEPARTMENT")
print(summary)
