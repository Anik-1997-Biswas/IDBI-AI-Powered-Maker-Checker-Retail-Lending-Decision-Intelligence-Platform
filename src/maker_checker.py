import os
import pandas as pd
os.makedirs("data", exist_ok=True)
df=pd.read_csv("data/features.csv")
customer=df.iloc[0]
print("\n ===== AI UNDERWRITING======")
print("Customer ID :",customer["customer_id"])
print("Lead Score:",round(customer["lead_score"],2))
print("Credit score:",customer["credit_score"])
print("FOIR:",round(customer["foir"],2),"%")
print("Repayment capacity",int(customer["repayment_capacity"]))

if(
    customer["lead_score"] >=80
    and customer["foir"] <=40
    and customer["credit_score"] >=700
):
    ai_decision="APPROVE"
elif customer["credit_score"] < 650:
    ai_decision="REJECT"
else:
    ai_decision="REFER TO MANUAL REVIEW"
print("\n AI recommendation:",ai_decision)
####### MAKER REVIEW #####

print("\n===MAKER REVIEW=====")
maker_decision=input("Maker Decision (APPROVE/REJECT):").upper()
maker_comment=input("Maker comment: ")

####CHECKER REVIEW #######

print("\n===CHECKER REVIEW=====")
checker_decision=input(
    "Checker Decision (APPROVE/REJECT):"
).upper()
checker_comment=input("Checker comment: ")

####### FINAL DECISION #########
if (
    maker_decision == "APPROVE"
    and checker_decision == "APPROVE"
):
    final_decision="LOAN APPROVED"
else:
    final_decision="LOAN REJECTED"

#### AUDIT RECORD ####
audit_record = {
    "customer_id": customer["customer_id"],
    "lead_score": customer["lead_score"],
    "credit_score": customer["credit_score"],
    "foir": customer["foir"],
    "ai_decision": ai_decision,
    "maker_decision": maker_decision,
    "maker_comment": maker_comment,
    "checker_decision": checker_decision,
    "checker_comment": checker_comment,
    "final_decision": final_decision
}

audit_df=pd.DataFrame([audit_record])
audit_file="data/audit_log.csv"

if not os.path.exists(audit_file):
    audit_df.to_csv(audit_file, index=False)
else:
    audit_df.to_csv(
        audit_file,
        mode="a",
        header=False,
        index=False
    )
print("\n =========FINAL DECISION==========")
print(final_decision)
print("\n=========AUDIT TRAIL=======")
print(audit_df)
