import streamlit as st
from dash_style import d_style
from dash_html import d_html

st.set_page_config(
    page_title="DeepTrace",
    page_icon="🔎",
    layout="wide"
)

d_style()

st.title("DeepTrace AI")
st.subheader("AI-Assisted Deepfake Detection")

d_html()

st.write(
    "Analyze audio and video files for potential signs "
    "of manipulation."
)

st.info(
    "This prototype provides advisory results, "
    "not definitive proof of authenticity."
)

st.header("Upload Media")

uploaded_file = st.file_uploader(
    "Choose an audio or video file",
    type=["mp4", "mov", "avi", "mp3", "wav", "m4a"]
)

if uploaded_file is not None:
    st.success(f"File selected: {uploaded_file.name}")
    st.write(f"File size: {uploaded_file.size / (1024 * 1024):.2f} MB")

    if st.button("Analyze Media"):
        st.warning(
            "Upload works! The detection models "
            "still need to be connected."
        )
