import streamlit as st

st.set_page_config(
    page_title="Air Quality App",
    page_icon="🌫️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌫️ Air Quality Analytics App")

st.markdown("""
Welcome to the **Air Quality Analytics App**.

This application follows a simple workflow:

1. **Upload Dataset**  
2. **Data Description and Preprocessing**  
3. **Exploratory Data Analysis (EDA)**  
4. **Model Building**
""")

st.info("Use the sidebar to navigate between pages.")

st.markdown("---")

st.subheader("Workflow Overview")

section = st.radio(
    "Select a stage to see what it does:",
    (
        "Upload Dataset",
        "Data Description and Preprocessing",
        "EDA",
        "Model Building"
    )
)

if section == "Upload Dataset":
    st.write("""
    On this page, users upload their CSV dataset.

    The uploaded file is saved so it can be reused in the next pages.
    """)

elif section == "Data Description and Preprocessing":
    st.write("""
    On this page, users:
    - preview the dataset
    - check the shape of the data
    - view column names
    - inspect missing values
    - create a basic preprocessed dataset
    """)

elif section == "EDA":
    st.write("""
    On this page, users:
    - view the processed dataset
    - create bar charts
    - create line charts
    - create scatter plots
    - inspect the correlation matrix
    """)

elif section == "Model Building":
    st.write("""
    On this page, users:
    - select a target variable
    - choose feature variables
    - split the dataset into training and testing sets
    - train a Linear Regression model
    - evaluate model performance using R² score
    """)

st.markdown("---")
st.subheader("Quick Help")

col1, col2 = st.columns(2)

with col1:
    if st.button("How to use this app"):
        st.success("""
        Start from **Upload Dataset**, then move to **Data Description**,
        then **EDA**, and finally **Model Building**.
        """)

with col2:
    if st.button("What kind of data should I upload?"):
        st.success("""
        Upload a CSV dataset with at least a few numeric columns.
        Numeric columns are needed for charts and model building.
        """)

st.markdown("---")
st.caption("Tip: Follow the pages in order from the sidebar.")
