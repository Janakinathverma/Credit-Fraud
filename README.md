# 🛡️ Financial Fraud Detection System v2.0

An **end-to-end data analytics project** focused on exploring credit card transaction data to identify fraud patterns and understand transaction behavior.

The main objective of this project is to **analyze class imbalance in fraud data and extract analytical insights** from transaction distributions.

---

# 🚀 Features

## 📊 Interactive Dashboard

A **Streamlit-based UI** that visualizes:

- Transaction distribution  
- Fraud rates  
- Transaction amount patterns  

---

## 🗄️ Database Management

- Uses **SQLite** for efficient data storage  
- Fast query execution using **SQLAlchemy**

---

## 📈 Analytical Insights

The dashboard provides insights into:

- Fraud vs non-fraud transaction distribution  
- Transaction amount patterns  
- Data imbalance within the dataset  

These insights help in understanding **fraud behavior trends in financial transactions**.

---

# 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| Language | Python 3.12 |
| Data Processing | Pandas, NumPy |
| Visualization | Streamlit, Plotly |
| Database | SQLite3, SQLAlchemy |
| Environment | Virtual Environments (venv) |

---

# 📂 Project Structure


Credit-Fraud/
│
├── app/
│ ├── app.py # Main Streamlit dashboard
│ └── queries.py # SQL query definitions
│
├── database/
│ ├── setup_db.py # Database initialization script
│ └── fraud_data.db # SQLite database
│
├── data/
│ └── creditcard.csv # Raw dataset
│
├── requirements.txt
└── myenv/ # Virtual environment


---

````markdown
## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Credit-Fraud
````

### 2. Setup Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pandas sqlalchemy streamlit plotly
```

### 4. Initialize Database

```bash
python3 database/setup_db.py
```

### 5. Run the Dashboard

```bash
streamlit run app/app.py
```

---

## 🛡️ Project Organization & Best Practices

### Version Control

The project includes a `.gitignore` file to prevent unnecessary files from being pushed to GitHub such as:

* `myenv/`
* `__pycache__/`
* local database files

This keeps the repository **clean and organized**.

### Virtual Environment Isolation

Dependencies are installed in a **project-specific virtual environment (`myenv`)** to avoid conflicts with the system Python environment.

### Modular Design

The project structure separates concerns:

* `app/` → Streamlit dashboard
* `queries.py` → SQL query logic

This improves **code readability and maintainability**.

### Performance Optimization

Streamlit caching is used to avoid repeated database queries and improve dashboard loading performance.

```python
@st.cache_data
```

---

## 🧠 Key Learnings

### Class Imbalance in Financial Data

The dataset contains only **~0.17% fraudulent transactions**, which highlights the extreme imbalance present in fraud datasets.

### Transaction Amount Distribution

Transaction amounts are **highly skewed**, making distribution analysis important for identifying unusual patterns.

### Database-First Data Handling

Using a **database layer instead of loading full CSV files in memory** improves:

* performance
* scalability
* query efficiency

---

## Dashboard
<img width="1851" height="889" alt="image" src="https://github.com/user-attachments/assets/97a8d582-b91b-4ee7-bdb9-79b338f80730" />
<img width="1820" height="755" alt="image" src="https://github.com/user-attachments/assets/8357a6f0-dbe0-43e4-8dcb-bdccb442587a" />


---

## 👨‍💻 Author

**Janaki Nath Verma**

---

## 📌 Project Status

✅ **Completed**

```
```
