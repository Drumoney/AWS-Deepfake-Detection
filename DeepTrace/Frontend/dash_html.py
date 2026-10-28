import streamlit as st

def d_html():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-icon">📁</div>
            <div class="card-title">Upload Media</div>
            <p class="card-description">
                Upload an audio or video file for analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-icon">🔍</div>
            <div class="card-title">AI Analysis</div>
            <p class="card-description">
                Examine media for potential manipulation.
            </p>
        </div>
        """, unsafe_allow_html=True)