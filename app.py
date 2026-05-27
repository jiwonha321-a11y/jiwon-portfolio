import streamlit as st
import plotly.express as px
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Jiwon Ha | Portfolio & Profile", 
    page_icon="💻", 
    layout="wide"
)

# Custom Styling function using pure Streamlit components
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
    st.markdown("An operations and data analysis specialist with a robust academic foundation in **Computational Cognition, Psychology, and Statistics** from the **University of Toronto**. Proven track record of optimizing workflows, reducing administrative errors, and architecting data-driven dashboards in high-stakes environments. Characterized by a meticulous, deliberate, and detail-oriented approach to building robust Python scripts and automated data workflows to drive organizational efficiency.")
    
    section_header("Education")
    st.markdown("**University of Toronto, St. George** \n*Honours Bachelor of Science in Computational Cognition, Psychology and Statistics*")
    
    section_header("Areas of Expertise")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("* **Data & Analytics:** Python (Pandas/NumPy), Advanced Excel, Data Analysis, Operational Reporting\n* **Operations Management:** Process Improvement, Workflow Documentation, SOP Development")
    with col2:
        st.markdown("* **Risk & Quality Control:** Compliance Auditing, Records Management, Inventory Tracking\n* **Leadership:** Stakeholder Communication, Multi-disciplinary Team Coordination")

# --- TAB 2: EXPERIENCE & PROJECTS ---
with tab2:
    section_header("Featured Project")
    with st.container():
        st.subheader("Brigade Logistics Digitalization Project")
        st.caption("Lead Operations & Dashboard Developer | Sep 2024 - Jan 2025")
        st.markdown("* **Real-Time Synchronization:** Architected a multidimensional Excel command dashboard for 5+ supply streams, achieving 100% synchronization and reducing tracking errors by 40%.\n* **Framework Integration:** Integrated automated data-validation frameworks to enhance stock replenishment accuracy by 25% and optimize audit readiness.\n* **Standard Operating Procedures:** Authored a comprehensive SOP manual for digital dashboard operations, accelerating team onboarding speed by 50%.")

    section_header("Work Experience")
    
    # 1. Lahan Hotel
    with st.expander("🏨 Lahan Hotel — Operations Support Specialist (Mar 2026 - Present)", expanded=True):
        st.markdown("* Improved guest satisfaction scores by 15% by streamlining front-desk workflows and coordinating with hotel staff to reduce service delays.\n* Reduced quarterly supply waste by 10% through data-driven inventory tracking and documentation management.\n* Supported daily hotel operations by resolving room readiness issues and coordinating across teams.")

    # 2. Republic of Korea Army - HR
    with st.expander("🪖 Republic of Korea Army — HR Operations Specialist (Sep 2024 - Mar 2026)"):
        st.markdown("* Maintained 100% accuracy across 150+ personnel records by performing meticulous records management and data verification.\n* Reduced administrative processing errors by supporting payroll audits and improving documentation accuracy.\n* Conducted quarterly audits of 1,200+ confidential personnel files, achieving a 98% compliance accuracy rate.")

    # 3. Republic of Korea Army - Logistics
    with st.expander("🚛 Republic of Korea Army — Logistics Support Specialist (Jan 2025 - Jun 2025)"):
        st.markdown("* Coordinated logistics support for a 30-person ROK/U.S. joint force, achieving 100% on-time material delivery during exercises.\n* Reduced operational downtime by 30% through strict inventory tracking, asset monitoring, and real-time coordination.")

    # 4. Operations & Administrative Specialist
    with st.expander("📊 Operations & Administrative Specialist (Sep 2024 - Jan 2025)", expanded=True):
        st.markdown("* **Increased administrative efficiency by 60%** by digitizing manual workflows and improving operational documentation processes.\n* **Improved leadership response times by 35%** through rigorous operational reporting, data analysis, and summaries.\n* **Managed a secure archive of 3,500+ records** while maintaining a 100% audit pass rate through accurate documentation and compliance tracking.")

    section_header("Leadership Experience")
    
    with st.expander("🎓 University of Toronto Student Union — Recognized Study Group Leader (Sep 2021 - Aug 2024)"):
        st.markdown("* **Increased group academic performance by 30%** by organizing weekly study sessions, structured peer feedback, and collaborative learning.")

# --- TAB 3: INTERACTIVE SKILL DASHBOARD ---
with tab3:
    section_header("Data Visualizations: Competency & Impact")
    st.write("This interactive section demonstrates Python (Pandas & Plotly) utilization directly in the browser to visualize operational impacts.")
    
    st.subheader("Operational Efficiency Improvement Metrics (%)")
    impact_data = pd.DataFrame({
        "Metric / Project Area": [
            "Administrative Efficiency ↑ (Ops Specialist)", 
            "Academic Group Performance ↑ (U of T)",
            "Leadership Response Times ↑ (Ops Specialist)", 
            "Logistics Downtime Reduction ↓ (ROK Army)", 
            "Dashboard Tracking Errors ↓ (Project)",
            "Procurement Turnaround Times ↑ (ROK Army)",
            "Guest Satisfaction Scores ↑ (Lahan Hotel)"
        ],
        "Improvement Percentage (%)": [60, 30, 35, 30, 40, 20, 15],
        "Category": ["Admin & Ops", "Education", "Admin & Ops", "Logistics", "Project", "Logistics", "Hospitality"]
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
    
    st.divider()
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
    fig2.update_traces(fill='toself')
    st.plotly_chart(fig2, use_container_width=True)
