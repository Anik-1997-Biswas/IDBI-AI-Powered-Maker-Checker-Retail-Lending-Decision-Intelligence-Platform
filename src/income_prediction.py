import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ---------------------------------------------------
# Create models directory if it doesn't exist
# ---------------------------------------------------
os.makedirs("models", exist_ok=True)

# ---------------------------------------------------
# Load feature dataset
# ---------------------------------------------------
df = pd.read_csv("data/features.csv")

# ---------------------------------------------------
# Features for income prediction
# ---------------------------------------------------
X = df[
    [
        "avg_salary_credit",
        "avg_account_balance",
        "digital_transactions",
        "salary_consistency",
        "credit_score",
        "existing_emi",
    ]
]

# Target variable
y = df["monthly_income"]

# ---------------------------------------------------
# Train-Test Split
# ---------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
)

# ---------------------------------------------------
# Model Training
# ---------------------------------------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
)

model.fit(X_train, y_train)

# ---------------------------------------------------
# Model Evaluation
# ---------------------------------------------------
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========")
print("Mean Absolute Error :", round(mae, 2))
print("R2 Score            :", round(r2, 3))

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------
joblib.dump(
    model,
    "models/income_model.pkl"
)

print("\nIncome model saved successfully.")

# ---------------------------------------------------
# Sample Customer Underwriting
# ---------------------------------------------------
sample = X.iloc[[0]]

predicted_income = model.predict(sample)[0]

customer = df.iloc[0]

print("\n========== CUSTOMER UNDERWRITING ==========")

print("Customer ID          :", customer["customer_id"])
print("Actual Income        :", customer["monthly_income"])
print("Estimated Income     :", int(predicted_income))

# FOIR
foir = (
    customer["existing_emi"]
    / predicted_income
) * 100

print("FOIR                 :", round(foir, 2), "%")

# Repayment Capacity
repayment_capacity = (
    predicted_income
    - customer["monthly_expense"]
    - customer["existing_emi"]
)

print(
    "Repayment Capacity   :",
    int(repayment_capacity),
)

# Affordable EMI
affordable_emi = (
    predicted_income * 0.50
    - customer["existing_emi"]
)

print(
    "Affordable EMI       :",
    int(affordable_emi),
)

# ---------------------------------------------------
# Loan Recommendation
# ---------------------------------------------------
if customer["property_interest"] == 1:
    recommended_loan = "HOME LOAN"

elif customer["vehicle_interest"] == 1:
    recommended_loan = "AUTO LOAN"

elif predicted_income > 100000:
    recommended_loan = "MORTGAGE LOAN"

else:
    recommended_loan = "PERSONAL LOAN"

print(
    "Recommended Product :",
    recommended_loan,
)
