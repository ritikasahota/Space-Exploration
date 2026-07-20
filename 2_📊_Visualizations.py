import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Visualizations",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

st.title("📊 Interactive Visualizations")

st.markdown("---")

# ============================
# Country Wise Missions
# ============================

st.subheader("🌍 Country-wise Missions")

country = df["Country"].value_counts().reset_index()
country.columns = ["Country", "Missions"]

fig = px.bar(
    country,
    x="Country",
    y="Missions",
    color="Missions",
    title="Number of Missions by Country",
    text_auto=True
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Mission Types
# ============================

st.subheader("🚀 Mission Type Distribution")

mission = df["Mission Type"].value_counts().reset_index()
mission.columns = ["Mission Type", "Count"]

fig = px.pie(
    mission,
    names="Mission Type",
    values="Count",
    hole=0.4,
    title="Mission Type Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Launch Trend
# ============================

st.subheader("📈 Launch Trend by Year")

year = df.groupby("Year").size().reset_index(name="Launches")

fig = px.line(
    year,
    x="Year",
    y="Launches",
    markers=True,
    title="Launches Over the Years"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Budget Analysis
# ============================

st.subheader("💰 Budget Analysis")

fig = px.box(
    df,
    y="Budget (in Billion $)",
    color="Country",
    title="Budget Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Success Rate
# ============================

st.subheader("✅ Success Rate by Country")

success = df.groupby("Country")["Success Rate (%)"].mean().reset_index()

fig = px.bar(
    success,
    x="Country",
    y="Success Rate (%)",
    color="Success Rate (%)",
    text_auto=".1f",
    title="Average Success Rate"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Environmental Impact
# ============================

st.subheader("🌱 Environmental Impact")

impact = df["Environmental Impact"].value_counts().reset_index()
impact.columns = ["Impact", "Count"]

fig = px.bar(
    impact,
    x="Impact",
    y="Count",
    color="Count",
    text_auto=True,
    title="Environmental Impact"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Technology Used
# ============================

st.subheader("🛰️ Technology Used")

tech = df["Technology Used"].value_counts().reset_index()
tech.columns = ["Technology", "Count"]

fig = px.bar(
    tech,
    x="Technology",
    y="Count",
    color="Count",
    text_auto=True,
    title="Technology Used"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Duration Analysis
# ============================

st.subheader("⏳ Mission Duration")

fig = px.histogram(
    df,
    x="Duration (in Days)",
    nbins=20,
    title="Mission Duration Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================
# Budget vs Success Rate
# ============================

st.subheader("📌 Budget vs Success Rate")

fig = px.scatter(
    df,
    x="Budget (in Billion $)",
    y="Success Rate (%)",
    color="Country",
    size="Duration (in Days)",
    hover_data=["Mission Name"],
    title="Budget vs Success Rate"
)

st.plotly_chart(fig, use_container_width=True)

st.success("✅ Interactive charts loaded successfully.")