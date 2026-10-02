import streamlit as st
import pandas as pd
import json
import os
import streamlit.components.v1 as components
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="TDA AI Audit Prototype", page_icon="⚖️")

st.title("⚖️ Topological Auditing & Governance Dashboard for Service AI")
st.markdown("""
*An interactive glass-box governance dashboard for detecting algorithmic bias and latent manifold disparities in automated finance and healthcare services.*
""")

current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, ".."))
tables_path = os.path.join(base_dir, "tables", "benchmark_fairness_multimodel_cv.json")
mapper_dir = os.path.join(base_dir, "mapper_graphs")

if os.path.exists(tables_path):
    with open(tables_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
else:
    df = pd.DataFrame()

st.sidebar.header("Audit Controls & Datasets")
dataset_list = df['Dataset'].unique().tolist() if not df.empty else ["German_Credit", "Taiwan_Credit", "Cleveland_Heart", "Diabetes_130"]
selected_dataset = st.sidebar.selectbox("Choose Service Benchmark:", dataset_list)
selected_model = st.sidebar.selectbox("Classifier Architecture:", ["MLP", "RandomForest", "XGBoost"])

tab1, tab2, tab3 = st.tabs(["📊 Empirical Audit Benchmarks", "🕸️ Interactive Mapper Topology", "📜 Governance & Redress"])

with tab1:
    st.subheader(f"Auditing Performance: {selected_dataset} ({selected_model})")
    if not df.empty:
        filtered = df[(df['Dataset'] == selected_dataset) & (df['Model'] == selected_model)]
        if not filtered.empty:
            row = filtered.iloc[0]
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Accuracy (5-Fold)", row['Accuracy'])
            c2.metric("ROC AUC", row['ROC_AUC'])
            c3.metric("Scalar DPD", row['DPD_Scalar'])
            c4.metric("Topological W2(H1)", row['W2_H1_Void_Disparity'])
            
            st.markdown("#### Full Multi-Model 5-Fold Cross Validation Table")
            display_cols = ['Dataset', 'Model', 'Accuracy', 'ROC_AUC', 'DPD_Scalar', 'EOD_Scalar', 'W2_H0_Fragmentation', 'W2_H1_Void_Disparity']
            st.dataframe(df[display_cols], use_container_width=True)
            
            st.markdown("#### Scalar Fairness vs. Topological Disparity Paradox")
            fig = go.Figure(data=[
                go.Bar(name='Scalar DPD', x=df[df['Model']=='MLP']['Dataset'], y=df[df['Model']=='MLP']['DPD_mean_num'], marker_color='#64B5F6'),
                go.Bar(name='Topological W2(H1)', x=df[df['Model']=='MLP']['Dataset'], y=df[df['Model']=='MLP']['W2_H1_mean_num'], marker_color='#E53935')
            ])
            fig.update_layout(barmode='group', title="Disparity Metric Comparison across Benchmarks (MLP)")
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader(f"Mapper Graph Simplicial Complex: {selected_dataset}")
    st.markdown("""
    *Each node represents a micro-cluster of decision-space profiles. Red flares identify protected/minority sub-cohorts trapped in decision voids.*
    """)
    html_file = os.path.join(mapper_dir, f"{selected_dataset}_mapper_graph.html")
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as hf:
            html_content = hf.read()
        components.html(html_content, height=650, scrolling=True)
    else:
        st.warning(f"Mapper graph HTML not found at: {html_file}")

with tab3:
    st.subheader("EU AI Act & Managerial Redress Framework")
    st.markdown("""
    ### 4-Stage Managerial Governance Protocol
    1. **Pre-Deployment Topological Screening:** Compute $W_2(H_1)$ during continuous integration (CI/CD).
    2. **Disparity Alert:** Trigger automated audit alerts when $W_2(H_1) > 0.25$, even if standard $DPD < 0.10$.
    3. **Localization via Mapper Graph:** Trace rejected applicant clusters back to input feature distortions.
    4. **Human-in-the-Loop Redress:** Enable manual override for applicants falling into persistent topological voids.
    """)
