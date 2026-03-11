import mysql.connector
import pandas as pd

# ---------------- DATABASE CONNECTION ---------------- #

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Finance_db"
    )


# ---------------- FETCH DATA FOR DASHBOARD ---------------- #

def fetch_data():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM loan_data")
    rows = cursor.fetchall()

    connection.close()

    df = pd.DataFrame(rows)
    return df


# ---------------- VALIDATION LOGIC ---------------- #

def validate_loan(data):

    errors = []

    if not (data["Loan_ID"].startswith("L") and len(data["Loan_ID"]) == 8):
        errors.append("Loan_ID must start with 'L' and be exactly 8 characters")

    if data["LoanAmount"] < 100 or data["LoanAmount"] > 800:
        errors.append("Loan amount must be between 100 and 800")

    if data["Loan_Amount_Term"] > 360:
        errors.append("Loan term should not exceed 360")

    if data["Credit_History"] != 1:
        errors.append("Credit history must be 1")

    if data["Self_Employed"] == "Yes":
        errors.append("Self-employed applicants are high risk")

    if data["ApplicantIncome"] < data["LoanAmount"]:
        errors.append("Income is less than loan amount")

    if errors:
        return False, errors

    return True, ["Eligible"]


# ---------------- CHECK DUPLICATE ---------------- #

def check_duplicate(loan_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT Loan_ID FROM loan_data WHERE Loan_ID = %s"
    cursor.execute(query, (loan_id,))
    result = cursor.fetchone()

    connection.close()
    return result is not None


# ---------------- INSERT RECORD ---------------- #

def insert_record(data, loan_status):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO loan_data 
        (Loan_ID, Education, ApplicantIncome, LoanAmount,
         Loan_Amount_Term, Credit_History, Self_Employed, Loan_Status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data["Loan_ID"],
            data["Education"],
            data["ApplicantIncome"],
            data["LoanAmount"],
            data["Loan_Amount_Term"],
            data["Credit_History"],
            data["Self_Employed"],
            loan_status
        )

        cursor.execute(query, values)
        connection.commit()
        connection.close()
        return True

    except Exception:
        return False
