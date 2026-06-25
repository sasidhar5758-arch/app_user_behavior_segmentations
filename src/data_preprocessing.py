import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/app_user_behavior.csv")

print(df.dtypes)

# Handle missing values
for col in df.columns:

    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())

    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False
)

print("Data Cleaning Completed")
print("Shape:", df.shape)   