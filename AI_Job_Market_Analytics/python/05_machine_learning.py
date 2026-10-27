# ============================================================
# PHASE 7 — MACHINE LEARNING
# AI Job Market Analytics
# Goal: Predict whether a job belongs to the higher-salary segment
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    ConfusionMatrixDisplay
)


# ============================================================
# 1. LOAD CLEANED DATA
# ============================================================

df = pd.read_csv(
    r"B:\AI_Job_Market_Analytics\dataset\cleaned_ai_job_market.csv"
)

print("=" * 60)
print("AI JOB MARKET ANALYTICS - MACHINE LEARNING")
print("=" * 60)

print("\nDataset shape:", df.shape)


# ============================================================
# 2. CREATE TARGET VARIABLE
# ============================================================

salary_threshold = df["salary_usd"].median()

df["high_salary"] = (
    df["salary_usd"] >= salary_threshold
).astype(int)

print("\nMedian Salary Threshold:")
print(f"${salary_threshold:,.2f}")

print("\nTarget Distribution:")
print(df["high_salary"].value_counts())


# ============================================================
# 3. SELECT FEATURES
# ============================================================

features = [
    "experience_level",
    "employment_type",
    "company_location",
    "company_size",
    "remote_ratio",
    "education_required",
    "years_experience",
    "industry",
    "job_description_length",
    "benefits_score"
]

X = df[features]
y = df["high_salary"]


# ============================================================
# 4. DEFINE CATEGORICAL AND NUMERICAL FEATURES
# ============================================================

categorical_features = [
    "experience_level",
    "employment_type",
    "company_location",
    "company_size",
    "education_required",
    "industry"
]

numeric_features = [
    "remote_ratio",
    "years_experience",
    "job_description_length",
    "benefits_score"
]


# ============================================================
# 5. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# 6. PREPROCESSING
# ============================================================

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            )
        )
    ]
)

numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            categorical_pipeline,
            categorical_features
        ),
        (
            "numeric",
            numeric_pipeline,
            numeric_features
        )
    ]
)


# ============================================================
# 7. LOGISTIC REGRESSION MODEL
# ============================================================

logistic_model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            LogisticRegression(
                max_iter=1000,
                random_state=42
            )
        )
    ]
)

print("\n" + "=" * 60)
print("TRAINING LOGISTIC REGRESSION")
print("=" * 60)

logistic_model.fit(
    X_train,
    y_train
)

logistic_predictions = logistic_model.predict(
    X_test
)

logistic_probabilities = logistic_model.predict_proba(
    X_test
)[:, 1]


# ============================================================
# 8. LOGISTIC REGRESSION EVALUATION
# ============================================================

logistic_accuracy = accuracy_score(
    y_test,
    logistic_predictions
)

logistic_precision = precision_score(
    y_test,
    logistic_predictions,
    zero_division=0
)

logistic_recall = recall_score(
    y_test,
    logistic_predictions,
    zero_division=0
)

logistic_f1 = f1_score(
    y_test,
    logistic_predictions,
    zero_division=0
)

logistic_auc = roc_auc_score(
    y_test,
    logistic_probabilities
)

print("\nLogistic Regression Results:")

print(
    f"Accuracy : {logistic_accuracy:.4f}"
)

print(
    f"Precision: {logistic_precision:.4f}"
)

print(
    f"Recall   : {logistic_recall:.4f}"
)

print(
    f"F1 Score : {logistic_f1:.4f}"
)

print(
    f"ROC-AUC  : {logistic_auc:.4f}"
)


# ============================================================
# 9. RANDOM FOREST MODEL
# ============================================================

random_forest_model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            RandomForestClassifier(
                n_estimators=200,
                random_state=42,
                n_jobs=-1,
                class_weight="balanced"
            )
        )
    ]
)

print("\n" + "=" * 60)
print("TRAINING RANDOM FOREST")
print("=" * 60)

random_forest_model.fit(
    X_train,
    y_train
)

rf_predictions = random_forest_model.predict(
    X_test
)

rf_probabilities = random_forest_model.predict_proba(
    X_test
)[:, 1]


# ============================================================
# 10. RANDOM FOREST EVALUATION
# ============================================================

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

rf_precision = precision_score(
    y_test,
    rf_predictions,
    zero_division=0
)

rf_recall = recall_score(
    y_test,
    rf_predictions,
    zero_division=0
)

rf_f1 = f1_score(
    y_test,
    rf_predictions,
    zero_division=0
)

rf_auc = roc_auc_score(
    y_test,
    rf_probabilities
)

print("\nRandom Forest Results:")

print(
    f"Accuracy : {rf_accuracy:.4f}"
)

print(
    f"Precision: {rf_precision:.4f}"
)

print(
    f"Recall   : {rf_recall:.4f}"
)

print(
    f"F1 Score : {rf_f1:.4f}"
)

print(
    f"ROC-AUC  : {rf_auc:.4f}"
)


# ============================================================
# 11. MODEL COMPARISON
# ============================================================

comparison = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest"
    ],

    "Accuracy": [
        logistic_accuracy,
        rf_accuracy
    ],

    "Precision": [
        logistic_precision,
        rf_precision
    ],

    "Recall": [
        logistic_recall,
        rf_recall
    ],

    "F1 Score": [
        logistic_f1,
        rf_f1
    ],

    "ROC-AUC": [
        logistic_auc,
        rf_auc
    ]
})


print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(
    comparison.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# ============================================================
# 12. CONFUSION MATRIX - LOGISTIC REGRESSION
# ============================================================

ConfusionMatrixDisplay.from_predictions(
    y_test,
    logistic_predictions
)

plt.title(
    "Logistic Regression - Confusion Matrix"
)

plt.tight_layout()
plt.show()


# ============================================================
# 13. CONFUSION MATRIX - RANDOM FOREST
# ============================================================

ConfusionMatrixDisplay.from_predictions(
    y_test,
    rf_predictions
)

plt.title(
    "Random Forest - Confusion Matrix"
)

plt.tight_layout()
plt.show()


# ============================================================
# 14. RANDOM FOREST FEATURE IMPORTANCE
# ============================================================

rf_preprocessor = (
    random_forest_model
    .named_steps["preprocessor"]
)

rf_model = (
    random_forest_model
    .named_steps["model"]
)

feature_names = (
    rf_preprocessor
    .get_feature_names_out()
)

importance_df = pd.DataFrame({

    "feature": feature_names,

    "importance":
        rf_model.feature_importances_
})

importance_df = importance_df.sort_values(
    "importance",
    ascending=False
)


print("\n" + "=" * 60)
print("TOP 20 IMPORTANT FEATURES")
print("=" * 60)

print(
    importance_df
    .head(20)
    .to_string(index=False)
)


# ============================================================
# 15. FEATURE IMPORTANCE CHART
# ============================================================

top_features = (
    importance_df
    .head(15)
    .sort_values("importance")
)

plt.figure(
    figsize=(10, 7)
)

plt.barh(
    top_features["feature"],
    top_features["importance"]
)

plt.title(
    "Top 15 Random Forest Feature Importances"
)

plt.xlabel(
    "Importance"
)

plt.ylabel(
    "Feature"
)

plt.tight_layout()
plt.show()


# ============================================================
# 16. SAVE MODEL COMPARISON
# ============================================================

comparison.to_csv(
    r"B:\AI_Job_Market_Analytics\dataset\ml_model_comparison.csv",
    index=False
)


# ============================================================
# 17. SAVE FEATURE IMPORTANCE
# ============================================================

importance_df.to_csv(
    r"B:\AI_Job_Market_Analytics\dataset\random_forest_feature_importance.csv",
    index=False
)


# ============================================================
# 18. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("MACHINE LEARNING COMPLETED")
print("=" * 60)

print("\nFiles created:")

print(
    "1. B:\\AI_Job_Market_Analytics\\dataset\\ml_model_comparison.csv"
)

print(
    "2. B:\\AI_Job_Market_Analytics\\dataset\\random_forest_feature_importance.csv"
)

print("\nNext step:")
print("MODEL INTERPRETATION AND PROJECT DOCUMENTATION")

print("=" * 60)