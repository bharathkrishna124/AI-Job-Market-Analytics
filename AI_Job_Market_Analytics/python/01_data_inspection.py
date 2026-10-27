import pandas as pd

df = pd.read_csv(r"B:\AI_Job_Market_Analytics\dataset\ai_job_dataset.csv")

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== COLUMNS ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print(df.duplicated().sum())

print("\n========== UNIQUE VALUES ==========")
print(df.nunique())

print("\n========== SUMMARY ==========")
print(df.describe(include="all"))