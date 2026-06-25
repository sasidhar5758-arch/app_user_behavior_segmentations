import pandas as pd

df = pd.read_csv("data/processed/clustered_data.csv")

profile = df.groupby("Cluster").mean()

print(profile)

profile.to_csv(
    "data/processed/cluster_profile.csv"
)