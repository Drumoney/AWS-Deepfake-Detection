
import streamlit as st

def d_style():
    st.markdown("""
    <style>
    .stApp {
        background-color: #0B1220;
        color: #F1F5F9;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    h1, h2, h3 {
        color: #F1F5F9 !important;
    }

    p, label, .stMarkdown {
        color: #CBD5E1;
    }

    [data-testid="stSidebar"] {
        background-color: #111B2E;
        border-right: 1px solid #26364F;
    }

    .stButton > button {
        background-color: #2873B9;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #60A5FA;
        color: #0B1220;
    }

    [data-testid="stFileUploader"] {
        background-color: #172338;
        border: 1px dashed #60A5FA;
        border-radius: 12px;
        padding: 1rem;
    }

    .dashboard-card {
        background-color: #172338;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        min-height: 170px;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }

    .dashboard-card:hover {
        border-color: #60A5FA;
        transform: translateY(-3px);
    }

    .card-icon {
        color: #60A5FA;
        font-size: 28px;
        margin-bottom: 12px;
    }

    .card-title {
        color: #F1F5F9;
        font-size: 18px;
        font-weight: 600;
    }

    .card-description {
        color: #94A3B8;
        font-size: 14px;
    }

    hr {
        border-color: #334155;
    }
    </style>
    """, unsafe_allow_html=True)
