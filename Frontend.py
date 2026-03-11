import streamlit as st
import pandas as pd
from main import validate_loan, insert_record, check_duplicate, fetch_data

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Loan Approval Dashboard",
    page_icon="💼",
    layout="wide"
)

# ---------------- CLEAN LIGHT THEME ---------------- #

st.markdown("""
<style>
.stApp {
    background-color: #f5f7fa;
    font-family: 'Segoe UI';
}

h1 {
    color: #0b3c5d;
    font-weight: 700;
}

.sidebar .sidebar-content {
    background-color: #ffffff;
}

.metric-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

menu = st.sidebar.selectbox("Navigation", ["Dashboard", "New Loan Application"])

st.sidebar.markdown("### 🏦 Finance Loan System")
st.sidebar.success("Professional Loan Prediction App")

# ---------------- DASHBOARD ---------------- #

if menu == "Dashboard":

    st.title("📊 Loan Analytics Dashboard")

    df = fetch_data()

    if df.empty:
        st.warning("No data available yet.")
    else:
        total = len(df)
        approved = len(df[df["Loan_Status"] == "Yes"])
        rejected = len(df[df["Loan_Status"] == "No"])

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Applications", total)
        col2.metric("Approved Loans", approved)
        col3.metric("Rejected Loans", rejected)

        st.markdown("---")

        # ---------------- Loan Status Count ---------------- #

        st.subheader("Loan Approval Distribution")

        status_count = df["Loan_Status"].value_counts()
        st.bar_chart(status_count)

        # ---------------- Education vs Loan Status ---------------- #

        st.subheader("Education vs Loan Status")

        edu_status = pd.crosstab(df["Education"], df["Loan_Status"])
        st.bar_chart(edu_status)

    # ---------------- Income Trend ---------------- #

        st.subheader("Applicant Income Trend")

        income_sorted = df.sort_values("ApplicantIncome")
        st.line_chart(income_sorted["ApplicantIncome"])

        # ---------------- Self Employed Distribution ---------------- #

        st.subheader("Self Employed Distribution")

        self_emp = df["Self_Employed"].value_counts()
        st.bar_chart(self_emp)

# ---------------- NEW LOAN APPLICATION ---------------- #

elif menu == "New Loan Application":

    st.title("📝 New Loan Application")

    with st.form("loan_form"):

        # ---------- LINE BY LINE FIELDS ---------- #

        loan_id = st.text_input("Loan ID *")

        education = st.selectbox(
            "Education *",
            ["Select", "Graduate", "Not Graduate"]
        )

        income = st.number_input(
            "Applicant Income *",
            min_value=0
        )

        loan_amount = st.number_input(
            "Loan Amount *",
            min_value=0
        )

        loan_term = st.number_input(
            "Loan Term (Months) *",
            min_value=0
        )

        credit_history = st.selectbox(
            "Credit History *",
            ["Select", 0, 1]
        )

        self_employed = st.selectbox(
            "Self Employed *",
            ["Select", "Yes", "No"]
        )

        submitted = st.form_submit_button("Submit Application")

    if submitted:

        errors = {}

        # --------VALIDATION -------- #

        if not loan_id:
            errors["loan_id"] = "Loan ID is required"

        if education == "Select":
            errors["education"] = "Please select education"

        if income <= 0:
            errors["income"] = "Income must be greater than 0"

        if loan_amount <= 0:
            errors["loan_amount"] = "Loan amount is required"

        if loan_term <= 0:
            errors["loan_term"] = "Loan term is required"

        if credit_history == "Select":
            errors["credit_history"] = "Select credit history"

        if self_employed == "Select":
            errors["self_employed"] = "Select employment type"

        # -------- IF ERRORS EXIST -------- #

        if errors:
            for field, error_msg in errors.items():
                st.error(error_msg)

        # -------- IF NO UI ERRORS -------- #

        else:

            data = {
                "Loan_ID": loan_id,
                "Education": education,
                "ApplicantIncome": income,
                "LoanAmount": loan_amount,
                "Loan_Amount_Term": loan_term,
                "Credit_History": credit_history,
                "Self_Employed": self_employed
            }

            # Check duplicate
            if check_duplicate(loan_id):
                st.error("Loan ID already exists. Please use another ID.")

            else:
                # Business validation
                valid, message = validate_loan(data)

                if valid:
                    success = insert_record(data, "Yes")

                    if success:
                        st.success("Loan Approved successfully ✅")
                    else:
                        st.error("System error. Please try again later.")

                else:
                    insert_record(data, "No")
                    st.error(f"Loan Rejected ")
                    for msg in message:
                        st.error(msg)
