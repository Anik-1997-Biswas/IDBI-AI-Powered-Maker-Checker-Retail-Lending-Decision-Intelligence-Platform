import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

NUM_CUSTOMERS = 1000

customers = []
transactions = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    # Customer Profile
    age = np.random.randint(21, 60)

    income = np.random.choice([
        30000,
        40000,
        50000,
        70000,
        100000,
        150000,
        200000
    ])

    expenses = int(
        income * np.random.uniform(0.35, 0.75)
    )

    emi = int(
        income * np.random.uniform(0, 0.25)
    )

    balance = int(
        income * np.random.uniform(2, 8)
    )

    credit_score = np.random.randint(650, 850)

    digital_transactions = np.random.randint(20, 300)

    loan_inquiries = np.random.randint(0, 5)

    salary_consistency = round(
        np.random.uniform(0.60, 1.00), 2
    )

    property_interest = np.random.choice(
        [0, 1],
        p=[0.7, 0.3]
    )

    vehicle_interest = np.random.choice(
        [0, 1],
        p=[0.75, 0.25]
    )

    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "age": age,
        "monthly_income": income,
        "monthly_expense": expenses,
        "existing_emi": emi,
        "avg_balance": balance,
        "credit_score": credit_score,
        "digital_transactions": digital_transactions,
        "loan_inquiries": loan_inquiries,
        "salary_consistency": salary_consistency,
        "property_interest": property_interest,
        "vehicle_interest": vehicle_interest
    })

    # Transaction History (12 months)
    for month in range(1, 13):

        salary_credit = int(
            income * np.random.uniform(0.9, 1.1)
        )

        spending = int(
            expenses * np.random.uniform(0.8, 1.2)
        )

        transactions.append({
            "customer_id": customer_id,
            "month": month,
            "salary_credit": salary_credit,
            "monthly_spending": spending,
            "account_balance":
                balance + np.random.randint(-10000, 10000)
        })

# Create DataFrames
customers_df = pd.DataFrame(customers)
transactions_df = pd.DataFrame(transactions)

# Generate target variable for prospect conversion
customers_df["conversion"] = (
    (
        customers_df["credit_score"] > 720
    ).astype(int)
    &
    (
        customers_df["salary_consistency"] > 0.8
    ).astype(int)
)

# Save files
customers_df.to_csv(
    "data/customers.csv",
    index=False
)

transactions_df.to_csv(
    "data/transactions.csv",
    index=False
)

print("\nCustomers Dataset")
print(customers_df.head())

print("\nTransactions Dataset")
print(transactions_df.head())

print("\nCustomers Shape:",
      customers_df.shape)

print("Transactions Shape:",
      transactions_df.shape)