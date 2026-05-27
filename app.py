import streamlit as st
import plotly.express as px
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Jiwon Ha | Portfolio & Profile", 
    page_icon="💻", 
    layout="wide"
)

# Custom Styling function (Safe for Python 3.14)
def section_header(text):
    st.markdown(f"### {text}")
    st.markdown("---")

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown('<div style="text-align: center;">', unsafe_allowed_html=True)
    st.image("https://via.placeholder.com/150", caption="Jiwon Ha")
    st.markdown('</div>', unsafe_allowed_html=True)
    
    st.title("Jiwon Ha")
    st.write("📍 Toronto, ON")
    st.write("✉️ [jiwonj.ha@mail.utoronto.ca](mailto:jiwonj.ha@mail.utoronto.ca)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/jiwonhaaa)")
    
    st.markdown("---")
    st.subheader("🛠️ Technical Core")
    st.code("Python (Pandas / NumPy)\nData Analysis\nOperational Reporting\nExcel Dashboarding\nSOP Development\nCompliance Auditing", language="text")

# ----------------- MAIN CONTENT -----------------
st.title("Jiwon Ha")
st.subheader("Data-Driven Operations Specialist & Python Developer")
st.markdown("<br>", unsafe_allowed_html=True)

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
        * **Real-Time Synchronization:** Architected a multidimensional command dashboard for 5+ mission-critical supply streams (Fuel, Rations, Ordnance), achieving 100% real-time synchronization and reducing manual tracking errors by 40%.
        * **Framework Integration:** Integrated automated data-validation frameworks to enhance stock replenishment accuracy by 25% and optimize audit readiness for brigade assets.
        * **Standard Operating Procedures:** Authored a comprehensive SOP manual for digital dashboard operations, accelerating team onboarding speed by 50% and ensuring 100% workflow continuity.
        """)

    section_header("Professional Experience")
    
    # Lahan Hotel
    with st.expander("🏨 Lahan Hotel — Operations Support Specialist (Mar 2026 - Present)", expanded=True):
        st.markdown("""
        * Improved guest satisfaction scores by 15% by streamlining front-desk workflows and coordinating with hotel staff to reduce service delays during peak hours.
        * Reduced quarterly supply waste by 10% through data-driven inventory tracking, documentation management, and operational process improvements.
        * Supported daily hotel operations by resolving room readiness issues and coordinating across teams to maintain efficient guest service.
        """)
        
    # ROK Army - HR
    with st.expander("🪖 Republic of Korea Army — HR Operations Specialist (Sep 2024 - Mar 2026)"):
        st.markdown("""
        * Maintained 100% accuracy across 150+ personnel records by performing meticulous records management, compliance audits, and data verification procedures.
        * Reduced administrative processing errors by supporting payroll audits, reviewing operational data, and improving documentation accuracy.
        * Conducted quarterly audits of 1,200+ confidential personnel files, achieving a 98% compliance accuracy rate while strictly meeting privacy standards.
        """)

    # ROK Army - Logistics
    with st.expander("🚛 Republic of Korea Army — Logistics Support Specialist (Jan 2025 - Jun 2025)"):
        st.markdown("""
        * Coordinated logistics support for a 30-person ROK/U.S. joint force, achieving 100% on-time material delivery during large-scale training exercises.
        * Reduced operational downtime by 30% through strict inventory tracking, asset monitoring, and real-time logistics coordination.
        * Improved procurement turnaround times by 20% by communicating with suppliers, tracking inventory needs, and supporting workflow coordination.
        """)

# --- TAB 3: INTERACTIVE SKILL DASHBOARD ---
with tab3:
    section_header("Data Visualizations: Competency & Impact")
    st.write("This interactive section demonstrates Python (Pandas & Plotly) utilization directly in the browser to visualize operational impacts.")
    
    # Chart 1: Key Achievements Impact
    st.subheader("Operational Efficiency Improvement Metrics (%)")
    impact_data = pd.DataFrame({
        "Metric / Project Area": [
            "Administrative Efficiency ↑", 
            "Leadership Response Times ↑", 
            "Logistics Downtime Reduction ↓", 
            "Procurement Turnaround Times ↑",
            "Dashboard Tracking Errors ↓",
            "Guest Satisfaction Scores ↑"
        ],
        "Improvement Percentage (%)": [60, 35, 30, 20, 40, 15],
        "Category": ["Admin", "Admin", "Logistics", "Logistics", "Project", "Hospitality"]
    })
    
    fig1 = px.bar(
        impact_data, 
        x="Improvement Percentage (%)", 
        y="Metric / Project Area", 
        color="Category",
        orientation='h',
        title="Quantifiable Contributions Across Roles",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig1.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig1, use_container_width=True)
    
    # Chart 2: Skill Radar Chart Map
    st.markdown("---")
    st.subheader("Core Technical Proficiency Profile")
    
    skills = ["Python (Pandas/NumPy)", "Data Analysis", "Excel Dashboarding", "SOP & Documentation", "Compliance Auditing"]
    levels = [85, 90, 95, 90, 95]
    
    df_skills = pd.DataFrame({"Skill": skills, "Proficiency Level (%)": levels})
    fig2 = px.line_polar(
        df_skills, 
        r="Proficiency Level (%)", 
        theta="Skill", 
        line_close=True,
        title="Skill Radar Chart Map",
        template="plotly_dark"
    )
    fig2.update_traces(fill='adjacent')
    st.plotly_chart(fig2, use_container_width=True)
