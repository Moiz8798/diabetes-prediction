<div align="center">

# 🩺 DiabetesIQ
### Smart Diabetes Risk Predictor — Input. Predict. Know Your Risk.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

<br/>

> **Enter 8 basic health values. Get an instant diabetes risk prediction with confidence score, probability breakdown, and personalized health tips — all powered by Logistic Regression.**

<br/>

</div>

---

## 🖼️ Screenshots
<img width="851" height="413" alt="image" src="https://github.com/user-attachments/assets/7a49a4fa-a3c7-4ab2-b80e-bf604c4595d8" />

---

<img width="788" height="415" alt="image" src="https://github.com/user-attachments/assets/262c93c5-6fe3-429d-8e0e-d412b7c92ccd" />


---
### 🏠 Main Form — Patient Input
<!-- Upload your screenshot and replace the src below -->
<!-- <img width="935" height="410" alt="DiabetesIQ Main Form" src="screenshots/form.png" /> -->
> 📸 *Add screenshot: run the app → take a screenshot of the form → upload to GitHub as `screenshots/form.png`*

---

### 🔴 Prediction Result — Diabetic
<!-- <img width="587" height="410" alt="DiabetesIQ Diabetic Result" src="screenshots/result_diabetic.png" /> -->
> 📸 *Add screenshot: fill in the Quick Test values → take a screenshot of the red result card*

---

### 🟢 Prediction Result — Not Diabetic
<!-- <img width="473" height="372" alt="DiabetesIQ Healthy Result" src="screenshots/result_healthy.png" /> -->
> 📸 *Add screenshot: fill in low-risk values → take a screenshot of the green result card*

---

> **How to add screenshots:**
> 1. Run the app locally
> 2. Take screenshots of the UI
> 3. Create a `screenshots/` folder in your repo
> 4. Upload the images and uncomment the `<img>` lines above

---

## ✨ Features

<table>
<tr>
<td>

**📊 Risk Prediction**
Logistic Regression trained on 768 real patient records — instant Diabetic / Not Diabetic result

</td>
<td>

**🎯 Confidence Score**
Shows model confidence % so you know how certain the prediction is

</td>
</tr>
<tr>
<td>

**📈 Probability Bars**
Visual breakdown of Diabetic vs Healthy probability side by side

</td>
<td>

**💡 Health Tips**
Personalized tips shown after each prediction based on your result

</td>
</tr>
<tr>
<td>

**🧹 Smart Data Cleaning**
Zero values replaced with column means — same preprocessing used in real ML pipelines

</td>
<td>

**⚡ Instant Results**
No page reload — async fetch API delivers results in milliseconds

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
├── 📄 diabetes_model.py      ← data cleaning, model training, saves .pkl files
├── 📄 app.py                 ← Flask backend + prediction API route
├── 📋 requirements.txt       ← Python dependencies
├── 📖 README.md              ← You are here
│
└── 📂 templates/
    └── index.html            ← Full frontend UI (light theme)
```

> `model.pkl` and `scaler.pkl` are generated automatically when you run `diabetes_model.py`

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

This downloads the Pima Indians dataset and saves `model.pkl` + `scaler.pkl` in the project folder.

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

### Prediction Model
Trains a **Logistic Regression** classifier on the Pima Indians Diabetes dataset. The data is preprocessed by replacing biologically invalid zero values with column means, then normalized using **StandardScaler** before training.

```
Confidence ≥ 70%  →  ✅ High confidence prediction
Confidence 50–69% → ⚠️  Moderate confidence
```

### Scoring Breakdown

| Step | What Happens |
|---|---|
| Data Cleaning | Zeros replaced with column mean for Glucose, BP, BMI, Insulin, Skin |
| Normalization | StandardScaler applied to all 8 features |
| Prediction | Logistic Regression outputs class (0/1) + probability |
| Result | Label, confidence %, and probability bars shown in UI |

### Accuracy on Test Set

```
~79% Accuracy   →  ✅ Solid baseline for a student ML project
80/20 Split     →  Stratified train/test split used
```

---

## 🔬 Input Features

| # | Feature | Description | Example |
|---|---------|-------------|---------|
| 1 | Pregnancies | Number of times pregnant | 2 |
| 2 | Glucose | Plasma glucose concentration (mg/dL) | 120 |
| 3 | Blood Pressure | Diastolic blood pressure (mmHg) | 70 |
| 4 | Skin Thickness | Triceps skinfold thickness (mm) | 20 |
| 5 | Insulin | 2-hour serum insulin (μU/mL) | 80 |
| 6 | BMI | Body mass index (kg/m²) | 25.5 |
| 7 | DPF | Diabetes pedigree function (genetic risk) | 0.52 |
| 8 | Age | Age of the patient (years) | 30 |

---

## 🧪 Quick Test

Enter these values to test the app:

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

**Expected result:** 🔴 Diabetic · Confidence ~82%

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
- [ ] 📊 More ML models — SVM, Random Forest, comparison chart
- [ ] 📱 Mobile responsive improvements
- [ ] 🌐 Deploy to Render / Railway
- [ ] 📄 PDF export of prediction report

---

## ⚠️ Disclaimer

This app is built **for educational purposes only**. The predictions are based on a machine learning model and are **not** a substitute for professional medical advice. Always consult a qualified doctor for any health-related decisions.

---

## 🙋‍♂️ About

**Developer:** Abdul Moiz Khan
**Stack:** Python · Flask · scikit-learn · HTML · CSS · JavaScript

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and share.

---

<div align="center">

⭐ **Star this repo if you found it helpful!**

Made with ❤️ Abdul Moiz Khan

</div>
