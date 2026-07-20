import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Project Insights",
    page_icon="💡",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

st.title("💡 Project Insights & Conclusions")

st.markdown("---")

# ======================================
# KPI CARDS
# ======================================

total_missions = len(df)
total_countries = df["Country"].nunique()
avg_budget = df["Budget (in Billion $)"].mean()
avg_success = df["Success Rate (%)"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Missions", total_missions)
col2.metric("Countries", total_countries)
col3.metric("Average Budget", f"${avg_budget:.2f} B")
col4.metric("Average Success", f"{avg_success:.2f}%")

st.markdown("---")

# ======================================
# TOP COUNTRY
# ======================================

st.subheader("🌍 Country with Maximum Missions")

top_country = df["Country"].value_counts().idxmax()
country_count = df["Country"].value_counts().max()

st.success(
    f"{top_country} has the highest number of missions ({country_count})."
)

# ======================================
# TOP MISSION TYPE
# ======================================

st.subheader("🚀 Most Common Mission Type")

top_mission = df["Mission Type"].value_counts().idxmax()
mission_count = df["Mission Type"].value_counts().max()

st.info(
    f"The most common mission type is **{top_mission}** with **{mission_count}** missions."
)

# ======================================
# HIGHEST BUDGET
# ======================================

st.subheader("💰 Highest Budget Mission")

budget_row = df.loc[df["Budget (in Billion $)"].idxmax()]

st.write("Mission Name :", budget_row["Mission Name"])
st.write("Country :", budget_row["Country"])
st.write("Budget :", f"${budget_row['Budget (in Billion $)']} Billion")

# ======================================
# HIGHEST SUCCESS RATE
# ======================================

st.subheader("🏆 Highest Success Rate")

success_row = df.loc[df["Success Rate (%)"].idxmax()]

st.write("Mission :", success_row["Mission Name"])
st.write("Country :", success_row["Country"])
st.write("Success Rate :", f"{success_row['Success Rate (%)']}%")

# ======================================
# LONGEST MISSION
# ======================================

st.subheader("⏳ Longest Mission")

duration_row = df.loc[df["Duration (in Days)"].idxmax()]

st.write("Mission :", duration_row["Mission Name"])
st.write("Duration :", duration_row["Duration (in Days)"], "Days")

# ======================================
# LATEST YEAR
# ======================================

st.subheader("📅 Latest Mission Year")

st.success(df["Year"].max())

st.markdown("---")

# ======================================
# KEY INSIGHTS
# ======================================

st.subheader("📌 Key Insights")

st.markdown("""
### Insight 1
Countries with more missions generally invest more in space research.

### Insight 2
Mission success rates improve with better technology adoption.

### Insight 3
Budget allocation plays an important role in mission planning.

### Insight 4
International collaborations help improve mission success.

### Insight 5
Technological advancements have increased successful launches over the years.

### Insight 6
Environmental impact should be considered while planning future missions.
""")

st.markdown("---")

# ======================================
# CONCLUSION
# ======================================

st.subheader("📖 Conclusion")

st.success("""
The analysis shows that global space exploration has grown significantly over the years.
Countries investing more in technology and international collaboration generally achieve
higher mission success rates. Budget, mission planning, and advanced technology are key
factors influencing successful space missions. This dashboard helps users understand
mission trends, compare countries, and identify patterns through interactive visualizations.
""")

st.markdown("---")

# ======================================
# FUTURE SCOPE
# ======================================

st.subheader("🔮 Future Scope")

st.markdown("""
- Add real-time NASA, ESA, and ISRO mission data.
- Integrate Machine Learning for mission success prediction.
- Add live satellite tracking.
- Include launch weather analysis.
- Connect with cloud databases.
- Deploy the dashboard online using Streamlit Cloud.
""")

st.success("✅ Project insights generated successfully.")