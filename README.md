# Solar Energy Analytics Platform

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

An interactive analytics platform for evaluating solar potential across West Africa.  
It analyzes solar irradiance metrics (GHI, DNI, DHI) from **Benin, Sierra Leone, and Togo** to support renewable energy investment decisions.

**Key Objectives:**
- Identify regions with the highest solar potential  
- Compare environmental factors affecting panel efficiency  
- Provide interactive tools for investment planning  

## 🚀 Quick Start

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yitbarek16/solar-challenge-week1.git

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate

3. **Install the requirements**:
    ```bash
    pip install -r requirements.txt

4. **Launch dashboard**:
    ```bash
    streamlit run app/main.py

Or Access at: `solar-dashboard.streamlit.app`

## 📊 Key Insights

| Country       | Avg GHI (W/m²) | Variability | Best Use Case              |
|---------------|----------------|-------------|----------------------------|
| Benin         | 240.6          | High        | Large-scale solar farms    |
| Togo          | 230.6          | Moderate    | Balanced commercial use    |
| Sierra Leone  | 202.0          | Low         | Stable residential solar   |


## Findings:

- Benin shows the highest average GHI but with greater variability
- Sierra Leone provides the most stable irradiance values
- Togo offers balanced performance across metrics

## 🛠️ Features

- Interactive country & metric selection
- Comparative visualizations (bar charts, heatmaps, variability analysis)
- Statistical validation (ANOVA, outlier detection)
- Dashboard

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

---
Let's stay in touch! Feel free to connect with me on LinkedIn:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yitbarektesfaye)
