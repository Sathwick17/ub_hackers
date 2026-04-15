<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,100:0ea5e9&height=160&section=header&text=Synapse%20Street&fontSize=42&fontColor=ffffff&fontAlignY=50&desc=AI%20Multi-Agent%20Short-Selling%20Detection%20System%20%7C%20UB%20Hackers%202024&descAlignY=72&descSize=13" width="100%"/>

</div>

<div align="center">

![LangGraph](https://img.shields.io/badge/LangGraph-7c3aed?style=for-the-badge&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-0ea5e9?style=for-the-badge&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-f97316?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Hadoop](https://img.shields.io/badge/Hadoop-FFCE00?style=for-the-badge&logo=apachehadoop&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

[![Tableau Dashboard](https://img.shields.io/badge/View%20Tableau%20Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/Book1_17626741383510/Dashboard1)

</div>

---

> **Inspired by *The Big Short*** — an AI-powered system that questions market optimism using multi-agent reasoning, vector search, and machine learning to detect short-selling opportunities before they're obvious.

---

### 🧠 What is Synapse Street?

Synapse Street is a **multi-agent AI system** built during a 15-hour hackathon at the University at Buffalo. It detects potential short-selling opportunities in the U.S. stock market by combining ML models, LLM agents, and vector databases into one cohesive pipeline — like a digital hedge-fund team operating autonomously.

---

### ⚙️ How It Works

```
U.S. Stock Market Data (~5 GB, Kaggle)
              │
              ▼
   Pandas Feature Engineering
   (RSI, MA Ratio, Volatility, OHLCV)
              │
        ┌─────┴──────┐
        ▼            ▼
    HDFS Cluster   Logistic Regression Model
  (Vultr Cloud)    (Short Probability per Ticker)
                         │
                         ▼
              Qdrant Vector Database
           (Sentence-Transformer Embeddings)
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
        Analyst       Model       Risk
         Agent        Agent       Agent
     (Overbought)  (Probabilities) (Narratives)
              └──────────┬──────────┘
                         ▼
                  LangGraph StateGraph
                  (Agent Orchestration)
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Streamlit               Tableau
        Dashboard              Dashboard
```

---

### 🤖 The Three Agents

| Agent | Role | What It Does |
|-------|------|--------------|
| 🔍 **Analyst Agent** | Market Scanner | Detects high-volatility and overbought tickers using RSI and MA signals |
| 📊 **Model Agent** | Quant Evaluator | Evaluates short probabilities and model metrics per ticker |
| ⚠️ **Risk Agent** | Risk Narrator | Assesses exposure and generates interpretable risk summaries |

---

### 📈 Key Results

| Metric | Result |
|--------|--------|
| AUROC | 0.642 |
| Precision@10 | 0.60 |
| F1-Score | 0.45 |
| Top Short Candidate | **CMAX** — 94.5% short probability |
| Dataset Size | ~5 GB · U.S. Stock Market History |
| Build Time | ⏱️ 15 hours (hackathon) |

---

### 🗂️ Files

| File | Description |
|------|-------------|
| `hackathon_stock.ipynb` | Main notebook — data processing, ML pipeline, agent orchestration |
| `app.py` | Streamlit dashboard app |
| `model_pipeline.pkl` | Trained Logistic Regression model |
| `picks.csv` | Top 10 short candidates with probabilities |
| `today_scores.csv` | All analyzed tickers with short scores |
| `metrics.csv` | Model evaluation metrics |
| `equity_curve.csv` | Backtest equity curve results |
| `narrative.txt` | AI-agent generated reasoning summary |
| `SYNAPSE_STREET.pptx` | Hackathon presentation deck |
| `Tableau Dashboard.pdf` | Exported Tableau analytics views |

---

### 🛠️ Tech Stack

**ML & AI**

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-f97316?style=flat-square&logo=scikitlearn&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-7c3aed?style=flat-square&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0ea5e9?style=flat-square&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-34d399?style=flat-square&logoColor=white)

**Data & Infrastructure**

![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Hadoop](https://img.shields.io/badge/Hadoop_HDFS-FFCE00?style=flat-square&logo=apachehadoop&logoColor=black)
![Vultr](https://img.shields.io/badge/Vultr_Cloud-007BFC?style=flat-square&logoColor=white)

**Visualization & Deployment**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace_Spaces-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

### 🚧 Challenges

- Connecting Kaggle notebooks to a remote HDFS cluster within a 15-hour window
- Preprocessing ~5 GB of financial data under memory and runtime constraints
- Handling Qdrant embedding fallbacks when `fastembed` was unavailable
- Debugging LangGraph inter-agent state flows under time pressure
- Streamlit deployment inside Kaggle (port 8501 blocked)

---

### 🔭 What's Next

- [ ] Integrate live market APIs (Polygon, Alpha Vantage) for real-time scoring
- [ ] Add GPT / Claude commentary for AI-generated market summaries
- [ ] Expand to 5 agents — adding News Sentiment and Portfolio Optimization roles
- [ ] Build Sharpe Ratio and drawdown dashboards for risk-adjusted metrics
- [ ] Deploy full app on HuggingFace Spaces

---

### 👥 Team

Built in 15 hours at **UB Hackers 2024**

| Name |
|------|
| Sathwick Kiran M S |
| Siddharth Adhikari |
| Kundan Satkar |
| Mrudula Deshmukh |

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:7c3aed&height=80&section=footer" width="100%"/>

</div>
