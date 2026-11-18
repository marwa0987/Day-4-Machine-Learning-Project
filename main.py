# Day 4 - Machine Learning Project
import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {'Marks': [40, 55, 65, 80, 90],
        'Hours': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
print(df)

# Graph
plt.plot(df['Hours'], df['Marks'])
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Day 4 - Hours vs Marks')
plt.show()

print("Result: Jitne zyada hours, utne zyada marks!")
