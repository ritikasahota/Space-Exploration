import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Filters",
    page_icon="🔍",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

st.title("🔍 Advanced Data Filters")

st.markdown("Filter the dataset based on different parameters.")

st.markdown("---")

# ===========================
# SIDEBAR FILTERS
# ===========================

st.sidebar.header("Select Filters")

country = st.sidebar.multiselect(
    "Country",
    options=sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

mission = st.sidebar.multiselect(
    "Mission Type",
    options=sorted(df["Mission Type"].unique()),
    default=sorted(df["Mission Type"].unique())
)

launch = st.sidebar.multiselect(
    "Launch Site",
    options=sorted(df["Launch Site"].unique()),
    default=sorted(df["Launch Site"].unique())
)

technology = st.sidebar.multiselect(
    "Technology Used",
    options=sorted(df["Technology Used"].unique()),
    default=sorted(df["Technology Used"].unique())
)

year = st.sidebar.slider(
    "Year",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (
        int(df["Year"].min()),
        int(df["Year"].max())
    )
)

# ===========================
# FILTER DATA
# ===========================

filtered_df = df[
    (df["Country"].isin(country)) &
    (df["Mission Type"].isin(mission)) &
    (df["Launch Site"].isin(launch)) &
    (df["Technology Used"].isin(technology)) &
    (df["Year"] >= year[0]) &
    (df["Year"] <= year[1])
]

# ===========================
# KPI CARDS
# ===========================

st.subheader("📊 Filter Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Records", len(filtered_df))
col2.metric("Countries", filtered_df["Country"].nunique())
col3.metric("Mission Types", filtered_df["Mission Type"].nunique())
col4.metric("Launch Sites", filtered_df["Launch Site"].nunique())

st.markdown("---")

# ===========================
# FILTERED DATA
# ===========================

st.subheader("📄 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.markdown("---")

# ===========================
# QUICK SUMMARY
# ===========================

st.subheader("📌 Summary")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
Total Missions : {len(filtered_df)}

Average Budget :
${filtered_df['Budget (in Billion $)'].mean():.2f} Billion

Average Success Rate :
{filtered_df['Success Rate (%)'].mean():.2f}%
"""
    )

with col2:

    st.info(
        f"""
Average Duration :
{filtered_df['Duration (in Days)'].mean():.2f} Days

Countries :
{filtered_df['Country'].nunique()}

Mission Types :
{filtered_df['Mission Type'].nunique()}
"""
    )

st.markdown("---")

# ===========================
# TOP COUNTRIES
# ===========================

st.subheader("🌍 Top Countries")

st.bar_chart(
    filtered_df["Country"].value_counts()
)

st.markdown("---")

# ===========================
# MISSION TYPES
# ===========================

st.subheader("🚀 Mission Types")

st.bar_chart(
    filtered_df["Mission Type"].value_counts()
)

st.markdown("---")

# ===========================
# DOWNLOAD
# ===========================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="Filtered_Global_Space_Exploration.csv",
    mime="text/csv"
)

st.success("✅ Filters applied successfully.")