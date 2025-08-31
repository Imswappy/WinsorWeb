# Outlier Detection & Data Cleaning Web App

## 📊 Overview
A Flask-based data science application for **statistical outlier detection, visualization, and cleaning**.  
The app provides interactive insights into normal distribution analysis using the **Empirical Rule (68-95-99.7)** and applies **Winsorization** for robust outlier treatment.  

---

## 🚀 Features
- **Outlier Detection (Z-Score Method):**
  - Identifies extreme values beyond ±3σ using normal distribution properties.
  - Provides statistical insights (Mean, Standard Deviation, Standard Error).
- **Interactive PDF Plot:**
  - Visualizes probability density function with highlighted outliers.
  - Built using Plotly for dynamic graph rendering.
- **Winsorization (Robust Data Cleaning):**
  - Applies 5% Winsorization on dataset for treating extreme values.
  - Displays original vs cleaned data side by side.
- **Web Application (Flask):**
  - Clean UI with separate pages for analysis and cleaned dataset view.

---

## 🛠️ Technologies & Libraries Used
- **Flask** → Web framework for routing and UI integration.  
- **Pandas** → Data manipulation and analysis (`outlier.csv`, `dataset.csv`).  
- **NumPy** → Numerical computations, percentiles, and array processing.  
- **SciPy (stats)** → Normal distribution (PDF), SEM, and Z-score calculation.  
- **Plotly Graph Objects** → Interactive probability density function plots.  
- **Plotly I/O** → Conversion of plots into HTML for Flask rendering.  
- **OS Module** → File handling and dataset existence checks.  

---

## 📈 Workflow

### 🔹 Home Page (Outlier Detection & Normal Distribution)
1. Load dataset (`outlier.csv`).  
2. Compute statistics → **Mean, Standard Deviation, Standard Error**.  
3. Apply **Empirical Rule (68-95-99.7)** to interpret spread.  
4. Detect outliers using **Z-Score > ±3**.  
5. Visualize via **interactive PDF plot** with highlighted outliers.  

### 🔹 Clean Data Page (Winsorization)
1. Load dataset (`dataset.csv`) or generate dummy dataset if not found.  
2. Apply **5% Winsorization** → clip values below 5th percentile & above 95th percentile.  
3. Display **side-by-side comparison**: Original vs Winsorized values.  

---

## 📂 Project Structure
```
├── app.py                # Main Flask application
├── templates/
│   ├── index.html        # Homepage for outlier detection
│   ├── clean_data.html   # Winsorized dataset view
├── static/               # CSS, JS, images if required
├── dataset.csv           # Input dataset for Winsorization (optional)
├── outlier.csv           # Input dataset for outlier detection
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/outlier-detection-app.git
   cd outlier-detection-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Flask app:
   ```bash
   python app.py
   ```

4. Open browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Example Outputs
- **PDF Plot with Outliers Highlighted**  
- **Table of Outliers**  
- **Winsorized Dataset Table**  

---

## ✅ Conclusion
This application combines **statistics, visualization, and robust data cleaning** into a seamless web interface.  
It is particularly useful for **data preprocessing, anomaly detection, and exploratory data analysis (EDA)** in machine learning pipelines.

