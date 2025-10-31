import streamlit as st
import pandas as pd

# --------------------------------
# Streamlit Page Configuration
# --------------------------------
st.set_page_config(page_title="HR Data Analysis", page_icon="📊", layout="wide")
st.title("📊 HR Data Analysis Dashboard")

# --------------------------------
# File Upload Section
# --------------------------------
uploaded_file = st.file_uploader("📂 Upload your HR CSV file", type="csv")

if uploaded_file is not None:
    hr_data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # --------------------------------
    # DATA PREVIEW
    # --------------------------------
    st.subheader("🔍 Data Preview")
    st.dataframe(hr_data.head())

    st.markdown("---")

    # --------------------------------
    # SUMMARY METRICS
    # --------------------------------
    st.subheader("📈 Key HR Insights")

    total_employees = len(hr_data)

    # Detect columns dynamically
    age_col = next((col for col in hr_data.columns if 'age' in col.lower()), None)
    salary_col = next((col for col in hr_data.columns if 'salary' in col.lower()), None)

    avg_age = hr_data[age_col].mean() if age_col else None
    avg_salary = hr_data[salary_col].mean() if salary_col else None

    col1, col2, col3 = st.columns(3)
    col1.metric("👥 Total Employees", f"{total_employees:,}")
    col2.metric("🧓 Average Age", f"{avg_age:.1f}" if avg_age else "N/A")
    col3.metric("💰 Average Salary", f"{avg_salary:,.2f}" if avg_salary else "N/A")

    st.markdown("---")

    # --------------------------------
    # EDUCATION DISTRIBUTION
    # --------------------------------
    education_col = next((col for col in hr_data.columns if 'educ' in col.lower()), None)
    if education_col:
        st.subheader("🎓 Education Level Distribution")
        education_distribution = hr_data[education_col].value_counts()
        st.bar_chart(education_distribution)
        st.dataframe(pd.DataFrame({
            "Education Level": education_distribution.index,
            "Count": education_distribution.values
        }))
    else:
        st.warning("⚠️ No 'Education' column found in dataset.")

    st.markdown("---")

    # --------------------------------
    # AGE DISTRIBUTION
    # --------------------------------
    if age_col:
        st.subheader("🧑‍💼 Age Distribution of Employees")
        age_counts = hr_data[age_col].value_counts().sort_index()
        st.line_chart(age_counts)
    else:
        st.warning("⚠️ No 'Age' column found in dataset.")

    st.markdown("---")

    # --------------------------------
    # SALARY OVERVIEW
    # --------------------------------
    if salary_col:
        st.subheader(f"💰 Salary Overview ({salary_col})")
        avg = hr_data[salary_col].mean()
        max_salary = hr_data[salary_col].max()
        min_salary = hr_data[salary_col].min()

        col1, col2, col3 = st.columns(3)
        col1.metric("Average Salary", f"{avg:,.2f}")
        col2.metric("Highest Salary", f"{max_salary:,.2f}")
        col3.metric("Lowest Salary", f"{min_salary:,.2f}")

        st.bar_chart(hr_data[salary_col])
    else:
        st.warning("⚠️ No 'Salary' column found in this dataset.")

else:
    st.info("👆 Please upload an HR-related CSV file to begin your analysis.")

# --------------------------------
# TEAM CREDITS (Always Visible)
# --------------------------------
st.markdown("""
---
👩‍💻 **Project Created By:**
- Srujan Anirudh  
- Srinivas  
- M. Chathurya  
- Nakka Dharani  
- Pavan  

🏫 **Project:** HR Data Analysis Dashboard  
💡 Built with ❤️ using **Python** & **Streamlit**
""")





