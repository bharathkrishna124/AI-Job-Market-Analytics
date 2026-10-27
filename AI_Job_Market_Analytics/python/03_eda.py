import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# AI JOB MARKET ANALYTICS
# EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

print("=" * 70)
print("AI JOB MARKET ANALYTICS - EXPLORATORY DATA ANALYSIS")
print("=" * 70)


# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

df = pd.read_csv(
    r"B:\AI_Job_Market_Analytics\dataset\cleaned_ai_job_market.csv"
)

print("\nDataset loaded successfully.")


# ============================================================
# 2. CONVERT DATE COLUMNS
# ============================================================

print("\nConverting date columns...")

df["posting_date"] = pd.to_datetime(
    df["posting_date"],
    dayfirst=True,
    errors="coerce"
)

df["application_deadline"] = pd.to_datetime(
    df["application_deadline"],
    dayfirst=True,
    errors="coerce"
)

print("Date conversion completed.")


# ============================================================
# 3. BASIC DATASET INFORMATION
# ============================================================

print("\n" + "=" * 50)
print("BASIC DATASET INFORMATION")
print("=" * 50)

print(
    "Total Jobs:",
    len(df)
)

print(
    "Unique Companies:",
    df["company_name"].nunique()
)

print(
    "Unique Job Roles:",
    df["job_title"].nunique()
)

print(
    "Unique Industries:",
    df["industry"].nunique()
)

print(
    "Unique Locations:",
    df["company_location"].nunique()
)


# ============================================================
# 4. TOP 15 JOB ROLES
# ============================================================

print("\n" + "=" * 50)
print("TOP 15 JOB ROLES")
print("=" * 50)

top_roles = (
    df["job_title"]
    .value_counts()
    .head(15)
)

print(top_roles)


# Graph

plt.figure(figsize=(12, 7))

top_roles.sort_values().plot(
    kind="barh"
)

plt.title(
    "Top 15 Job Roles"
)

plt.xlabel(
    "Number of Job Postings"
)

plt.ylabel(
    "Job Role"
)

plt.tight_layout()

plt.show()


# ============================================================
# 5. TOP 15 INDUSTRIES
# ============================================================

print("\n" + "=" * 50)
print("TOP 15 INDUSTRIES")
print("=" * 50)

industry_counts = (
    df["industry"]
    .value_counts()
    .head(15)
)

print(industry_counts)


# Graph

plt.figure(figsize=(12, 7))

industry_counts.sort_values().plot(
    kind="barh"
)

plt.title(
    "Top Industries by Job Postings"
)

plt.xlabel(
    "Number of Jobs"
)

plt.ylabel(
    "Industry"
)

plt.tight_layout()

plt.show()


# ============================================================
# 6. EMPLOYMENT TYPE ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("EMPLOYMENT TYPE")
print("=" * 50)

employment = (
    df["employment_type"]
    .value_counts()
)

print(employment)


# Graph

plt.figure(figsize=(8, 5))

employment.plot(
    kind="bar"
)

plt.title(
    "Jobs by Employment Type"
)

plt.xlabel(
    "Employment Type"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.show()


# ============================================================
# 7. COMPANY SIZE ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("COMPANY SIZE")
print("=" * 50)

company_size = (
    df["company_size"]
    .value_counts()
)

print(company_size)


# Graph

plt.figure(figsize=(8, 5))

company_size.plot(
    kind="bar"
)

plt.title(
    "Jobs by Company Size"
)

plt.xlabel(
    "Company Size"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.show()


# ============================================================
# 8. SALARY ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("SALARY ANALYSIS")
print("=" * 50)

print(
    df["salary_usd"].describe()
)

median_salary = (
    df["salary_usd"].median()
)

mean_salary = (
    df["salary_usd"].mean()
)

print(
    "\nMean Salary:",
    round(mean_salary, 2)
)

print(
    "Median Salary:",
    round(median_salary, 2)
)

print(
    "Minimum Salary:",
    round(df["salary_usd"].min(), 2)
)

print(
    "Maximum Salary:",
    round(df["salary_usd"].max(), 2)
)


# ============================================================
# 9. SALARY DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["salary_usd"],
    bins=40,
    kde=True
)

plt.title(
    "Salary Distribution"
)

plt.xlabel(
    "Salary (USD)"
)

plt.ylabel(
    "Number of Jobs"
)

plt.tight_layout()

plt.show()


# ============================================================
# 10. SALARY BY EXPERIENCE CATEGORY
# ============================================================

print("\n" + "=" * 50)
print("SALARY BY EXPERIENCE CATEGORY")
print("=" * 50)

salary_experience = (
    df.groupby(
        "experience_category"
    )["salary_usd"]
    .agg(
        ["count", "mean", "median"]
    )
    .sort_values(
        "mean",
        ascending=False
    )
)

print(
    salary_experience.round(2)
)


# Graph

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="experience_category",
    y="salary_usd"
)

plt.title(
    "Salary Distribution by Experience"
)

plt.xlabel(
    "Experience Category"
)

plt.ylabel(
    "Salary (USD)"
)

plt.xticks(
    rotation=20
)

plt.tight_layout()

plt.show()


# ============================================================
# 11. AVERAGE SALARY BY JOB ROLE
# ============================================================

print("\n" + "=" * 50)
print("SALARY BY JOB ROLE")
print("=" * 50)

role_salary = (
    df.groupby(
        "job_title"
    )["salary_usd"]
    .agg(
        ["count", "mean", "median"]
    )
    .reset_index()
)

# Only consider roles with at least 10 postings

role_salary = role_salary[
    role_salary["count"] >= 10
]

role_salary = role_salary.sort_values(
    "mean",
    ascending=False
)

print(
    role_salary.head(15).round(2)
)


# Graph

top_role_salary = (
    role_salary
    .head(15)
    .sort_values("mean")
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_role_salary["job_title"],
    top_role_salary["mean"]
)

plt.title(
    "Top 15 Job Roles by Average Salary"
)

plt.xlabel(
    "Average Salary (USD)"
)

plt.ylabel(
    "Job Role"
)

plt.tight_layout()

plt.show()


# ============================================================
# 12. AVERAGE SALARY BY INDUSTRY
# ============================================================

print("\n" + "=" * 50)
print("SALARY BY INDUSTRY")
print("=" * 50)

industry_salary = (
    df.groupby(
        "industry"
    )["salary_usd"]
    .agg(
        ["count", "mean", "median"]
    )
    .reset_index()
)

# Only industries with at least 10 jobs

industry_salary = industry_salary[
    industry_salary["count"] >= 10
]

industry_salary = industry_salary.sort_values(
    "mean",
    ascending=False
)

print(
    industry_salary.round(2)
)


# Graph

top_industry_salary = (
    industry_salary
    .head(15)
    .sort_values("mean")
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_industry_salary["industry"],
    top_industry_salary["mean"]
)

plt.title(
    "Top Industries by Average Salary"
)

plt.xlabel(
    "Average Salary (USD)"
)

plt.ylabel(
    "Industry"
)

plt.tight_layout()

plt.show()


# ============================================================
# 13. SALARY BY COMPANY SIZE
# ============================================================

print("\n" + "=" * 50)
print("SALARY BY COMPANY SIZE")
print("=" * 50)

size_salary = (
    df.groupby(
        "company_size"
    )["salary_usd"]
    .mean()
    .sort_values(
        ascending=False
    )
)

print(
    size_salary.round(2)
)


# Graph

plt.figure(figsize=(8, 5))

size_salary.plot(
    kind="bar"
)

plt.title(
    "Average Salary by Company Size"
)

plt.xlabel(
    "Company Size"
)

plt.ylabel(
    "Average Salary (USD)"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.show()


# ============================================================
# 14. WORK MODE ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("WORK MODE ANALYSIS")
print("=" * 50)

work_mode_counts = (
    df["work_mode"]
    .value_counts()
)

print(
    work_mode_counts
)


# Percentage distribution

work_mode_percentage = (
    df["work_mode"]
    .value_counts(
        normalize=True
    )
    .mul(100)
    .round(2)
)

print(
    "\nWork Mode Percentage:"
)

print(
    work_mode_percentage
)


# Graph

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="work_mode"
)

plt.title(
    "Jobs by Work Mode"
)

plt.xlabel(
    "Work Mode"
)

plt.ylabel(
    "Number of Jobs"
)

plt.tight_layout()

plt.show()


# ============================================================
# 15. SALARY BY WORK MODE
# ============================================================

print("\n" + "=" * 50)
print("SALARY BY WORK MODE")
print("=" * 50)

work_mode_salary = (
    df.groupby(
        "work_mode"
    )["salary_usd"]
    .agg(
        ["count", "mean", "median"]
    )
    .sort_values(
        "mean",
        ascending=False
    )
)

print(
    work_mode_salary.round(2)
)


# Graph

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="work_mode",
    y="salary_usd"
)

plt.title(
    "Salary Distribution by Work Mode"
)

plt.xlabel(
    "Work Mode"
)

plt.ylabel(
    "Salary (USD)"
)

plt.tight_layout()

plt.show()


# ============================================================
# 16. TOP 15 LOCATIONS
# ============================================================

print("\n" + "=" * 50)
print("TOP 15 COMPANY LOCATIONS")
print("=" * 50)

locations = (
    df["company_location"]
    .value_counts()
    .head(15)
)

print(locations)


# Graph

plt.figure(figsize=(12, 7))

locations.sort_values().plot(
    kind="barh"
)

plt.title(
    "Top 15 Company Locations by Job Postings"
)

plt.xlabel(
    "Number of Jobs"
)

plt.ylabel(
    "Company Location"
)

plt.tight_layout()

plt.show()


# ============================================================
# 17. SALARY BY LOCATION
# ============================================================

print("\n" + "=" * 50)
print("SALARY BY LOCATION")
print("=" * 50)

location_salary = (
    df.groupby(
        "company_location"
    )["salary_usd"]
    .agg(
        ["count", "mean", "median"]
    )
    .reset_index()
)

# Only locations with at least 10 jobs

location_salary = location_salary[
    location_salary["count"] >= 10
]

location_salary = location_salary.sort_values(
    "mean",
    ascending=False
)

print(
    location_salary.head(15).round(2)
)


# Graph

top_location_salary = (
    location_salary
    .head(15)
    .sort_values("mean")
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_location_salary["company_location"],
    top_location_salary["mean"]
)

plt.title(
    "Top Locations by Average Salary"
)

plt.xlabel(
    "Average Salary (USD)"
)

plt.ylabel(
    "Company Location"
)

plt.tight_layout()

plt.show()


# ============================================================
# 18. JOB POSTING TREND OVER TIME
# ============================================================

print("\n" + "=" * 50)
print("MONTHLY JOB POSTING TREND")
print("=" * 50)

monthly_jobs = (
    df.groupby(
        df["posting_date"].dt.to_period("M")
    )
    .size()
)

print(monthly_jobs)


# Graph

plt.figure(figsize=(12, 6))

monthly_jobs.plot()

plt.title(
    "Job Posting Trend Over Time"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Number of Job Postings"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.show()


# ============================================================
# 19. YEARLY JOB POSTING TREND
# ============================================================

print("\n" + "=" * 50)
print("YEARLY JOB POSTING TREND")
print("=" * 50)

yearly_jobs = (
    df.groupby(
        df["posting_date"].dt.year
    )
    .size()
)

print(yearly_jobs)


# Graph

plt.figure(figsize=(8, 5))

yearly_jobs.plot(
    kind="bar"
)

plt.title(
    "Job Postings by Year"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Number of Job Postings"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.show()


# ============================================================
# 20. APPLICATION WINDOW ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("APPLICATION WINDOW")
print("=" * 50)

print(
    df["application_window_days"].describe()
)

print(
    "\nAverage Application Window:",
    round(
        df["application_window_days"].mean(),
        2
    ),
    "days"
)

print(
    "Median Application Window:",
    round(
        df["application_window_days"].median(),
        2
    ),
    "days"
)


# Graph

plt.figure(figsize=(10, 6))

sns.histplot(
    df["application_window_days"],
    bins=30,
    kde=True
)

plt.title(
    "Application Window Distribution"
)

plt.xlabel(
    "Application Window (Days)"
)

plt.ylabel(
    "Number of Jobs"
)

plt.tight_layout()

plt.show()


# ============================================================
# 21. EDUCATION REQUIREMENT
# ============================================================

print("\n" + "=" * 50)
print("EDUCATION REQUIREMENT")
print("=" * 50)

education = (
    df["education_required"]
    .value_counts()
)

print(education)


# Graph

plt.figure(figsize=(10, 6))

education.plot(
    kind="bar"
)

plt.title(
    "Jobs by Education Requirement"
)

plt.xlabel(
    "Education Required"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.show()


# ============================================================
# 22. EXPERIENCE CATEGORY DISTRIBUTION
# ============================================================

print("\n" + "=" * 50)
print("EXPERIENCE CATEGORY")
print("=" * 50)

experience_counts = (
    df["experience_category"]
    .value_counts()
)

print(experience_counts)


# Graph

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="experience_category"
)

plt.title(
    "Jobs by Experience Category"
)

plt.xlabel(
    "Experience Category"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=20
)

plt.tight_layout()

plt.show()


# ============================================================
# 23. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("CORRELATION ANALYSIS")
print("=" * 50)

correlation_columns = [
    "salary_usd",
    "remote_ratio",
    "years_experience",
    "job_description_length",
    "benefits_score",
    "application_window_days"
]

correlation_matrix = (
    df[correlation_columns]
    .corr()
)

print(
    correlation_matrix.round(2)
)


# ============================================================
# 24. CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title(
    "Correlation Between Job Market Variables"
)

plt.tight_layout()

plt.show()


# ============================================================
# 25. FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nAnalyses completed:")

print("1. Basic dataset statistics")
print("2. Top job roles")
print("3. Top industries")
print("4. Employment type")
print("5. Company size")
print("6. Salary distribution")
print("7. Salary by experience")
print("8. Salary by job role")
print("9. Salary by industry")
print("10. Salary by company size")
print("11. Work mode")
print("12. Salary by work mode")
print("13. Job locations")
print("14. Salary by location")
print("15. Monthly hiring trends")
print("16. Yearly hiring trends")
print("17. Application window")
print("18. Education requirements")
print("19. Experience category")
print("20. Correlation analysis")

print("\nNext step:")
print("SQL ANALYSIS")

print("=" * 70)