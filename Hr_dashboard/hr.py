import streamlit as st
import pandas as pd

# -------------------------------
# Streamlit Page Configuration
# -------------------------------
st.set_page_config(page_title="HR Data Analysis", page_icon="📊", layout="wide")
st.title("📊 HR Data Analysis Dashboard")

# -------------------------------
# File Upload Section
# -------------------------------
uploaded_file = st.file_uploader("📂 Upload your HR CSV file", type="csv")

if uploaded_file is not None:
    hr_data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Data Preview")
    st.dataframe(hr_data.head())

    st.markdown("---")

    # ---------------------------------
    # SECTION 1: Education Distribution
    # ---------------------------------
    if st.button("1️⃣ Show Education Distribution"):
        education_col = None
        for col in hr_data.columns:
            if 'educ' in col.lower():
                education_col = col
                break

        if education_col:
            st.subheader("🎓 Education Level Distribution")
            education_distribution = hr_data[education_col].value_counts()
            st.write(education_distribution)
            st.bar_chart(education_distribution)
        else:
            st.error("❌ No 'Education' column found in this dataset.")

    # ---------------------------------
    # SECTION 2: College Dropouts
    # ---------------------------------
    if st.button("2️⃣ Show College Dropouts"):
        education_col = None
        for col in hr_data.columns:
            if 'educ' in col.lower():
                education_col = col
                break

        if education_col:
            st.subheader("📉 College Dropouts (Attended but Didn’t Graduate)")

            dropouts = hr_data[
                hr_data[education_col].astype(str).str.contains("some", case=False, na=False)
            ]
            dropouts = dropouts[
                ~dropouts[education_col].astype(str).str.contains("bachelor|master|doctor|phd|graduate", case=False, na=False)
            ]

            st.write(f"Total count: **{dropouts.shape[0]}**")
            if dropouts.shape[0] > 0:
                st.dataframe(dropouts)
            else:
                st.info("No college dropouts found based on current dataset values.")
        else:
            st.error("❌ No 'Education' column found in this dataset.")

    # ---------------------------------
    # SECTION 3: Age Distribution
    # ---------------------------------
    if st.button("3️⃣ Show Age Distribution"):
        if 'Age' in hr_data.columns:
            st.subheader("🧑‍💼 Age Distribution of Employees")
            age_counts = hr_data['Age'].value_counts().sort_index()
            st.line_chart(age_counts)
        else:
            st.error("❌ 'Age' column not found in this dataset.")


    # ---------------------------------
    # SECTION 5: Salary Overview
    # ---------------------------------
    if st.button("5️⃣ Show Salary Overview"):
        salary_cols = [col for col in hr_data.columns if 'salary' in col.lower()]
        if salary_cols:
            col = salary_cols[0]
            st.subheader(f"💰 Salary Overview ({col})")
            st.write(f"Average Salary: **{hr_data[col].mean():,.2f}**")
            st.write(f"Maximum Salary: **{hr_data[col].max():,.2f}**")
            st.write(f"Minimum Salary: **{hr_data[col].min():,.2f}**")
            st.bar_chart(hr_data[col])
        else:
            st.error("❌ No 'Salary' column found in this dataset.")

else:
    st.info("👆 Please upload an HR-related CSV file to begin your analysis.")


