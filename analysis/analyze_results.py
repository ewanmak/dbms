import pandas as pd

df = pd.read_csv("../results/sample_results.csv")

summary = df.groupby("encryption_method").mean()
print(summary)
