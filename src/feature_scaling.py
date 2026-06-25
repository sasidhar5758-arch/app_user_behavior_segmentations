import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_data.csv")

# Select only numeric columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

print("Numeric Columns:")
print(numeric_cols)

# Remove ID columns if present
exclude_cols = ["User_ID", "user_id", "Customer_ID"]

features = [col for col in numeric_cols if col not in exclude_cols]

X = df[features]

# Standard Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaled data
scaled_df = pd.DataFrame(X_scaled, columns=features)

scaled_df.to_csv(
    "data/processed/scaled_data.csv",
    index=False
)

print("Feature Scaling Completed")
print("Shape:", scaled_df.shape)