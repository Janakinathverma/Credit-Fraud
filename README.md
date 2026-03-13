🛡️ Financial Fraud Detection System v2.0
Ek end-to-end data science project jo credit card transactions mein fraud detection ke liye banaya gaya hai. Is project ka main objective dataset mein class imbalance ko handle karna aur anomaly detection ke liye patterns identify karna hai.

🚀 Features
Interactive Dashboard: Streamlit-based UI jo transaction data, fraud rates, aur amount distributions ko visualize karta hai.

Neural Network Ready: Dashboard ko is tarah design kiya gaya hai ki wo features ko pre-process kar sake (e.g., Log Transformation).

Database Management: SQLite ka use karke efficient query execution.

Analytical Insights: Har chart ke saath actionable insights jo model training strategy (SMOTE/Undersampling) mein madad karte hain.

🛠️ Tech Stack
Language: Python 3.12

Data Processing: Pandas, NumPy

Visualization: Plotly, Streamlit

Database: SQLAlchemy, SQLite3

Environment: Virtual Environments (venv)

📂 Project Structure
Plaintext
Credit-Fraud/
├── app/
│   ├── app.py          # Main Streamlit dashboard
│   └── queries.py      # SQL query definitions
├── database/
│   ├── setup_db.py     # Database initialization script
│   └── fraud_data.db   # SQLite database file
├── data/
│   └── creditcard.csv  # Raw dataset
└── myenv/              # Virtual environment
⚙️ Setup & Installation
Clone the repository:

Bash
git clone <your-repo-link>
cd "Credit Fraud"
Setup Virtual Environment:

Bash
python3 -m venv myenv
source myenv/bin/activate
pip install pandas sqlalchemy streamlit plotly scikit-learn
Initialize Database:

Bash
python3 database/setup_db.py
Run Dashboard:

Bash
streamlit run app/app.py
🧠 Key Learnings
Class Imbalance: Dataset mein sirf ~0.17% fraud cases hain, jiske liye accuracy ke bajaye Precision-Recall curve ka importance samjha.

Feature Scaling: Amount distribution skewed hone ke karan log_y scaling ka upyog kiya.

System Design: Database-first approach use kiya taaki memory usage optimize ho sake.

Author: Janaki Nath Verma

Status: Project Completed