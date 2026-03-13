🛡️ Financial Fraud Detection System v2.0

An end-to-end data science project designed to detect fraudulent credit card transactions.
The main objective of this project is to handle extreme class imbalance and identify anomalous transaction patterns that indicate fraud.

🚀 Features
📊 Interactive Dashboard

A Streamlit-based UI that visualizes:

Transaction distribution

Fraud rates

Transaction amount patterns

🧠 Neural Network Ready

Dashboard preprocessing includes:

Log transformation for skewed features

Data preparation suitable for ML models

🗄️ Database Management

Uses SQLite for efficient data storage

Fast query execution via SQLAlchemy

📈 Analytical Insights

Each visualization provides actionable insights useful for:

Model training strategy

Handling imbalanced datasets (SMOTE / Undersampling)

🛠️ Tech Stack
Category	Tools
Language	Python 3.12
Data Processing	Pandas, NumPy
Visualization	Streamlit, Plotly
Database	SQLite3, SQLAlchemy
ML Preparation	Scikit-learn
Environment	Virtual Environments (venv)
📂 Project Structure
Credit-Fraud/
│
├── app/
│   ├── app.py            # Main Streamlit dashboard
│   └── queries.py        # SQL query definitions
│
├── database/
│   ├── setup_db.py       # Database initialization script
│   └── fraud_data.db     # SQLite database
│
├── data/
│   └── creditcard.csv    # Raw dataset
│
├── requirements.txt
└── myenv/                # Virtual environment
⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone <your-repo-url>
cd Credit-Fraud
2️⃣ Setup Virtual Environment
python3 -m venv myenv
source myenv/bin/activate
3️⃣ Install Dependencies
pip install pandas sqlalchemy streamlit plotly scikit-learn
4️⃣ Initialize Database
python3 database/setup_db.py
5️⃣ Run the Dashboard
streamlit run app/app.py
🛡️ Project Organization & Best Practices
Version Control

The project includes a .gitignore file to prevent unnecessary files from being pushed to GitHub such as:

myenv/

__pycache__/

local database files

This keeps the repository clean and secure.

Virtual Environment Isolation

Dependencies are installed in a project-specific virtual environment (myenv) to prevent conflicts with the system Python environment.

Modular Design

The project structure separates concerns:

app/ → Streamlit dashboard

queries.py → SQL query logic

This improves maintainability and readability.

Performance Optimization

Streamlit’s caching system:

@st.cache_data

is used to avoid repeated database queries and improve dashboard loading speed.

🧠 Key Learnings
Handling Class Imbalance

The dataset contains only ~0.17% fraudulent transactions, which highlights the importance of:

Precision

Recall

PR Curve

instead of relying solely on accuracy.

Feature Transformation

Transaction amounts are highly skewed, so log scaling was applied to normalize distributions.

Database-First Architecture

Using a database layer instead of loading full CSVs in memory improves:

performance

scalability

query efficiency

👨‍💻 Author

Janaki Nath Verma

📌 Project Status

✅ Completed