import pandas as pd

def Nth_Highest_Salary(n):
    df = pd.read_csv('employee.csv')

    values_array = df.Salary.sort_values(ascending=False).values
    return values_array[n-1]

