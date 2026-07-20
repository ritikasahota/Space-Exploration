import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Statistics",
    page_icon="📈",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

st.title("📈 Statistical Analysis")

st.markdown("---")

# ==========================
# DATASET INFORMATION
# ==========================

st.subheader("📋 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))

st.markdown("---")

# ==========================
# DATA TYPES
# ==========================

st.subheader("📌 Data Types")

dtype = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype, use_container_width=True)

st.markdown("---")

# ==========================
# STATISTICAL SUMMARY
# ==========================

st.subheader("📊 Statistical Summary")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

st.markdown("---")

# ==========================
# NUMERIC COLUMNS
# ==========================

st.subheader("🔢 Numeric Columns")

numeric = df.select_dtypes(include="number")

st.write(numeric.columns.tolist())

st.markdown("---")

# ==========================
# CORRELATION MATRIX
# ==========================

st.subheader("📉 Correlation Matrix")

corr = numeric.corr()

st.dataframe(
    corr,
    use_container_width=True
)

st.markdown("---")

# ==========================
# CORRELATION HEATMAP
# ==========================

st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8,6))

heatmap = ax.imshow(corr)

plt.colorbar(heatmap)

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(
    corr.columns,
    rotation=45,
    ha="right"
)

ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)

st.pyplot(fig)

st.markdown("---")

# ==========================
# MISSING VALUES
# ==========================

st.subheader("❗ Missing Value Report")

missing = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Percentage": (
        df.isnull().sum()/len(df)*100
    ).round(2)
})

st.dataframe(
    missing,
    use_container_width=True
)

st.bar_chart(df.isnull().sum())

st.markdown("---")

# ==========================
# UNIQUE VALUES
# ==========================

st.subheader("📑 Unique Values")

unique = pd.DataFrame({
    "Column": df.columns,
    "Unique Values": df.nunique()
})

st.dataframe(
    unique,
    use_container_width=True
)

st.markdown("---")

# ==========================
# OUTLIER ANALYSIS
# ==========================

st.subheader("📦 Outlier Detection")

column = st.selectbox(
    "Select Numeric Column",
    numeric.columns
)

fig, ax = plt.subplots(figsize=(6,4))

ax.boxplot(df[column])

ax.set_title(column)

st.pyplot(fig)

st.markdown("---")