# 🎯 Simple Marks Predictor  

This project is a machine learning app that predicts **student marks based on study hours**.  
It uses a **Linear Regression model** for training and a **Streamlit app** for interactive predictions.  

---

## 📂 Project Files  

- **`model.py`** → Trains the Linear Regression model using dataset (`marks - Sheet1.csv`) and saves it as `mymarksmodel` using **joblib**.  
- **`marks_predictor_model.py`** → Streamlit app that loads the trained model and predicts marks based on hours of study.  
- **`marks - Sheet1.csv`** → Simple dataset with columns:  
  - `hrs` → Hours studied  
  - `marks` → Marks obtained  

---

## ⚙️ Features  

✅ Train & save a Linear Regression model  
✅ Interactive slider in the web app to select study hours  
✅ Instant marks prediction  
✅ Lightweight & beginner-friendly ML project  

---

## 🚀 How to Run  

### 1️⃣ Install  dependencies  
```bash
pip install streamlit scikit-learn pandas joblib

2️⃣ Train  the model
Run the training script to generate `mymarksmodel`:  

```bash
python model.py

3️⃣ Launch  the Streamlit app

```bash
streamlit run marks_predictor_model.py

---
