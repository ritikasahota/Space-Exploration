import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_emoji_float import emoji_float

button = st.button("Emoji", icon='👍')
if button :
    emoji_float(emojis=["⭐", "😊", "🎈","🚀","👋"],
                count=40,
                minSize=10,
                maxSize=50,
                animationLength=12)
# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Global Space Exploration Analysis",
    page_icon="🚀",
    layout="wide"
)

# ---------------------- LOAD DATA ----------------------
@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

# ---------------------- TITLE ----------------------
st.title("🚀 Global Space Exploration Analysis")
st.markdown("### Summer Internship Project using Python, Data Science & Streamlit")

# ---------------------- SIDEBAR ----------------------
st.sidebar.title("Home🏠")

menu = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Dashboard",
        "📄 Dataset",
        "📊 Data Summary",
        "🧹 Data Cleaning",
        "📈 Visualizations",
        "🔥 Correlation",
        "📌 Conclusion"
    ]
)

# ---------------------- DASHBOARD ----------------------
if menu == "🏠 Dashboard":

    st.subheader("Project Dashboard")

    total_rows = len(df)
    total_columns = len(df.columns)
    numeric_cols = len(df.select_dtypes(include=np.number).columns)
    missing = int(df.isnull().sum().sum())

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Records", total_rows)
    c2.metric("Total Columns", total_columns)
    c3.metric("Numeric Columns", numeric_cols)
    c4.metric("Missing Values", missing)

    st.markdown("---")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

# ---------------------- DATASET ----------------------
elif menu == "📄 Dataset":

    st.subheader("Dataset Preview")

    rows = st.slider("Number of Rows", 5, 50, 10)

    st.dataframe(df.head(rows))

    st.download_button(
        "Download Dataset",
        df.to_csv(index=False),
        file_name="Global_Space_Exploration_Dataset.csv",
        mime="text/csv"
    )

# ---------------------- SUMMARY ----------------------
elif menu == "📊 Data Summary":

    st.subheader("Dataset Information")

    st.write("Shape :", df.shape)

    st.markdown("### Column Names")
    st.write(df.columns.tolist())

    st.markdown("### Data Types")
    st.dataframe(df.dtypes)

    st.markdown("### Statistical Summary")
    st.dataframe(df.describe(include="all"))

# ---------------------- CLEANING ----------------------
elif menu == "🧹 Data Cleaning":

    st.subheader("Data Cleaning")

    st.markdown("### Missing Values")

    st.dataframe(df.isnull().sum())

    st.markdown("### Duplicate Rows")

    st.write(df.duplicated().sum())

    if st.button("Remove Duplicate Rows"):
        df = df.drop_duplicates()
        st.success("Duplicate rows removed successfully!")

# ---------------------- PLACEHOLDERS ----------------------
elif menu == "📈 Visualizations":

    st.subheader("📈 Interactive Visualizations")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    chart = st.selectbox(
        "Select Visualization",
        [
            "Bar Chart",
            "Pie Chart",
            "Histogram",
            "Box Plot",
            "Scatter Plot",
            "Line Chart"
        ]
    )

    # ---------------- BAR CHART ----------------
    if chart == "Bar Chart":

        column = st.selectbox("Select Categorical Column", categorical_cols)

        fig, ax = plt.subplots(figsize=(10,5))

        df[column].value_counts().plot(
            kind="bar",
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    # ---------------- PIE CHART ----------------
    elif chart == "Pie Chart":

        column = st.selectbox("Select Categorical Column", categorical_cols)

        fig, ax = plt.subplots(figsize=(7,7))

        df[column].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax
        )

        plt.ylabel("")

        st.pyplot(fig)

    # ---------------- HISTOGRAM ----------------
    elif chart == "Histogram":

        column = st.selectbox("Select Numeric Column", numeric_cols)

        fig, ax = plt.subplots(figsize=(8,5))

        ax.hist(df[column], bins=20)

        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")

        st.pyplot(fig)

    # ---------------- BOXPLOT ----------------
    elif chart == "Box Plot":

        column = st.selectbox("Select Numeric Column", numeric_cols)

        fig, ax = plt.subplots(figsize=(8,5))

        sns.boxplot(y=df[column], ax=ax)

        st.pyplot(fig)

    # ---------------- SCATTER ----------------
    elif chart == "Scatter Plot":

        x = st.selectbox("X Axis", numeric_cols)

        y = st.selectbox("Y Axis", numeric_cols)

        fig, ax = plt.subplots(figsize=(8,5))

        ax.scatter(df[x], df[y])

        ax.set_xlabel(x)
        ax.set_ylabel(y)

        st.pyplot(fig)

    # ---------------- LINE ----------------
    elif chart == "Line Chart":

        column = st.selectbox("Select Numeric Column", numeric_cols)

        fig, ax = plt.subplots(figsize=(10,5))

        ax.plot(df[column])

        ax.set_xlabel("Index")
        ax.set_ylabel(column)

        st.pyplot(fig)
elif menu == "🔥 Correlation":

    st.subheader("Correlation Heatmap")

    numeric = df.select_dtypes(include="number")

    fig, ax = plt.subplots(figsize=(10,8))

    sns.heatmap(
        numeric.corr(),
        annot=True,
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    st.pyplot(fig)
elif menu == "📌 Conclusion":
    st.success("""
Global Space Exploration Analysis helps understand mission trends,
budgets, success rates and technological advancements using
Python and Data Science.
""")

