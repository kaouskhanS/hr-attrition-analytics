import pandas as pd
import numpy as np

np.random.seed(42)

n = 1500

data = pd.DataFrame({
    "Age": np.random.randint(18, 60, n),
    "MonthlyIncome": np.random.randint(2000, 20000, n),
    "OverTime": np.random.choice([0,1], n),
    "JobSatisfaction": np.random.randint(1,5,n),
    "YearsAtCompany": np.random.randint(0,20,n),
    "Attrition": np.random.choice([0,1], n, p=[0.7,0.3])
})

data.to_csv("hr_data.csv", index=False)
