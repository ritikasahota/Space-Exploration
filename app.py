import streamlit as st
import pandas as pd


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Global Space Exploration Dashboard",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/rocket.png", width=90)
st.sidebar.title("🚀 Space Dashboard")

st.sidebar.info("""
**Python Data Science Project**

Global Space Exploration Analysis

Developed using:
- Streamlit
- Pandas
- Matplotlib
""")

# -----------------------------
# TITLE
# -----------------------------
st.title("🚀 Global Space Exploration Analysis")

st.markdown("""
Welcome to the **Global Space Exploration Dashboard**.

This dashboard provides interactive insights into global space missions,
including launch trends, budgets, mission success, environmental impact,
and collaborations between countries.
""")

st.markdown("---")

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Missions", len(df))
col2.metric("Countries", df["Country"].nunique())
col3.metric("Mission Types", df["Mission Type"].nunique())
col4.metric("Launch Sites", df["Launch Site"].nunique())

st.markdown("---")

# -----------------------------
# SECOND ROW
# -----------------------------
col1, col2, col3 = st.columns(3)

avg_budget = df["Budget (in Billion $)"].mean()
avg_success = df["Success Rate (%)"].mean()
avg_duration = df["Duration (in Days)"].mean()

col1.metric(
    "Average Budget",
    f"${avg_budget:.2f} B"
)

col2.metric(
    "Average Success Rate",
    f"{avg_success:.2f}%"
)

col3.metric(
    "Average Duration",
    f"{avg_duration:.0f} Days"
)

st.markdown("---")

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# QUICK INFORMATION
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Shape")
    st.success(f"Rows : {df.shape[0]}")
    st.success(f"Columns : {df.shape[1]}")

with col2:
    st.subheader("Available Features")

    for column in df.columns:
        st.write("✅", column)

st.markdown("---")

# -----------------------------
# TOP COUNTRIES
# -----------------------------
st.subheader("🌍 Top Countries by Missions")

country_count = df["Country"].value_counts()

st.bar_chart(country_count)

st.markdown("---")

# -----------------------------
# MISSION TYPES
# -----------------------------
st.subheader("🚀 Mission Type Distribution")

mission_count = df["Mission Type"].value_counts()

st.bar_chart(mission_count)

st.markdown("---")

# -----------------------------
# TECHNOLOGY USED
# -----------------------------
st.subheader("🛰 Technology Used")

tech = df["Technology Used"].value_counts()

st.bar_chart(tech)

st.markdown("---")

# -----------------------------
# DOWNLOAD
# -----------------------------
st.download_button(
    "⬇ Download Dataset",
    df.to_csv(index=False),
    "Global_Space_Exploration_Dataset.csv",
    "text/csv"
)

st.markdown("---")

st.success("✅ Use the pages in the left sidebar to explore visualizations, filters, statistics, and insights.") 