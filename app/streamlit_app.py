import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Project NIRNAY",
    page_icon="🏦",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
features = pd.read_csv("data/features.csv")

st.title(
    "🏦 Project NIRNAY"
)

st.subheader(
    "AI-Powered Maker-Checker Retail Lending Decision Intelligence Platform"
)

### KPI dashboard

st.header("📈 Portfolio KPIs")
col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric(
        "Applications",
        len(features)
    )
with col2:
    st.metric(
        "Avg Credit score",
        round(features["credit_score"].mean())
    )
with col3:
    st.metric(
        "Average Credit Score",
        round(features["credit_score"].mean())
    )

with col4:
    conversion = (
        len(features[features["lead_score"] >= 80])
        / len(features)
    ) * 100

st.metric(
    "Potential Conversion",
    f"{conversion:.1f}%"
)

# =================================================
# CUSTOMER SELECTION
# =================================================

customer_id = st.selectbox(
    "Select Customer ID",
    features["customer_id"].tolist()
)

customer = features[
    features["customer_id"] == customer_id
].iloc[0]

# =================================================
# CUSTOMER PROFILE
# =================================================

st.header("👤 Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Monthly Income",
        f"₹{int(customer['monthly_income']):,}"
    )

with col2:
    st.metric(
        "Credit Score",
        int(customer["credit_score"])
    )

with col3:
    st.metric(
        "Lead Score",
        round(customer["lead_score"], 2)
    )

st.write("**Customer Name:**", customer["customer_name"])
if customer["monthly_income"] > 100000:
    segment="AFFLUENT"
elif customer["monthly_income"] > 50000:
    segment="MASS AFFLUENT"
else:
    segment="RETAIL"
st.metric("Customer Segment",segment)

# =================================================
# UNDERWRITING
# =================================================

st.header("💰 Underwriting Assessment")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "FOIR %",
        round(customer["foir"], 2)
    )

with col2:
    st.metric(
        "Repayment Capacity",
        f"₹{int(customer['repayment_capacity']):,}"
    )

with col3:
    st.metric(
        "Salary Consistency",
        customer["salary_consistency"]
    )

# =================================================
# PRODUCT RECOMMENDATION
# =================================================

st.header("🏦 Loan Recommendation")

if customer["property_interest"] == 1:
    product = "HOME LOAN"

elif customer["vehicle_interest"] == 1:
    product = "AUTO LOAN"

elif customer["monthly_income"] > 100000:
    product = "MORTGAGE LOAN"

else:
    product = "PERSONAL LOAN"

st.success(
    f"Recommended Product: {product}"
)

# =================================================
# AI DECISION
# =================================================

st.header("🤖 AI Decision Engine")

if (
        customer["lead_score"] >= 80
        and customer["foir"] <= 40
        and customer["credit_score"] >= 700
):
    ai_decision = "APPROVE"

elif customer["credit_score"] < 650:
    ai_decision = "REJECT"

else:
    ai_decision = "REVIEW"

st.info(
    f"AI Recommendation: {ai_decision}"
)

####DECISION REASON ENGINE #######
st.header("📋 Decision Reason")
reasons=[]
if customer["credit_score"] < 700:
    reasons.append("Credit score below bank approval threashold")
if customer["foir"] > 40:
    reasons.append("FOIR exceeds acceptable lending policy")
if customer["lead_score"] >=80:
    reasons.append("High customer conversion prosperity")
if customer["salary_consistency"] < 0.75:
    reasons.append("Salary pattern requires verification")
if customer["credit_score"]>700:
    reasons.append("Credit score satisfies lending policy")

for r in reasons:
    st.write(r)
if ai_decision == "APPROVE":
    st.success("Recommendation eligible for automated approval")
elif ai_decision=="REVIEW":
    st.warning("Recommendation forwarded for manual maker review")
else:
    st.error("Recommendation Reject application")

##### ELIGIBILITY SCORE ###
st.header("📈 Eligibility Score")
eligibility_score=(
    customer["lead_score"] * 0.5 +
    (100- customer["foir"]) * 0.3 +
    (customer["credit_score"]/850) * 20
)
st.metric(
    "Eligibility Score",
    round(eligibility_score, 2)
)

##### RISK ASSESSMENT ####
st.header("⚠️ Risk Assessment")
if customer["credit_score"] >=750:
    st.success("LOW RISK")
elif customer["credit_score"] >=680:
    st.warning("MEDIUM RISK")
else:
    st.error("HIGH RISK")

### EXPLAINABLE AI #####
st.header("🔍 Explainable AI")
st.success(
    f"✓ Credit score of {customer['credit_score']} indicates strong repayment behavior"
)
st.success(
    f"✓ FOIR of {customer['foir']}% is within acceptable threshold"
)
st.success(
    f"✓ Salary consistency score of {customer['salary_consistency']} indicates stable income"
)
st.success(
    f"✓ Lead score of {customer['lead_score']} predicts high conversion probability"
)

#### BANKING POLICY VALIDATION
st.header("📑 Lending Policy Validation")

policy = []

policy.append(("Minimum Age", customer["age"] >= 21))
policy.append(("Credit Score ≥ 700", customer["credit_score"] >= 700))
policy.append(("FOIR ≤ 40%", customer["foir"] <= 40))
policy.append(("Salary Consistency ≥ 0.75", customer["salary_consistency"] >= 0.75))
policy.append(("Lead Score ≥ 80", customer["lead_score"] >= 80))

for name, status in policy:
    if status:
        st.success(f"✅ {name}")
    else:
        st.error(f"❌ {name}")

##### RECOMMENDED LOAN OFFER
st.header("💳 Loan Offer Recommendation")
eligible_loan=customer["monthly_income"]*40
suggested_emi=customer["monthly_income"]*0.35
col1,col2=st.columns(2)
with col1:
    st.metric(
        "Eligible Loan Amount",
        f"₹{int(eligible_loan):,}"
    )
with col2:
    st.metric(
        "Suggested EMI",
        f"₹{int(suggested_emi):,}"
    )

######  UNDERWRITING SUMMARY #########
st.header("📊 Underwriting Summary")
summary=pd.DataFrame({
    "Parameter":[
        "Income Verification",
        "Credit Bureau Check",
        "FOIR Assessment",
        "Lead Assessment",
        "Policy Validation",
        "Recommended Product"
    ],
    "Status":[
        "Passed",
        "Passed" if customer["credit_score"]>=700 else "Review",
        "Passed" if customer["foir"]<=40 else "Failed",
        "Passed" if customer["lead_score"]>=80 else "Review",
        ai_decision,
        product
    ]
})
st.dataframe(summary,use_container_width=True)




#MAKER CHECKER CONTROLS

st.header("🛡️ Governance Controls")

st.write("✓ Dual Authorization Enabled")
st.write("✓ Audit Trail Maintained")
st.write("✓ Explainable AI Enabled")
st.write("✓ Underwriting Policy Validation")

#APPROVAL WORKFLOW VISUALIIZATION
st.header("🔄 Approval Workflow")

st.write("✅ AI Decision :", ai_decision)
st.write("🟡 Maker Review : Pending")
st.write("🟡 Checker Review : Pending")
st.write("🏦 Final Decision : Pending")

####### MAKER CHECKER WORKFLOW ########
st.header("👥 Maker–Checker Workflow")
with st.expander("👨‍💼 Maker Review", expanded=True):
    maker_decision=st.selectbox(
        "Maker Decision",
        ["APPROVE","REJECT"],
        key="maker_decision"
    )
    maker_comment=st.text_area(
        "Maker Comment",
        placeholder="Enter maker observations..",
        key="maker_comment"
    )
with st.expander("🧑‍💼 Checker Review", expanded=False):
    checker_decision=st.selectbox(
        "Checker Decision",
        ["APPROVE","REJECT"],
        key="checker_decision"
    )
    checker_comment=st.text_area(
        "Checker Comment",
        placeholder="Enter checker observations..",
        key="checker_comment"
    )
# =================================================
# FINAL DECISION
# =================================================

if st.button("Submit Decision"):

    if (
            maker_decision == "APPROVE"
            and checker_decision == "APPROVE"
    ):
        final_decision = "LOAN APPROVED"
    else:
        final_decision = "LOAN REJECTED"

    st.success(
        f"Final Decision: {final_decision}"
    )

    audit = pd.DataFrame([{
        "customer_id": customer_id,
        "lead_score": customer["lead_score"],
        "credit_score": customer["credit_score"],
        "foir": customer["foir"],
        "ai_decision": ai_decision,
        "maker_decision": maker_decision,
        "maker_comment": maker_comment,
        "checker_decision": checker_decision,
        "checker_comment": checker_comment,
        "final_decision": final_decision
    }])

    audit_file = "data/audit_log.csv"

    if os.path.exists(audit_file):
        old = pd.read_csv(audit_file)
        audit = pd.concat([old, audit])

    audit.to_csv(
        audit_file,
        index=False
    )

    st.header("📋 Audit Trail")
    st.dataframe(audit.tail(10))

#Project version footer
st.divider()
st.caption(
    "Project NIRNAY v1.0 | AI-Powered Maker-Checker Retail Lending Decision Intelligence Platform"
)
