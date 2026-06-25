import pandas as pd
from sklearn.cluster import KMeans

# Load scaled data
X = pd.read_csv("data/processed/scaled_data.csv")

# Choose optimal K from Elbow Method
k = 4

# Train model
kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X)

# Add cluster labels
X["Cluster"] = clusters

# Save clustered data
X.to_csv(
    "data/processed/clustered_data.csv",
    index=False
)

print("Clustering Completed")
print(X["Cluster"].value_counts())