import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(
    r"B:\AI_Job_Market_Analytics\dataset\cleaned_ai_job_market.csv"
)

# Handle missing skills
df["required_skills"] = df["required_skills"].fillna("")

# Split skills
df["skill_list"] = df["required_skills"].str.split(",")

# Clean skills
df["skill_list"] = df["skill_list"].apply(
    lambda skills: [
        skill.strip().lower()
        for skill in skills
        if skill.strip()
    ]
)

# Count skills
all_skills = []

for skills in df["skill_list"]:
    all_skills.extend(skills)

skill_counts = Counter(all_skills)

# Display top 15 skills
print("\nTop 15 In-Demand Skills:")

for skill, count in skill_counts.most_common(15):
    print(f"{skill}: {count}")

# Create DataFrame
skill_df = pd.DataFrame(
    skill_counts.items(),
    columns=["skill", "job_count"]
)

skill_df = skill_df.sort_values(
    "job_count",
    ascending=False
)

# Plot
top_skills = skill_df.head(15)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_skills,
    x="job_count",
    y="skill"
)

plt.title("Top 15 In-Demand Skills")
plt.xlabel("Number of Job Postings")
plt.ylabel("Skill")

plt.tight_layout()
plt.show()