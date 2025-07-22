# insurance-cost-modeling-aids
A clean and statistically validated data pipeline for analyzing health insurance charges. Includes EDA, encoding, feature engineering (BMI categories), p-value-based selection, and final dataset preparation for modeling
# 🏥 Insurance Charges Analysis with Feature Engineering

This project analyzes the factors affecting health insurance charges using Python and statistical techniques. It includes exploratory data analysis (EDA), feature preprocessing, BMI-based categorization, and statistically validated feature selection using correlation and p-values. Final output is a clean, model-ready dataset.

---

## 🔍 Project Goals

- Identify key drivers of insurance costs
- Validate features using point-biserial correlation and p-value logic
- Engineer and encode BMI categories
- Prepare final dataset for modeling

---

## 📁 Dataset

- Source: `insurance.csv`
- Columns: age, sex, BMI, children, smoker status, region, charges

---

## 🔧 Techniques Used

- ✅ Exploratory Data Analysis
- ✅ Label + One-Hot Encoding
- ✅ Feature Engineering (BMI Categories)
- ✅ Scaling with StandardScaler
- ✅ Statistical Validation (p-values vs alpha)
- ✅ Final feature selection pipeline

---

## 📊 Feature Selection Logic

Features are retained based on:
- Low p-value (≤ 0.05) → statistically significant
- Reasonable correlation with `charges`
- Predictive potential confirmed through point-biserial test

---

## 📦 Final Feature Set

| Feature             | Type       | Notes                         |
|---------------------|------------|-------------------------------|
| `age`               | Numeric    | Scaled                       |
| `is_male`           | Binary     | Encoded                      |
| `bmi`               | Numeric    | Scaled                       |
| `children`          | Numeric    | Scaled                       |
| `is_smoker`         | Binary     | Strong predictor              |
| `region_southeast`  | Binary     | From one-hot encoding         |
| `bmi_category_*`     | Binary     | Engineered features (Normal, Overweight, Obese) |

---

## 📈 Next Steps

- Build regression models (Linear, Ridge, Random Forest)
- Compare predictions vs actual charges
- Fine-tune and evaluate performance
- Add visualizations (heatmaps, prediction scatter plots)

---

## 🚀 Tools & Libraries

`Python`, `pandas`, `numpy`, `seaborn`, `matplotlib`, `scikit-learn`, `scipy`

---

## 💬 Author

**shubham**  
Bachelor in Computer Applications — Specialization in Artificial Intelligence and Data Science  
📍 Passionate about statistical modeling, feature engineering, and real-world analytics

---

Let me know if you want this formatted into a notebook or if you’d like a badge or banner idea to give it visual pop 👨‍💻✨
