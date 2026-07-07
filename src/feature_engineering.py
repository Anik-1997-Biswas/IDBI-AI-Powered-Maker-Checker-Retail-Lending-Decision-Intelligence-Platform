import pandas as pd

# Load data
customers = pd.read_csv("data/customers.csv")
transactions = pd.read_csv("data/transactions.csv")

# -----------------------------------
# Transaction level aggregations
# -----------------------------------

transaction_features = (
    transactions
    .groupby("customer_id")
    .agg({
        "salary_credit": "mean",
        "monthly_spending": "mean",
        "account_balance": "mean"
    })
    .reset_index()
)

transaction_features.columns = [
    "customer_id",
    "avg_salary_credit",
    "avg_monthly_spending",
    "avg_account_balance"
]

# -----------------------------------
# Merge with customer data
# -----------------------------------

features = customers.merge(
    transaction_features,
    on="customer_id"
)

# -----------------------------------
# FOIR
# Fixed Obligation to Income Ratio
# -----------------------------------

features["foir"] = round(
    (
        features["existing_emi"]
        /
        features["monthly_income"]
    ) * 100,
    2
)

# -----------------------------------
# Repayment capacity
# -----------------------------------

features["repayment_capacity"] = (
    features["monthly_income"]
    - features["monthly_expense"]
    - features["existing_emi"]
)

# -----------------------------------
# Behavioral score
# -----------------------------------

features["behavior_score"] = (
    features["salary_consistency"] * 40
    +
    (features["credit_score"]/850)*30
    +
    (features["digital_transactions"]/300)*30
)

# -----------------------------------
# Lead score
# -----------------------------------

features["lead_score"] = (
    features["behavior_score"]
    +
    (100 - features["foir"])
)

features["lead_score"] = (
    features["lead_score"]
    .clip(0,100)
)

# Save
features.to_csv(
    "data/features.csv",
    index=False
)

print("\nFeature Dataset")
print(features.head())

print("\nShape")
print(features.shape)