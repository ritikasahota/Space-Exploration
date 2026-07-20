import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("---")

# ====================================
# PROJECT OVERVIEW
# ====================================

st.header("🚀 Project Overview")

st.write("""
The **Global Space Exploration Analysis Dashboard** is a data science project
developed using Python and Streamlit. It provides interactive analysis of
global space missions conducted by different countries.

The dashboard helps users understand mission trends, budgets, launch sites,
technology usage, mission success rates, and environmental impact through
interactive charts and statistical analysis.
""")

st.markdown("---")

# ====================================
# OBJECTIVES
# ====================================

st.header("🎯 Project Objectives")

st.markdown("""
- Analyze global space exploration data.
- Study mission trends over the years.
- Compare missions across different countries.
- Analyze mission budgets and success rates.
- Visualize important information using interactive charts.
- Generate meaningful insights for decision-making.
""")

st.markdown("---")

# ====================================
# DATASET
# ====================================

st.header("📄 Dataset")

st.write("""
Dataset Name:
**Global Space Exploration Dataset**

Dataset Features:

- Country
- Year
- Mission Name
- Mission Type
- Launch Site
- Satellite Type
- Budget (in Billion $)
- Success Rate (%)
- Technology Used
- Environmental Impact
- Collaborating Countries
- Duration (in Days)
""")

st.markdown("---")

# ====================================
# TECHNOLOGIES
# ====================================

st.header("💻 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Programming

- Python
- Pandas
- NumPy
- Streamlit
""")

with col2:
    st.markdown("""
### Visualization

- Plotly
- Matplotlib
""")

st.markdown("---")

# ====================================
# DASHBOARD FEATURES
# ====================================

st.header("✨ Dashboard Features")

st.markdown("""
✅ Home Dashboard

✅ Dataset Explorer

✅ Interactive Visualizations

✅ Advanced Filters

✅ Statistical Analysis

✅ Project Insights

✅ Download Dataset

✅ Correlation Analysis

✅ Missing Value Analysis

✅ Interactive Charts
""")

st.markdown("---")

# ====================================
# PROJECT WORKFLOW
# ====================================

st.header("📊 Project Workflow")

st.markdown("""
1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Data Visualization
6. Statistical Analysis
7. Insight Generation
8. Dashboard Development
""")

st.markdown("---")

# ====================================
# BENEFITS
# ====================================

st.header("🌍 Benefits")

st.markdown("""
- Understand global mission trends.
- Compare country-wise performance.
- Analyze mission budgets.
- Study technology adoption.
- Evaluate mission success rates.
- Support data-driven decisions.
""")

st.markdown("---")

# ====================================
# FUTURE SCOPE
# ====================================

st.header("🔮 Future Scope")

st.markdown("""
- Integrate live NASA, ESA and ISRO APIs.
- Add Machine Learning prediction.
- Real-time mission tracking.
- AI-powered chatbot.
- Cloud deployment.
- Mobile responsive dashboard.
""")

st.markdown("---")

# ====================================
# DEVELOPER
# ====================================

st.header("👨‍💻 Developer")

st.info("""
**Project Title:**
Global Space Exploration Analysis

**Developed Using:**
Python, Streamlit, Pandas, Plotly, Matplotlib

**Purpose:**
Summer Internship Project in Python with Data Science
""")

st.markdown("---")

st.success("🚀 Thank you for exploring the Global Space Exploration Dashboard!")