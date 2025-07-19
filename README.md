# 🚀 AutoCleanAI: Real-Time AI-Powered Data Quality Monitoring & Cleaning System

AutoCleanAI is a **production-grade, intelligent data quality framework** that automatically detects, explains, and corrects data issues in real-time — powered by machine learning, Airflow, Great Expectations, and Streamlit.

> ⚡ Built with hiring managers in mind to showcase real-world data engineering skills.

---

## 📌 Why AutoCleanAI?

💥 **Data pipelines break silently** due to dirty or drifting data.  
🔍 AutoCleanAI watches your data 24/7 — detecting anomalies, cleaning, and explaining issues automatically.  
📊 It gives data engineers and analysts a live dashboard to monitor and fix quality issues before business is impacted.

---

## 🧠 Architecture Diagram

![AutoCleanAI Architecture](https://github.com/Sai123444/AutoCleanAI/assets/YOUR_IMAGE_ID_HERE/architecture.png)

> (You can upload a diagram later and update the link above.)

---

## ✨ Key Features

- 🧼 **AI-Powered Data Cleaning:** Intelligent imputations, outlier detection, and label corrections.
- 🚨 **Anomaly Detection:** Uses statistical + ML-based techniques to detect schema drifts, missing values, and distribution shifts.
- 🔍 **Explainable Errors:** Explains why a data point is anomalous (e.g. z-score, missingness, invalid types).
- 📊 **Streamlit Dashboard:** Visualizes detected issues, their severity, and trends in real time.
- 🔁 **Airflow DAGs:** Automates the entire ETL → validation → cleaning → dashboard pipeline.
- ✅ **Great Expectations Integration:** Ensures contract-based schema and quality validation.

---

## 🛠 Tech Stack

| Category            | Tools Used                                  |
|---------------------|----------------------------------------------|
| 🐍 Programming       | Python 3.11                                  |
| 💾 Data Processing   | Pandas, Numpy                                |
| 📈 Anomaly Detection | SciKit-Learn, Isolation Forest, Z-Scores     |
| ✅ Data Validation   | Great Expectations                           |
| 🧹 Cleaning Engine   | Custom Python scripts                        |
| 📊 Dashboard         | Streamlit                                    |
| 🔄 Orchestration     | Apache Airflow                               |
| ☁️ Deployment-ready  | Docker (optional), GitHub Actions (CI/CD)    |

---

## 🧪 How to Run Locally

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/Sai123444/AutoCleanAI.git
cd AutoCleanAI
✅ Step 2: Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Linux/macOS
✅ Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔄 Run the Pipeline (Airflow)
Set Up Airflow (basic)
bash
Copy
Edit
# Initialize Airflow DB
airflow db init

# Create user
airflow users create --username admin --password admin --role Admin --email admin@example.com --firstname Admin --lastname User

# Start web server
airflow webserver --port 8080

# In new terminal
airflow scheduler
Go to: http://localhost:8080

Trigger autoclean_dag

📊 Launch Streamlit Dashboard
bash
Copy
Edit
streamlit run dashboard/app.py
📁 File Structure
graphql
Copy
Edit
AutoCleanAI/
│
├── src/
│   ├── ingest.py              # Ingests raw CSV files
│   ├── profile.py             # Profiles data
│   ├── detect_anomalies.py   # Finds outliers, schema drift
│   ├── clean.py               # Fixes or drops bad records
│   └── explain.py             # Explains issues found
│
├── dags/
│   └── autoclean_dag.py       # Airflow DAG to orchestrate all steps
│
├── dashboard/
│   └── app.py                 # Streamlit dashboard
│
├── data/
│   └── input.csv              # Sample data file (replace with yours)
│
├── requirements.txt
└── README.md
🧾 Sample Input/Output
✅ Input (data/input.csv):
csv
Copy
Edit
id, age, income, gender
1, 25, 30000, Male
2, , 50000, Female
3, 80, -1000, Male
🔍 Detected Issues:
Missing age

Negative income (invalid)

Possible outlier: age = 80

🧼 Cleaned Output:
csv
Copy
Edit
id, age, income, gender
1, 25, 30000, Male
2, 30, 50000, Female        # Age imputed
3, 80, NULL, Male           # Negative income flagged or removed
🎥 Demo (Optional)
🔗 Add a screen recording link here once ready
e.g., Watch the Demo Video

👨‍💻 Author
Sreesai Malli
🔗 GitHub | 📫 mallisreesai2004@gmail.com

📢 Hiring?
I'm actively looking for a Data Engineer / Python Developer role.
AutoCleanAI showcases my skills in:

Building production-ready data pipelines

AI/ML integration into ETL

Airflow orchestration & Streamlit dashboards

Let's connect!

⭐ Show Your Support
If you liked this project:

Give it a ⭐ on GitHub

Share with your network

yaml
Copy
Edit

---

Would you like me to auto-upload this to your GitHub repo or give you the `.md` file to copy manually?
