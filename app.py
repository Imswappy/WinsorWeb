from flask import Flask, render_template
import pandas as pd
import numpy as np
from scipy.stats import norm, zscore, sem
import plotly.graph_objs as go
import plotly.io as pio
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Load dataset
    df = pd.read_csv("outlier.csv")

    # Basic stats
    mean_age = df['age'].mean()
    std_dev_age = df['age'].std()
    std_err_age = sem(df['age'])

    # Empirical rule
    one_sd = (mean_age - std_dev_age, mean_age + std_dev_age)
    two_sd = (mean_age - 2*std_dev_age, mean_age + 2*std_dev_age)
    three_sd = (mean_age - 3*std_dev_age, mean_age + 3*std_dev_age)

    # Interpretation
    if std_dev_age < 5:
        interpretation = "Most age values are close to the mean."
    elif std_dev_age < 10:
        interpretation = "There's a moderate spread around the mean."
    else:
        interpretation = "Age values are widely spread out."

    # PDF plot
    x_vals = np.linspace(df['age'].min(), df['age'].max(), 100)
    pdf = norm.pdf(x_vals, mean_age, std_dev_age)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=pdf, mode='lines', name='Normal PDF', line=dict(color='blue')))
    
    z_scores = zscore(df['age'])
    outliers = df[(z_scores < -3) | (z_scores > 3)]

    fig.add_trace(go.Scatter(
        x=outliers['age'], y=[0]*len(outliers), mode='markers',
        name='Outliers', marker=dict(color='red', size=10)
    ))

    fig.update_layout(title="PDF of Age", xaxis_title="Age", yaxis_title="Density")

    graph_html = pio.to_html(fig, full_html=False)

    return render_template("index.html",
                           mean=mean_age, std=std_dev_age, se=std_err_age,
                           one_sd=one_sd, two_sd=two_sd, three_sd=three_sd,
                           interpretation=interpretation,
                           graph_html=graph_html,
                           outliers=outliers[['age']].values.tolist())

@app.route('/clean_data')
def clean_data():
    """
    Loads the dataset, applies Winsorization to the 'age' column,
    and renders an HTML page to display the original and winsorized data directly.
    """
    # Hakikisha dataset.csv ipo kwenye saraka moja na app.py
    # Kwa madhumuni ya maonyesho, tutaunda dataset bandia ikiwa haipo.
    dataset_path = 'dataset.csv'
    if not os.path.exists(dataset_path):
        # Unda dataset bandia kwa madhumuni ya maonyesho
        data = {
            'age': np.concatenate([
                np.random.randint(18, 65, 90), # Umri wa kawaida
                np.random.randint(5, 15, 5),  # Outliers za chini
                np.random.randint(70, 90, 5)  # Outliers za juu
            ]),
            'name': [f'Person_{i}' for i in range(100)]
        }
        dummy_df = pd.DataFrame(data)
        dummy_df.to_csv(dataset_path, index=False)
        print(f"Imeunda {dataset_path} bandia kwa maonyesho.")

    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        return "Hitilafu: dataset.csv haikupatikana. Tafadhali hakikisha ipo kwenye saraka moja na app.py", 404
    except Exception as e:
        return f"Hitilafu wakati wa kupakia dataset: {e}", 500

    if 'age' not in df.columns:
        return "Hitilafu: Safu wima ya 'age' haikupatikana kwenye dataset.csv", 400

    # Bainisha thamani za asilimia kwa Winsorization
    winsor_percentile = 5  # Weka asilimia ya 5 na 95 kwa mipaka ya chini na juu

    # Kokotoa mipaka ya Winsorization
    lower_bound = np.percentile(df['age'], winsor_percentile)
    upper_bound = np.percentile(df['age'], 100 - winsor_percentile)

    # Winsorization
    df['age_winsorized'] = df['age'].clip(lower=lower_bound, upper=upper_bound)

    # Andaa data kwa jedwali la HTML
    # Tutatuma orodha ya kamusi kwenye template kwa urahisi wa kuzunguka
    cleaned_data = df[['age', 'age_winsorized']].to_dict(orient='records')

    return render_template('clean_data.html', data=cleaned_data)

if __name__ == "__main__":
    app.run(debug=True)
