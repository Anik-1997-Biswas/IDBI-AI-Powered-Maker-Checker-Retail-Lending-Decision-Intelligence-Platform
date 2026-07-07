# Project NIRNAY

## AI-Powered Maker-Checker Retail Lending Decision Intelligence Platform

Project NIRNAY is an end-to-end AI prototype built for the **IDBI
Innovate 2026 Hackathon**. It modernizes retail lending by combining
machine learning, underwriting analytics, explainable AI, and a
maker-checker approval workflow.

## Problem Statement

Traditional retail lending relies heavily on static financial metrics,
resulting in: - Low lead conversion - Limited understanding of customer
intent - Manual underwriting effort - Lack of transparent AI governance

This solution identifies high-quality prospects, estimates repayment
capacity, recommends lending products, and supports compliant approval
decisions.

## Features

-   AI Prospect Scoring
-   Income & Repayment Capacity Assessment
-   FOIR (Fixed Obligation to Income Ratio) calculation
-   Product Recommendation (Personal, Home, Auto, Mortgage)
-   Explainable AI decision rationale
-   Lending Policy Validation
-   Eligibility & Risk Scoring
-   Maker--Checker approval workflow
-   Audit Trail generation
-   Interactive Streamlit dashboard

## Tech Stack

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Streamlit
-   Joblib
-   Faker

## Project Structure

``` text
project/
│
├── app/
│   └── streamlit_app.py
├── data/
│   ├── customers.csv
│   ├── transactions.csv
│   ├── features.csv
│   └── audit_log.csv
├── models/
│   ├── prospect_model.pkl
│   └── income_model.pkl
├── src/
│   ├── generate_data.py
│   ├── feature_engineering.py
│   ├── prospect_scoring.py
│   ├── income_prediction.py
│   └── maker_checker.py
├── requirements.txt
└── README.md
```

## Workflow

1.  Generate synthetic customer and transaction data.
2.  Engineer lending features.
3.  Train a prospect scoring model.
4.  Train an income prediction model.
5.  Calculate underwriting metrics (FOIR, repayment capacity).
6.  Recommend lending products.
7.  Produce explainable AI outputs.
8.  Validate against lending policy.
9.  Route through Maker and Checker approvals.
10. Record the decision in an audit trail.

## Dashboard Highlights

-   Portfolio KPIs
-   Customer Profile
-   Underwriting Assessment
-   AI Decision Engine
-   Eligibility Score
-   Risk Assessment
-   Explainable AI
-   Lending Policy Validation
-   Loan Offer Recommendation
-   Underwriting Summary
-   Governance Controls
-   Approval Workflow
-   Audit Trail

## Installation

``` bash
git clone <repository-url>
cd Project-NIRNAY

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## Run

Generate data:

``` bash
python src/generate_data.py
```

Create features:

``` bash
python src/feature_engineering.py
```

Train prospect model:

``` bash
python src/prospect_scoring.py
```

Train income model:

``` bash
python src/income_prediction.py
```

Launch dashboard:

``` bash
streamlit run app/streamlit_app.py
```

## Future Enhancements

-   Bank statement OCR
-   Aadhaar/PAN verification integration
-   Credit bureau APIs
-   Fraud detection
-   GenAI underwriting assistant
-   Role-based authentication
-   Real-time monitoring dashboards

## Author

Anik Biswas

Built as a banking AI portfolio project demonstrating machine learning,
retail lending, underwriting, governance, and explainable AI.
