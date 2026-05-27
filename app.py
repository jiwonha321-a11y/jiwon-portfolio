import streamlit as st
import plotly.express as px
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Jiwon Ha | Portfolio & Profile", 
    page_icon="💻", 
    layout="wide"
)

# Custom Styling function using pure Streamlit components (Safe for Python 3.14)
def section_header(text):
    st.markdown(f"### {text}")
    st.divider()

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Jiwon Ha", use_container_width=True)
    
    st.title("Jiwon Ha")
    st.write("📍 Toronto, ON")
    st.write("✉️ [jiwonj.ha@mail.utoronto.ca](mailto:jiwonj.ha@mail.utoronto.ca)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/jiwonhaaa)")
    
    st.divider()
    st.subheader("🛠️ Technical Core")
    st.code("Python (Pandas / NumPy)\nData Analysis\nOperational Reporting\nExcel Dashboarding\nSOP Development\nCompliance Auditing", language="text")

# ----------------- MAIN CONTENT -----------------
st.title("Jiwon Ha")
st.subheader("Data-Driven Operations Specialist & Python Developer")

# Tabs Definition
tab1, tab2, tab3 = st.tabs(["👋 About Me & Skills", "💻 Experience & Projects", "📊 Interactive Skill Dashboard"])

# --- TAB 1: ABOUT ME & SKILLS ---
with tab1:
    section_header("Professional Summary")
    st.markdown("""
    An operations and data analysis specialist with a robust academic foundation in **Computational Cognition, Psychology, and Statistics** from the **University of Toronto**. 
    Proven track record of optimizing workflows, reducing administrative errors, and architecting data-driven dashboards in high-stakes environments, including the military and hospitality sectors. 
    Characterized by a meticulous, deliberate, and detail-oriented approach to building robust Python scripts and automated data workflows to drive organizational efficiency.
    """)
    
    section_header("Education")
    st.markdown("""
    **University of Toronto, St. George** *Honours Bachelor of Science in Computational Cognition, Psychology and Statistics*
    """)
    
    section_header("Areas of Expertise")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Data & Analytics:** Python (Pandas/NumPy), Advanced Excel, Data Analysis, Operational Reporting
        * **Operations Management:** Process Improvement, Workflow Documentation, SOP Development
        """)
    with col2:
        st.markdown("""
        * **Risk & Quality Control:** Compliance Auditing, Records Management, Inventory Tracking
        * **Leadership:** Stakeholder Communication, Multi-disciplinary Team Coordination
        """)

# --- TAB 2: EXPERIENCE & PROJECTS ---
with tab2:
    section_header("Featured Project")
    with st.container():
        st.subheader("Brigade Logistics Digitalization Project")
        st.caption("Lead Operations & Dashboard Developer | Sep 2024 - Jan 2025")
        st.markdown("""
        * **Real-Time Synchronization:** Architected a multidimensional Excel-based command dashboard for 5+ mission-critical supply streams (Fuel, Rations, Ordnance), achieving 100% real-time synchronization and reducing manual tracking errors by 40%.
        * **Framework Integration:** Integrated automated data-validation frameworks to enhance stock replenishment accuracy by 25% and optimize audit readiness for brigade assets.
        * **Standard Operating Procedures:** Authored a comprehensive SOP manual for digital dashboard operations, accelerating team onboarding speed by 50% and ensuring 100% workflow continuity.
        """)

    section_header("Work Experience")
    
    # Lahan Hotel
    with st.expander("🏨 Lahan Hotel — Operations Support Specialist (Mar 2026 - Present)", expanded=True):
        st.markdown("""
        * Improved guest satisfaction scores by 15% by streamlining front-desk workflows and coordinating with hotel staff to reduce service delays during peak hours.
        * Reduced quarterly supply waste by 10% through inventory tracking, documentation management, and operational process improvements.
        * Supported daily hotel operations by resolving room readiness issues and coordinating across teams to maintain efficient guest service.
        """)

    # Operations & Administrative Specialist
    with st.expander("📊 Operations & Administrative Specialist (Sep 2024 - Jan 2025)", expanded=True):
        st.markdown("""
        * **Increased administrative efficiency by 60%** by digitizing manual workflows and improving operational documentation processes.
        * **
