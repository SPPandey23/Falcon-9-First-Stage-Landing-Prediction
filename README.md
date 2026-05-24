<div align="center">

  <h1> Falcon 9 First Stage Landing Predictor</h1>

  <h3>
    End-to-End Machine Learning System for Predicting SpaceX Falcon 9 Booster Landing Success
  </h3>

  <p>
    Built using real SpaceX launch data, feature engineering, model optimization,
    FastAPI deployment, and an interactive Streamlit dashboard.
  </p>

  <br>

  <p>
    <img src="https://img.shields.io/badge/Test%20Accuracy-94.44%25-brightgreen?style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Cross%20Validation-83.33%25-blue?style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Best%20Model-Random%20Forest-orange?style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Launches%20Analysed-90-red?style=for-the-badge"/>
  </p>

  <br>

  <img src="https://github.com/SPPandey23/Falcon-9-First-Stage-Landing-Prediction/blob/main/assests/HomePage.png" width="900"/>

  <br><br>

  <p>
    Predicting reusable rocket landings has major implications for launch economics,
    mission planning, and aerospace risk assessment.
  </p>

</div>

<hr>

<h2>📌 Overview</h2>

<p>
This project builds a complete machine learning pipeline capable of predicting whether
the Falcon 9 first-stage booster will successfully land after launch.
</p>

<p>
The system demonstrates the full machine learning lifecycle:
</p>

<ul>
  <li>Live SpaceX API data collection</li>
  <li>Data preprocessing & feature engineering</li>
  <li>Exploratory data analysis</li>
  <li>Model training & optimization</li>
  <li>REST API deployment with FastAPI</li>
  <li>Interactive dashboard development using Streamlit</li>
</ul>

<hr>

<h2> System Architecture</h2>

<pre>
┌─────────────────────┐
│ Streamlit Dashboard │
└──────────┬──────────┘
           │ HTTP Requests
           ▼
┌─────────────────────┐
│    FastAPI Server   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ ML Prediction Layer │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Random Forest Model │
└─────────────────────┘
</pre>
<h2>🛠 Tech Stack</h2>

<table>
  <tr>
    <th>Category</th>
    <th>Technologies</th>
  </tr>

 

  <tr>
    <td><b>Machine Learning</b></td>
    <td>scikit-learn, Pandas, NumPy</td>
  </tr>

  <tr>
    <td><b>Visualization</b></td>
    <td>Matplotlib, Seaborn, Folium</td>
  </tr>

  <tr>
    <td><b>Backend</b></td>
    <td>FastAPI</td>
  </tr>

  <tr>
    <td><b>Frontend</b></td>
    <td>Streamlit</td>
  </tr>

  <tr>
    <td><b>Deployment</b></td>
    <td>Uvicorn</td>
  </tr>
</table>




<h2> Problem Statement</h2>

<p>
Reusable rocket boosters significantly reduce launch costs.
Predicting landing success enables better mission planning,
risk assessment, and operational optimization.
</p>

<p>
This project classifies Falcon 9 booster landings into:
</p>

<ul>
  <li> Successful Landing</li>
  <li> Failed Landing</li>
</ul>

<p>
using mission parameters such as:
</p>

<ul>
  <li>Payload mass</li>
  <li>Orbit type</li>
  <li>Launch site</li>
  <li>Booster reuse history</li>
  <li>Hardware configuration</li>
</ul>


<hr>

<h2> Dataset Summary</h2>

<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>

  <tr>
    <td>Total Launch Records</td>
    <td>90</td>
  </tr>

  <tr>
    <td>Features After Engineering</td>
    <td>83</td>
  </tr>

  <tr>
    <td>Launch Period</td>
    <td>2010 – 2020</td>
  </tr>

  <tr>
    <td>Target Variable</td>
    <td>Landing Success</td>
  </tr>
</table>

<hr>

<h2>⚙️ Feature Engineering</h2>

<ul>
  <li>Handled missing values</li>
  <li>One-hot encoded categorical variables</li>
  <li>Applied StandardScaler normalization</li>
  <li>Created 83-dimensional feature space</li>
  <li>Prepared train/test split for evaluation</li>
</ul>

<hr>

<h2> Machine Learning Models</h2>

<table>
  <tr>
    <th>Model</th>
    <th>Status</th>
  </tr>

  <tr>
    <td>Random Forest</td>
    <td>🥇 Best Performer</td>
  </tr>

  <tr>
    <td>Logistic Regression</td>
    <td>Evaluated</td>
  </tr>

  <tr>
    <td>Support Vector Machine</td>
    <td>Evaluated</td>
  </tr>

  <tr>
    <td>K-Nearest Neighbors</td>
    <td>Evaluated</td>
  </tr>

  <tr>
    <td>Decision Tree</td>
    <td>Evaluated</td>
  </tr>
</table>

<br>

<h3>🏆 Best Model Performance</h3>

<table>
  <tr>
    <th>Metric</th>
    <th>Score</th>
  </tr>

  <tr>
    <td>Test Accuracy</td>
    <td><strong>94.44%</strong></td>
  </tr>

  <tr>
    <td>Cross Validation Score</td>
    <td><strong>83.33%</strong></td>
  </tr>

  <tr>
    <td>Best Model</td>
    <td>Random Forest Classifier</td>
  </tr>
</table>

<br>

<h3>Best Hyperparameters</h3>

<pre>
RandomForestClassifier(
    criterion="gini",
    n_estimators=10,
    min_samples_leaf=2
)
</pre>

<hr>

<h2> REST API Example</h2>

<h3>POST /predict</h3>

<pre>
{
  "FlightNumber": 90,
  "PayloadMass": 5300,
  "Flights": 2,
  "Block": 5,
  "ReusedCount": 1,
  "Orbit": "LEO",
  "LaunchSite": "KSC LC 39A",
  "GridFins": true,
  "Reused": true,
  "Legs": true
}
</pre>

<h3>Response</h3>

<pre>
{
  "prediction_label": "Success",
  "probability_success": 0.87
}
</pre>

<hr>

<h2>🎛 Dashboard Preview</h2>

<p align="center">
  <img src="https://github.com/SPPandey23/Falcon-9-First-Stage-Landing-Prediction/blob/main/assests/Result.png" width="850"/>
</p>

<hr>

<h2> Key Highlights</h2>

<ul>
  <li>Production-style ML architecture</li>
  <li>Interactive prediction dashboard</li>
  <li>REST API deployment using FastAPI</li>
  <li>End-to-end ML lifecycle implementation</li>
  <li>Real-world aerospace dataset</li>
  <li>Hyperparameter optimization using GridSearchCV</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
falcon9-landing-predictor/
│
├── model/
│   ├── main.py
│   ├── schema.py
│   └── app.py
│
├── datasets/
├── assets/
├── falcon9_model.pkl
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>🚀 Getting Started</h2>

<pre>
# Clone repository
git clone https://github.com/SPPandey23/falcon9-landing-predictor.git

# Navigate into project
cd falcon9-landing-predictor

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload

# Run Streamlit dashboard
streamlit run app.py
</pre>

<hr>

<h2>Future Improvements</h2>

<ul>
  <li>Train using latest SpaceX missions</li>
  <li>Add Docker support</li>
  <li>Deploy publicly on cloud infrastructure</li>
  <li>Add CI/CD pipeline</li>
</ul>

<hr>

<h2>👤 Author</h2>

<div align="center">

<h3>SP Pandey</h3>

<p>
Passionate about Machine Learning, Backend Engineering, and Space Technology 🚀
</p>

<p>
  <a href="https://github.com/SPPandey23">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

</div>

<hr>

<div align="center">

<h3>⭐ If you found this project interesting, consider starring the repository.</h3>

</div>
