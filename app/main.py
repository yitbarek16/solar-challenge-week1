import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Custom styling
st.set_page_config(
    page_title="Solar Analytics Dashboard",
    layout="wide",
)

# Load your real data
@st.cache_data
def load_data():
    return pd.DataFrame({
        'Country': ['Benin', 'Sierra Leone', 'Togo'],
        'GHI_mean': [240.56, 201.96, 230.56],
        'GHI_median': [1.8, 0.3, 2.1],
        'GHI_std': [331.13, 298.50, 322.53],
        'DNI_mean': [167.19, 116.38, 151.26],
        'DNI_median': [-0.1, -0.1, 0.0],
        'DNI_std': [261.71, 218.65, 250.96],
        'DHI_mean': [115.36, 113.72, 116.44],
        'DHI_median': [1.6, -0.1, 2.5],
        'DHI_std': [158.69, 158.95, 156.52]
    })

df = load_data()

# Dashboard Header
st.title("☀️ Solar Potential Analysis Dashboard")
st.markdown("---")

# Sidebar Filters
with st.sidebar:
    st.header("Filters")
    metrics = st.multiselect(
        "Select Metrics",
        ['GHI', 'DNI', 'DHI'],
        default=['GHI', 'DNI', 'DHI']
    )
    chart_type = st.selectbox(
        "Chart Type",
        ['Bar Chart']
    )

# Metrics Display
st.header("Performance Metrics")
metric_cols = st.columns(len(metrics))
for i, metric in enumerate(metrics):
    with metric_cols[i]:
        st.metric(
            label=f"Highest {metric} (Mean)",
            value=f"{df[f'{metric}_mean'].max():.2f} W/m²",
            delta=f"{df.loc[df[f'{metric}_mean'].idxmax(), 'Country']}"
        )

# Visualization Section
st.header("Comparative Analysis")
fig_cols = st.columns(2)

with fig_cols[0]:
    st.subheader("Mean Values Comparison")
    fig1, ax1 = plt.subplots(figsize=(10,6))
    melted_df = df.melt(id_vars=['Country'], 
                        value_vars=[f'{m}_mean' for m in metrics],
                        var_name='Metric', 
                        value_name='Value')
    sns.barplot(data=melted_df, x='Country', y='Value', hue='Metric', palette='viridis')
    plt.xticks(rotation=45)
    plt.ylabel("Varriance (W/m²)")
    st.pyplot(fig1)

with fig_cols[1]:
    st.subheader("Variability (Standard Deviation)")
    fig2, ax2 = plt.subplots(figsize=(10,6))
    sns.barplot(data=df, x='Country', y='GHI_std', color='skyblue', label='GHI')
    sns.barplot(data=df, x='Country', y='DNI_std', color='orange', label='DNI', alpha=0.7)
    sns.barplot(data=df, x='Country', y='DHI_std', color='green', label='DHI', alpha=0.7)
    plt.xticks(rotation=45)
    plt.ylabel("Standard Deviation")
    plt.legend()
    st.pyplot(fig2)



