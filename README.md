<div align="center">

# 🩺 DiabetesIQ
### Smart Diabetes Risk Predictor — Input. Predict. Know Your Risk.

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

<br/>

![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=flat-square)
![Accuracy](https://img.shields.io/badge/Model_Accuracy-~79%25-blue?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-Pima_Indians_(UCI)-orange?style=flat-square)
![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)

<br/>

> **Enter 8 basic health values. Get an instant diabetes risk prediction with confidence score, probability breakdown, and personalized health tips — all powered by Logistic Regression.**

</div>

---

## 📸 Screenshots

| Patient Input Form | Diabetic Result |
|---|---|
| <img src="https://github.com/user-attachments/assets/7a49a4fa-a3c7-4ab2-b80e-bf604c4595d8" width="100%"/> | <img src="https://github.com/user-attachments/assets/262c93c5-6fe3-429d-8e0e-d412b7c92ccd" width="100%"/> |

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔬 Prediction Engine
- 📊 **Risk Prediction** — Logistic Regression trained on 768 real patient records
- 🎯 **Confidence Score** — Know exactly how certain the model is
- 📈 **Probability Bars** — Visual Diabetic vs Healthy breakdown
- 💡 **Health Tips** — Personalized advice after every prediction

</td>
<td width="50%">

### ⚙️ Technical Highlights
- 🧹 **Smart Data Cleaning** — Zero values replaced with column means
- ⚡ **Instant Results** — Async fetch API, no page reload
- 📦 **Model Persistence** — Saved as `.pkl`, loads instantly on startup
- 🌐 **No frameworks** — Pure HTML, CSS & JavaScript frontend

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.9+, Flask | Server & prediction API |
| **ML Model** | scikit-learn | Logistic Regression + StandardScaler |
| **Dataset** | Pima Indians Diabetes (UCI) | 768 records, 8 features |
| **Frontend** | HTML, CSS, JavaScript | UI — no frameworks needed |
| **Model Storage** | Pickle | Save & load trained model |

---

## 📁 Project Structure

```
diabetes-prediction/
│
├── 📄 diabetes_model.py      ← Data cleaning, model training, saves .pkl files
├── 📄 app.py                 ← Flask backend + prediction API route
├── 📋 requirements.txt       ← Python dependencies
├── 📖 README.md              ← You are here
│
└── 📂 templates/
    └── index.html            ← Full frontend UI (light theme)
```

> 💡 `model.pkl` and `scaler.pkl` are generated automatically when you run `diabetes_model.py` — you don't need to create them manually.

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have **Python 3.9+** installed:
```bash
python --version
```

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/diabetes-prediction.git
cd diabetes-prediction
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the Model

```bash
python diabetes_model.py
```

This downloads the Pima Indians dataset, trains the model, and saves `model.pkl` + `scaler.pkl` in the project folder.

---

### 5️⃣ Run the App

```bash
python app.py
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000
```

That's it! 🎉

---

## 📖 How to Use

```
1. Open the App       →   Go to http://127.0.0.1:5000
2. Fill in Values     →   Enter 8 patient health values in the form
3. Click Predict      →   Hit the 🔍 Predict Now button
4. View Result        →   See Diabetic / Not Diabetic with confidence score
5. Read the Tips      →   Check the personalized health tip below the result
```

---

## 📊 How It Works

### ML Pipeline

```
Raw Input  →  Replace 0s with Mean  →  StandardScaler  →  Logistic Regression  →  Result + Confidence
```

### Confidence Levels

```
≥ 70%   →  ✅ High Confidence
50–69%  →  ⚠️  Moderate Confidence
< 50%   →  ❓ Low Confidence
```

### Scoring Breakdown

| Step | What Happens |
|---|---|
| **Data Cleaning** | Zeros replaced with column mean for Glucose, BP, BMI, Insulin, Skin |
| **Normalization** | StandardScaler applied to all 8 features |
| **Prediction** | Logistic Regression outputs class (0/1) + probability |
| **Result** | Label, confidence %, and probability bars shown in UI |

### Model Performance

```
~79% Accuracy   →  ✅ Solid baseline for a student ML project
80 / 20 Split   →  Stratified train/test split used
768 Records     →  Pima Indians Diabetes Dataset (UCI)
```

---

## 🔬 Input Features

| # | Feature | Description | Example |
|---|---|---|---|
| 1 | **Pregnancies** | Number of times pregnant | 2 |
| 2 | **Glucose** | Plasma glucose concentration (mg/dL) | 120 |
| 3 | **Blood Pressure** | Diastolic blood pressure (mmHg) | 70 |
| 4 | **Skin Thickness** | Triceps skinfold thickness (mm) | 20 |
| 5 | **Insulin** | 2-hour serum insulin (μU/mL) | 80 |
| 6 | **BMI** | Body mass index (kg/m²) | 25.5 |
| 7 | **DPF** | Diabetes pedigree function (genetic risk) | 0.52 |
| 8 | **Age** | Age of the patient (years) | 30 |

---

## 🧪 Quick Test

Enter these values to test a **Diabetic** prediction:

```
Pregnancies     →  6
Glucose         →  148
Blood Pressure  →  72
Skin Thickness  →  35
Insulin         →  0
BMI             →  33.6
DPF             →  0.627
Age             →  50
```

**Expected:** 🔴 Diabetic · Confidence ~82%

---

Enter these for a **Healthy** prediction:

```
Pregnancies     →  1
Glucose         →  85
Blood Pressure  →  66
Skin Thickness  →  29
Insulin         →  0
BMI             →  26.6
DPF             →  0.351
Age             →  22
```

**Expected:** 🟢 Not Diabetic · Confidence ~75%

---

## 📦 Dependencies

```txt
flask==3.0.0
scikit-learn==1.4.0
pandas==2.1.4
numpy==1.26.3
```

---

## 🚀 Upcoming Features

- [ ] 🔐 User login & saved prediction history
- [ ] 📊 Multiple ML models — SVM, Random Forest, comparison chart
- [ ] 📱 Mobile responsive improvements
- [ ] 🌐 Deploy to Render / Railway
- [ ] 📄 PDF export of prediction report

---

## ⚠️ Disclaimer

> This app is built **for educational purposes only**.
> Predictions are based on a machine learning model and are **not** a substitute for professional medical advice.
> Always consult a qualified doctor for any health-related decisions.

---

## 🤝 Contributing

Contributions are welcome!

```bash
# 1. Fork the repo
# 2. Create your branch
git checkout -b feature/your-feature

# 3. Commit your changes
git commit -m "✨ Add your feature"

# 4. Push and open a Pull Request
git push origin feature/your-feature
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and share.

---

<div align="center">

### 👨‍💻 Author

**Abdul Moiz Khan**
*Software Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Moiz8798)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/moiz-khan90?utm_source=share_via&utm_content=profile&utm_medium=member_android)

<br/>

⭐ **Star this repo if you found it helpful!**

*Made with ❤️ by Abdul Moiz Khan*

</div>
