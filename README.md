## 🏋️ Athlete Injury Prediction Analysis

### 📌 Overview
This project predicts the likelihood of injury in athletes using biometric and training-related features. By leveraging machine learning models and detailed exploratory data analysis, it aims to support coaches and sports professionals in identifying players at higher risk, enabling proactive injury prevention.

---

### 📊 Features & Highlights

- 🔍 **Exploratory Data Analysis (EDA)**  
  Custom visualization functions to explore distributions and relationships between features like:
  - BMI and its categories
  - Training Intensity vs Injury Probability
  - Player Age, Height, Weight, Recovery Time

- 🛠️ **Feature Engineering**
  - Calculated **BMI** and categorized it into standard health classes
  - One-hot encoded BMI categories for model input

- 🤖 **Machine Learning Models**
  - Trained and evaluated:  
    ✅ Decision Tree  
    ✅ Logistic Regression  
    ✅ Random Forest  
    ✅ Gradient Boosting  
    ✅ Support Vector Machine (LinearSVC)  
  - Visualized and compared accuracies of all models

- 🎯 **Model Performance**
  - Achieved high accuracy with **Random Forest** and **Gradient Boosting**
  - Evaluated using classification reports and confusion matrices

- 🌐 **Model Deployment**
  - Serialized the trained model with `pickle`
  - Deployed using **Flask** for real-time predictions

---

### 🧰 Tech Stack

- **Language**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Pickle  
- **Model Deployment**: Flask

---

