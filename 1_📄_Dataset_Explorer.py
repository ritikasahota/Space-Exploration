import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset Explorer", page_icon="📄", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("Global_Space_Exploration_Dataset.csv")

df = load_data()

st.title("📄 Dataset Explorer")

st.markdown("Explore the Global Space Exploration dataset interactively.")

st.markdown("---")

# ======================
# Dataset Shape
# ======================
col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.markdown("---")

# ======================
# Search
# ======================
st.subheader("🔍 Search Dataset")

search = st.text_input("Enter any keyword")

if search:
    filtered = df[
        df.astype(str).apply(
            lambda x: x.str.contains(search, case=False)
        ).any(axis=1)
    ]
else:
    filtered = df

# ======================
# Rows
# ======================
rows = st.slider(
    "Number of rows to display",
    5,
    min(100, len(filtered)),
    10
)

st.dataframe(
    filtered.head(rows),
    use_container_width=True
)

st.markdown("---")

# ======================
# Column Names
# ======================
st.subheader("📋 Dataset Columns")

for col in df.columns:
    st.write("✅", col)

st.markdown("---")

# ======================
# Data Types
# ======================
st.subheader("📌 Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(
    dtype_df,
    use_container_width=True
)

st.markdown("---")

# ======================
# Missing Values
# ======================
st.subheader("❗ Missing Values")

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum(),
    "Percentage": (
        df.isnull().sum() /
        len(df) * 100
    ).round(2)
})

st.dataframe(
    missing,
    use_container_width=True
)

st.bar_chart(
    df.isnull().sum()
)

st.markdown("---")

# ======================
# Statistics
# ======================
st.subheader("📊 Statistical Summary")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

st.markdown("---")

# ======================
# Sample Records
# ======================
st.subheader("🎲 Random Sample")

sample_size = st.slider(
    "Random Records",
    5,
    20,
    5
)

st.dataframe(
    df.sample(sample_size),
    use_container_width=True
)

st.markdown("---")

# ======================
# Download
# ======================
st.download_button(
    label="⬇ Download Dataset",
    data=df.to_csv(index=False),
    file_name="Global_Space_Exploration_Dataset.csv",
    mime="text/csv"
)

st.success("✅ Dataset loaded successfully.") 