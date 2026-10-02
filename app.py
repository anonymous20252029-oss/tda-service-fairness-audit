# 2. MÃ NGUỒN CẬP NHẬT HOÀN CHỈNH: `prototype_app/app.py`

Mã nguồn này được thiết kế lại nhằm:
- **Tích hợp 4 Tabs chuyên biệt** thể hiện rõ ràng 4 Đóng góp của bài báo.
- **Có bảng điều khiển tương tác Plotly** trực quan hóa Nghịch lý Bình đẳng Ảo.
- **Tích hợp khung giả lập (Simulator) cho 2 kịch bản thực tế:**
  1. Thẩm định viên Ngân hàng (Loan Underwriting Override).
  2. Bác sĩ Phân luồng Cấp cứu (Emergency Triage Override).
- **Nhúng trực tiếp đồ thị KeplerMapper HTML** ngay trong ứng dụng.

```python
# ==============================================================================
# STREAMLIT INTERACTIVE GOVERNANCE PROTOTYPE: TOPOLOGICAL SERVICE AI AUDITING
# Production Version: Supporting Empirical Contributions & Operational Redress
# ==============================================================================

import streamlit as st
import pandas as pd
import json
import os
import streamlit.components.v1 as components
import plotly.graph_objects as go

# Cấu hình trang hiển thị
st.set_page_config(
    layout="wide",
    page_title="TDA Algorithmic Governance Prototype",
    page_icon="⚖️"
)

# Đường dẫn thư mục dữ liệu
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
TABLES_JSON_PATH = os.path.join(BASE_DIR, "tables", "benchmark_fairness_multimodel_cv.json")
MAPPER_DIR = os.path.join(BASE_DIR, "mapper_graphs")

# Tải dữ liệu kết quả kiểm toán 5-Fold Cross Validation
@st.cache_data
def load_audit_data():
    if os.path.exists(TABLES_JSON_PATH):
        with open(TABLES_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    return pd.DataFrame()

df_audit = load_audit_data()

# ------------------------------------------------------------------------------
# THANH ĐIỀU KHIỂN BÊN TRÁI (SIDEBAR CONTROLS)
# ------------------------------------------------------------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/scales.png", width=70)
st.sidebar.title("Auditing Controls")
st.sidebar.markdown("*High-Stakes Service AI Evaluation Suite*")

if not df_audit.empty:
    dataset_list = df_audit["Dataset"].unique().tolist()
    model_list = df_audit["Model"].unique().tolist()
else:
    dataset_list = ["German_Credit", "Taiwan_Credit", "Cleveland_Heart", "Diabetes_130"]
    model_list = ["MLP", "RandomForest", "XGBoost"]

selected_dataset = st.sidebar.selectbox("1. Choose High-Stakes Benchmark:", dataset_list)
selected_model = st.sidebar.selectbox("2. Select Model Architecture:", model_list)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏛️ Regulatory Context")
st.sidebar.info("""
**EU AI Act Compliance:**
- **Article 10:** Continuous Bias Screening
- **Article 14:** Meaningful Human Oversight
- **US EEOC:** 80% Rule Disparity Threshold
""")

# ------------------------------------------------------------------------------
# TIÊU ĐỀ CHÍNH & DẪN NHẬP
# ------------------------------------------------------------------------------
st.title("⚖️ Auditing Algorithmic Injustice in High-Stakes Service Encounters")
st.markdown("""
*An interactive glass-box governance dashboard reconciling the **Scalar Fairness Paradox** using **Topological Data Analysis (TDA)** and **Simplicial Mapper Complexes**.*
""")

# Thiết lập 4 Tabs chuyên biệt khớp nối chặt chẽ với 4 Đóng góp của bài báo
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Empirical Audit Benchmarks", 
    "🕸️ Interactive Mapper Topology", 
    "🛠️ Operational Redress Simulator",
    "📚 Theoretical Contributions & Insights"
])

# ==============================================================================
# TAB 1: EMPIRICAL BENCHMARKS & SCALAR FAIRNESS PARADOX (CONTRIBUTION 2)
# ==============================================================================
with tab1:
    st.header(f"Cross-Validation Audit: {selected_dataset} ({selected_model})")
    
    if not df_audit.empty:
        filtered = df_audit[(df_audit["Dataset"] == selected_dataset) & (df_audit["Model"] == selected_model)]
        if not filtered.empty:
            row = filtered.iloc[0]
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Accuracy (5-Fold CV)", row.get("Accuracy", "N/A"))
            c2.metric("ROC AUC", row.get("ROC_AUC", "N/A"))
            c3.metric("Statutory Scalar Bias (DPD)", row.get("DPD_Scalar", "N/A"), help="Conventional macro demographic parity difference.")
            c4.metric("Topological Void Disparity W2(H1)", row.get("W2_H1_Void_Disparity", "N/A"), delta_color="inverse", help="Wasserstein distance of 1-dimensional decision voids.")
            
            st.markdown("---")
            st.subheader("The Scalar Fairness Paradox Exposed")
            st.markdown("""
            Notice the striking discrepancy: while conventional **Scalar DPD** remains well below the legal discriminatory threshold ($0.10$), 
            the **Topological Void Disparity $W_2(H_1)$** spikes dramatically, revealing severe latent representation distortion.
            """)
            
            # Trực quan hóa bằng Plotly
            mlp_data = df_audit[df_audit["Model"] == selected_model]
            if not mlp_data.empty:
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=mlp_data["Dataset"],
                    y=mlp_data["DPD_mean_num"],
                    name="Conventional Scalar DPD (Statutory Compliance)",
                    marker_color="#64B5F6"
                ))
                fig.add_trace(go.Bar(
                    x=mlp_data["Dataset"],
                    y=mlp_data["W2_H1_mean_num"],
                    name="Topological Void Disparity W2(H1) (Hidden Bias)",
                    marker_color="#E53935"
                ))
                fig.add_hline(
                    y=0.10, line_dash="dash", line_color="gray",
                    annotation_text="EEOC 80% Legal Threshold (0.10)", annotation_position="top left"
                )
                fig.update_layout(
                    barmode="group",
                    title=f"Head-to-Head Disparity Divergence across Benchmarks ({selected_model})",
                    xaxis_title="High-Stakes Benchmark Datasets",
                    yaxis_title="Disparity Index",
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )
                st.plotly_chart(fig, use_container_width=True)
                
            st.markdown("#### Complete 5-Fold Stratified Cross-Validation Benchmark Suite")
            display_cols = ["Dataset", "Model", "Accuracy", "ROC_AUC", "DPD_Scalar", "EOD_Scalar", "W2_H0_Fragmentation", "W2_H1_Void_Disparity"]
            st.dataframe(df_audit[display_cols], use_container_width=True)
    else:
        st.warning("Audit benchmark JSON not detected. Please ensure 'benchmark_fairness_multimodel_cv.json' is present in the /tables directory.")

# ==============================================================================
# TAB 2: INTERACTIVE MAPPER SIMPLICIAL GRAPH (CONTRIBUTION 3)
# ==============================================================================
with tab2:
    st.header(f"Glass-Box Simplicial Mapper Network: {selected_dataset}")
    st.markdown("""
    *High-dimensional decision spaces are projected and clustered into an interactive simplicial complex. 
    Nodes represent micro-clusters of applicants/patients; edges denote overlapping demographic profiles. 
    **Red flares identify protected sub-cohorts trapped in decision voids.***
    """)
    
    html_file_path = os.path.join(MAPPER_DIR, f"{selected_dataset}_mapper_graph.html")
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as hf:
            html_content = hf.read()
        components.html(html_content, height=720, scrolling=True)
    else:
        st.error(f"Mapper Graph HTML file not found at: `{html_file_path}`. Run the TDA pipeline in Colab to generate this graph.")

# ==============================================================================
# TAB 3: OPERATIONAL REDRESS SIMULATOR (CONTRIBUTION 4)
# ==============================================================================
with tab3:
    st.header("Human-in-the-Loop Redress & Governance Simulator")
    st.markdown("""
    *Simulating frontline operational recovery under **Article 14 of the EU AI Act**. 
    Test how frontline professionals override algorithmic misclassifications situated in persistent topological voids.*
    """)
    
    sim_mode = st.radio("Select Operational Service Encounter:", ["🏦 Financial Credit Underwriting", "🏥 Emergency Clinical Triage"], horizontal=True)
    
    if "Financial" in sim_mode:
        st.subheader("Consumer Credit Underwriting Workstation (German / Taiwan Credit)")
        col_a, col_b = st.columns([1, 1])
        
        with col_a:
            st.markdown("#### Applicant Profile Intake")
            app_id = st.text_input("Applicant Tracking ID:", "APP-2026-8841")
            age = st.slider("Applicant Age:", 18, 70, 23)
            monthly_income = st.number_input("Monthly Income ($):", value=3200, step=100)
            existing_savings = st.number_input("Liquid Savings ($):", value=800, step=100)
            rolling_balance = st.selectbox("Rolling Cash-Flow Trend:", ["Steady Positive", "Volatile", "Negative"])
            
            st.error("🚨 Automated AI Decision: **REJECTED** (High Default Risk Score: 0.78)")
            
        with col_b:
            st.markdown("#### Topological Audit Diagnostics")
            st.warning("""
            **Mapper Diagnostics Triggered:**
            - Applicant mapped to: **Cluster Flare #14** (Protected Young Demographic Void).
            - Topological State: **Trapped in $H_1$ Decision Void** ($p < 0.01$).
            - Diagnostic Cause: The algorithm penalizes brief credit history despite strong cash-flow fundamentals.
            """)
            
            override_reason = st.text_area("Audit Override Justification (EU AI Act Compliance):", "Alternative cash-flow verification shows 24 months of continuous freelance income with zero overdrafts.")
            if st.button("Authorize Human-in-the-Loop Approval (Override AI)"):
                st.success(f"✅ Decision for {app_id} successfully reversed! Loan granted under manual alternative underwriting.")
                st.balloons()
                
    else:
        st.subheader("Acute Emergency Triage Workstation (Cleveland Heart / Diabetes 130)")
        col_c, col_d = st.columns([1, 1])
        
        with col_c:
            st.markdown("#### Patient Intake & Vitals")
            pt_id = st.text_input("Patient Clinical ID:", "MED-2026-9022")
            pt_gender = st.selectbox("Biological Sex:", ["Female", "Male"])
            symptom_chest = st.checkbox("Substernal Crushing Chest Pain", value=False)
            symptom_atypical = st.checkbox("Severe Epigastric Discomfort, Dyspnea & Extreme Lethargy", value=True)
            ecg_initial = st.selectbox("Initial Resting ECG:", ["Normal / Inconclusive", "ST-Elevation", "Arrhythmia"])
            
            st.warning("⚠️ Automated AI Triage: **LOW ACUITY (Non-Emergency Queue)**")
            
        with col_d:
            st.markdown("#### Topological Clinical Safety Net")
            st.error("""
            **Topological Alert (Clinical Collapse Zone):**
            - Patient falls into: **Female Manifold Collapse Cavity ($W_2(H_1) = 0.00$)**.
            - Clinical Warning: Atypical ischemic heart disease presentation detected in female patient. 
            - Risk Factor: Standard male-biased algorithms treat atypical symptoms as non-emergency indigestion.
            """)
            
            if st.button("🚨 Trigger Emergent Clinical Override (Direct Cath Lab Pathway)"):
                st.success(f"🩺 Triage for {pt_id} escalated to **IMMEDIATE ACUITY LEVEL 1**! Stat 12-lead ECG and serial troponin assay ordered.")

# ==============================================================================
# TAB 4: THEORETICAL CONTRIBUTIONS & DOMAIN INSIGHTS (CONTRIBUTION 1)
# ==============================================================================
with tab4:
    st.header("Theoretical Framework & Research Contributions")
    
    st.markdown("""
    ### 1. Procedural Justice vs. Distributive Parity
    - **Distributive Justice (Old Metrics):** Measures *what* is allocated (e.g., equal approval proportions between genders).
    - **Procedural Justice (Our TDA Framework):** Measures *how* the decision is formed. By tracking topological homologies ($H_0, H_1$), we ensure protected applicants undergo an equitable, uncompromised decision process.
    
    ---
    ### 2. The Four High-Stakes Domain Realities
    1. **Taiwan Credit Card Clients ($N=30,000$):** Demonstrates *regulatory gaming*. The model achieves equal approval rates ($DPD = 0.0023$) by compressing female applicants into narrow geometric pockets, suppressing their credit expansion.
    2. **German Credit ($N=1,000$):** Exposes the *youth asset penalty*. Younger workers are fragmented into isolated topological islands ($H_0$), penalized for lack of multi-year financial tenure.
    3. **Cleveland Heart Disease ($N=297$):** Visualizes *clinical manifold collapse*. Tree-based models flatten female cardiac representations into zero cycles ($W_2(H_1) = 0.00$), blind to atypical ischemic manifestations.
    4. **Diabetes 130-US Hospitals ($N=2,500$):** Uncovers *Social Determinants of Health (SDoH) blind spots*. Minority readmission rates are skewed by outpatient care access, creating persistent decision holes in clinical discharge planning.
    
    ---
    ### 3. Managerial 4-Stage Auditing Protocol (EU AI Act Compliance)
    ```
    Stage 1: Pre-Deployment Screening ──> Continuous Integration CI/CD (Compute W2(H1))
    Stage 2: Disparity Threshold Alert  ──> Trigger audit warning if W2(H1) > 0.20
    Stage 3: Root-Cause Localization    ──> Trace applicant clusters on Mapper Graphs
    Stage 4: Active Procedural Redress   ──> Human-in-the-loop override & targeted retraining
    ```
    """)
