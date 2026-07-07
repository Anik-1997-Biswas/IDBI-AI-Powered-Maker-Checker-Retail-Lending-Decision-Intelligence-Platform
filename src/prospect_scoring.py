import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import os

os.makedirs("models", exist_ok=True)
df=pd.read_csv("data/features.csv")
X=df[[
    "monthly_income",
    "monthly_expense",
    "existing_emi",
    "credit_score",
    "digital_transactions",
    "salary_consistency",
    "avg_account_balance",
    "foir",
    "repayment_capacity",
    "behavior_score",
    "lead_score"
]]

y=df["conversion"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)
predictions=model.predict(X_test)
accuracy=accuracy_score(y_test,predictions)
print("\n Model Accuracy:")
print(round(accuracy*100,2),"%")
print("\n Classification Report:")
print(classification_report(y_test, predictions))
joblib.dump(
    model,
    "models/prospect_model.pkl"
)
print("\n Model saved successfully..")
##sample prediction
sample=X.iloc[[0]]
probability=model.predict_proba(sample)[0][1]
print("\n Sample Customer")
print("-------------")
print("Customer ID:",df.iloc[0]["customer_id"])
print("Conversion Probability:",
      round(probability*100,2),"%")

if probability > 0.80:
    lead="HOT"
elif probability > 0.50:
    lead="WARM"
else:
    lead="COLD"
print("Lead Category:",lead)

