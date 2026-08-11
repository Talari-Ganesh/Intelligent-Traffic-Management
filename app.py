import streamlit as st

st.set_page_config(
    page_title="Intelligent Traffic Management",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Intelligent Traffic Management System")

st.write(
    "AI-powered traffic monitoring, vehicle detection, "
    "traffic density analysis, and intelligent signal management."
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🚗 Vehicles", "0")

with col2:
    st.metric("🚦 Traffic Density", "Low")

with col3:
    st.metric("⏱ Signal Time", "30 sec")

with col4:
    st.metric("🚨 Emergency", "None")

st.divider()

st.subheader("📊 Traffic Monitoring")

road = st.selectbox(
    "Select Road",
    ["North Road", "South Road", "East Road", "West Road"]
)

st.info(
    f"Traffic monitoring is currently active for **{road}**."
)

st.subheader("🎥 Traffic Video")

uploaded_video = st.file_uploader(
    "Upload a traffic video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video:
    st.video(uploaded_video)
    st.success("Traffic video uploaded successfully!")