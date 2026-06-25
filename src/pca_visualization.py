import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load clustered data
df = pd.read_csv("data/processed/clustered_data.csv")

X = df.drop("Cluster", axis=1)

# PCA
pca = PCA(n_components=2)
components = pca.fit_transform(X)

plt.figure(figsize=(10, 6))

plt.scatter(
    components[:, 0],
    components[:, 1],
    c=df["Cluster"],
    cmap="viridis"
)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("User Behavior Clusters")
plt.colorbar(label="Cluster")
plt.show()