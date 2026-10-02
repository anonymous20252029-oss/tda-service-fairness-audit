# ⚖️️ Topological Auditing of Algorithmic Injustice in High-Stakes Service Encounters

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Double-Blind Review](https://img.shields.io/badge/Peer%20Review-Double--Blind-informational.svg)]()

> **Official Open-Science Repository** supporting the empirical investigation:  
> *"Auditing Algorithmic Injustice in High-Stakes Service Encounters: Reconciling the Scalar Fairness Paradox through Manifold Geometry and Interactive Glass-Box Governance"*  
> Prepared for the **Special Issue on Ethical Implications of AI in Service Industries**, *The Service Industries Journal* (Taylor & Francis).

---

## 📌 Executive Summary & Theoretical Grounding

Conventional industrial audits for algorithmic bias rely predominantly on summary **scalar metrics**—such as Demographic Parity Difference ($DPD$) and Equalized Odds ($EOD$). While statutory frameworks (e.g., the US EEOC 80% rule) celebrate models with near-zero $DPD$, this benchmark reveals a catastrophic blind spot: **macro-level statistical parity frequently masks micro-level geometric discrimination**.

Grounded in **Procedural Justice Theory** and **Service Recovery Frameworks**, this project introduces an end-to-end geometric auditing suite utilizing **Topological Data Analysis (TDA)** and **Persistent Homology**:
1. **$H_0$ Homological Fragmentation:** Quantifies whether protected sub-populations are shattered into disconnected topological clusters.
2. **$H_1$ Persistent Decision Voids:** Identifies non-bounding multi-dimensional loops representing idiosyncratic customer profiles that algorithms fail to generalize.
3. **Simplicial Mapper Architecture:** Translates black-box decision boundaries into glass-box, human-interpretable topological networks, enabling procedural contestability under **Articles 10 and 14 of the European Union AI Act**.

---

## 🔬 Core Empirical Contributions

- **Contribution 1 (Theoretical Reconciliation):** We prove mathematically and empirically that conventional scalar metrics audit only distributive fairness (allocation quotas), whereas topological persistent homology audits procedural fairness (the geometric integrity of the evaluation process).
- **Contribution 2 (The Scalar Fairness Paradox):** Across a stratified 5-fold cross-validation audit spanning Multi-Layer Perceptrons (MLP), Random Forests, and XGBoost, models satisfying statutory fairness ($DPD \le 0.0253$) exhibit substantial 2-Wasserstein topological disparities ($W_2(H_1) = 0.2053 - 0.4858$).
- **Contribution 3 (Contextual Domain Diagnostics):** 
  - **Retail Finance (German & Taiwan Credit):** Uncovers systematic representation collapse and credit line suppression against younger applicants ($<25$) and female cardholders.
  - **Clinical Healthcare (Cleveland Heart & Diabetes 130):** Exposes fatal homological extinction where female atypical cardiac symptoms are treated as background noise, deprioritizing emergency triage.
- **Contribution 4 (Interactive Glass-Box Prototype):** An operationalized decision-support workstation enabling frontline loan officers and triage physicians to trace adverse outcomes and execute verified human-in-the-loop overrides.

---

## 📊 Summary Benchmark Table (5-Fold Stratified Cross-Validation)

| Domain | Dataset | Sensitive Attr. | Model | Accuracy | DPD (Scalar Bias) | $W_2(H_1)$ Void Disparity | Audit Verdict |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Finance** | German Credit | Age ($<25$) | MLP | 0.7133 | 0.0775 ± 0.0533 | **0.3161 ± 0.0458** | ⚠️ Severe Youth Manifold Collapse |
| **Finance** | Taiwan Credit | Gender (Female) | MLP | 0.7819 | 0.0023 ± 0.0039 | **0.4183 ± 0.0463** | 🚨 **Scalar Paradox** (DPD Pass / TDA Fail) |
| **Finance** | Taiwan Credit | Gender (Female) | Random Forest | 0.8120 | 0.0132 ± 0.0035 | **0.4858 ± 0.0764** | 🚨 **Scalar Paradox** (DPD Pass / TDA Fail) |
| **Healthcare** | Cleveland Heart | Biological Sex (F) | MLP | 0.5840 | 0.1120 ± 0.0368 | **0.1154 ± 0.0119** | ⚠️ Atypical Symptom Deprioritization |
| **Healthcare** | Cleveland Heart | Biological Sex (F) | XGBoost | 0.5620 | 0.0472 ± 0.0274 | **0.0000 ± 0.0000** | 💀 Complete Homological Extinction |
| **Healthcare** | Diabetes 130 | Race (African Am.) | XGBoost | 0.5580 | 0.0586 ± 0.0375 | **0.3181 ± 0.2196** | ⚠️ SDoH Post-Discharge Care Void |

---

## 🚀 Repository Structure

```text
├── tables/
│   ├── benchmark_fairness_multimodel_cv.csv   # Consolidated 5-fold CV metrics
│   ├── benchmark_fairness_multimodel_cv.json  # Datafeed for interactive Streamlit prototype
│   └── raw_fold_records.csv                   # Per-fold validation metrics
├── mapper_graphs/
│   ├── German_Credit_mapper_graph.html        # Interactive 2D/3D Simplicial Complex
│   ├── Taiwan_Credit_mapper_graph.html
│   ├── Cleveland_Heart_mapper_graph.html
│   └── Diabetes_130_mapper_graph.html
├── figures/
│   ├── methodology_workflow_diagram.png       # Conceptual methodology architecture
│   ├── topology_concepts_diagram.png          # Visual definition of H0, H1, Mapper
│   ├── metric_comparison_chart.png            # Head-to-head DPD vs. W2(H1) chart
│   └── *_persistence_diagram.png              # Multi-cohort persistence diagrams
├── prototype_app/
│   ├── app.py                                 # Production Streamlit Governance App
│   └── requirements.txt                       # Python dependencies
└── README.md
