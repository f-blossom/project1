import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from matplotlib.gridspec import GridSpec

# Set the style for Seaborn plots
sns.set(style='dark')

# Load dataset
day_new = pd.read_csv("https://raw.githubusercontent.com/f-blossom/project1/refs/heads/main/dashboard/day.csv")

# Set page configuration for Streamlit
st.set_page_config(page_title="BIKE-RING",
                   page_icon="🚵",
                   layout="wide")
st.markdown("---")

# Title and Subheaders for the Dashboard
st.title("🚵 BIKE-RING: Bike Sharing Dashboard")
st.markdown("---")
st.subheader("Dataframe Jumlah Peminjaman Sepeda")

# Display DataFrame in Streamlit
st.dataframe(day_new.head())
with st.container():
    col1, col2, col3 = st.columns(3, gap='large')
    with col1:
        total_all_rides = day_new['cnt'].sum()
        st.metric("Total Peminjam", value=total_all_rides)
    with col2:
        total_casual_rides = day_new['casual'].sum()
        st.metric("Total Peminjam 'Casual'", value=total_casual_rides)
    with col3:
        total_registered_rides = day_new['registered'].sum()
        st.metric("Total Peminjam 'Registered'", value=total_registered_rides)
    st.markdown("""
    **Keterangan Musim**:
    - 1: Springer (Musim Semi)
    - 2: Summer (Musim Panas)
    - 3: Fall (Musim Gugur)
    - 4: Winter (Musim Dingin)
    """)

with st.sidebar:
    st.sidebar.header("Pertanyaan")

# Buttons for different analysis options
show_answer = st.sidebar.markdown("[Pertanyaan 1](#bagian-1)")
show_main = st.sidebar.markdown("[Pertanyaan 2](#bagian-2)")

st.markdown("## Bagian 1")
st.subheader(
    "1. Bagaimana musim memengaruhi peminjaman sepeda?"
)
st.write("Pada bagian ini akan dibahas analisa pengaruh musim.")
# Section for Season Effects on Bike Rentals
st.subheader("Jumlah Penyewa Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=day_new, estimator=sum, palette='Set2', ax=ax)
ax.set_title('Perbandingan Penyewa Berdasarkan musim', fontsize=16)
ax.set_xlabel('Musim', fontsize=12)
ax.set_ylabel('Jumlah Penyewa', fontsize=12)
st.pyplot(fig)

st.error("Conclusion: Dapat dilihat bahwa jumlah penyewa sepeda naik pada Fall season (musim gugur), dan turun pada springer season (musim semi)")

st.markdown("## Bagian 2")
st.subheader(
    "2. Pada weekdays, hari apa yang paling banyak pengunjung meminjam sepeda?"
)
st.write("Pada bagian ini akan dibahas hari yang paling banyak pengunjung meminjam sepeda.")

# Visualize total bike rentals on Weekdays
st.subheader("Total user pada weekdays")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', data=day_new, estimator=sum, palette='Set2', ax=ax)
ax.set_title('Total user pada weekdays', fontsize=16)
ax.set_xlabel('WEEKDAYS', fontsize=12)
ax.set_ylabel('Total Penggunaan', fontsize=12)
st.pyplot(fig)

st.error("Conclusion: pesanan terbanyak adalah Hari Sabtu, dengan jumlah pesanan mencapai 487.790, \
    diikuti oleh Jumat dan Minggu yang masing-masing mencatatkan 485.395 dan 477.807 pesanan. \
    Sebaliknya, hari dengan pesanan terendah adalah Senin, dengan total 444.027 pesanan.")

st.caption('Copyright (c), created by Andhin Vaniza Zahranie')
