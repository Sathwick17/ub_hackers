# Overview
```
Synapse Street is an AI-powered multi-agent system that detects potential short-selling opportunities in the U.S. stock market.
Inspired by The Big Short, this project combines machine learning, large language models, and vector databases to identify patterns that signal overvalued or volatile stocks.
The system autonomously analyzes market data, enables collaboration between AI agents, and delivers interpretable results through interactive dashboards.
```

# 1. Inspiration
```
The idea for Synapse Street was inspired by The Big Short—the story of analysts who spotted early signs of a financial collapse while the market stayed irrationally optimistic.
That principle of data-driven skepticism led us to design a system that questions market sentiment using evidence and AI reasoning.
Three agents—Analyst, Model, and Risk—work together like a digital hedge-fund team, detecting shorting opportunities before they become obvious to everyone else.
```

# 2. What It Does
```
Synapse Street integrates multiple AI and data components to:
Process large-scale historical U.S. stock data (Kaggle: U.S. Stock Market History).
Clean, standardize, and engineer features using Pandas with Hadoop (HDFS-ready).
Apply a Logistic Regression model to compute short probabilities for each ticker.
Store market observations as embeddings in Qdrant for vector similarity search.
Orchestrate three LangGraph agents:
Analyst Agent – detects high-volatility and overbought tickers.
Model Agent – evaluates short probabilities and model metrics.
Risk Agent – assesses exposure and creates interpretable narratives.
Present results in an interactive Streamlit dashboard (deployed via HuggingFace) and Tableau analytics views.
```

# 3. How We Built It
```
Dataset – Kaggle dataset U.S. Stock Market History Data (Eric Stanley), ~5 GB.
Data Processing – Performed with Pandas for feature engineering and integrated with HDFS for scalable file storage on a two-node Vultr Cloud cluster (nn1 + dn1).
Machine Learning – Logistic Regression pipeline built with Scikit-learn (MLflow-ready). Evaluated using AUROC, F1-Score, and Precision@10.
AI Agents (LangGraph) – Three autonomous nodes (Analyst, Model, Risk) coordinated through a StateGraph for stepwise reasoning and task sharing.
Vector Search (Qdrant) – Encoded “notes” combining RSI, MA ratio, and volatility metrics using sentence-transformer embeddings for semantic retrieval.
```

# 4. Visualization 
```
Streamlit dashboard showing probabilities, narratives, and metrics.
Tableau dashboards for performance and feature trend visualization.
Infrastructure – Deployed a distributed HDFS environment on Vultr Cloud supporting collaborative reads/writes from Kaggle notebooks.
```

# 5. Challenges We Faced
```
Connecting Kaggle notebooks to a remote HDFS cluster within time limits.
Managing and preprocessing ~5 GB of data under runtime and memory constraints.
Handling Qdrant embedding fallbacks when the fastembed module was unavailable.
Debugging LangGraph dependency chains and inter-agent state flows.
Deploying Streamlit inside Kaggle, where port 8501 access is blocked.
Building integrated Tableau dashboards from exported artifacts.
```

# 6. Accomplishments
```
Delivered a complete end-to-end multi-agent AI system within a 15-hour hackathon.
Integrated LangGraph, Qdrant, and Scikit-learn into one cohesive finance pipeline.
Achieved AUROC = 0.64 and F1 = 0.45 as baseline model performance.
Produced clear Tableau and Streamlit dashboards for explainable insights.
Published the full system on GitHub for transparency and reproducibility.
```

# 7. What We Learned
```
Designing AI agents to collaborate on financial reasoning tasks.
Using vector search (Qdrant) for contextual retrieval in quantitative workflows.
Structuring multi-agent orchestration with LangGraph StateGraphs.
Managing high-volume financial data with HDFS + Pandas pipelines.
Balancing computational speed and interpretability during rapid prototyping.
```

# 8. What’s Next for Synapse Street
```
Integrate LLM commentary (GPT-5 / Claude API) to generate market summaries.
Deploy a live Streamlit web app via HuggingFace Spaces.
Connect to real-time stock market APIs (Polygon, Alpha Vantage).
Expand to five agents, adding News Sentiment and Portfolio Optimization roles.
Include backtesting and risk-adjusted return metrics (Sharpe Ratio dashboards).
```

# 9. Key Results 
```
AUROC: 0.642
Precision@10: 0.60
Top Short Candidate: KAVL (98.7 % probability)
```

# 10. Files Included
```
picks.csv	- Top 10 short candidates
today_scores.csv	- All analyzed tickers with probabilities
metrics.csv	- Model evaluation metrics
narrative.txt	- AI-agent reasoning summary
equity_curve.csv	- Backtest results
model_pipeline.pkl - Trained Logistic Regression model
```

# 11. Tech Stack    
```
Multi-Agent Framework	- LangGraph
Vector Database	- Qdrant
Machine Learning - Scikit-learn, Regression, LightGBM, OHLCV
Data Processing -	Pandas
Big Data Storage - Hadoop (HDFS)
Visualization -	Streamlit, Tableau
Cloud Infrastructure -	Vultr (two-node HDFS cluster)
Version Control -	GitHub
Deployment Layer -	HuggingFace Spaces
```


## Streamlit Link - https://public.tableau.com/views/Book1_17626741383510/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

## Tableau Dashboard Link - https://public.tableau.com/views/Book1_17626741383510/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link



## Developed By :
```
Siddharth Adhikari
Sathwick Kiran M S
Kundan Satkar
Mrudula Deshmukh
```
