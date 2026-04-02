# 🛡️ InboxSecure: Mail Spam Detection Terminal

Deployment Link :- https://email-spam-detection-clzdafssvadmmcvo5bceav.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-orange?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Model-Random%20Forest-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A sleek, lightweight Natural Language Processing (NLP) dashboard designed to classify emails and text messages as either safe (Ham) or malicious (Spam). 

This project bypasses complex, heavy UI frameworks in favor of a single-purpose, high-speed cybersecurity terminal, allowing users to paste raw text and receive instant, probabilistically-backed threat assessments.

---

## 🧠 System Architecture

### 1. The NLP Pipeline (TF-IDF)
Raw text cannot be fed directly into a machine learning model. This system utilizes a **Term Frequency-Inverse Document Frequency (TF-IDF) Vectorizer** to transform unstructured email text into a structured, high-dimensional numerical format. It evaluates the mathematical importance of specific words, penalizing common filler words while highlighting rare, spam-indicative vocabulary.

### 2. The Classification Engine (Random Forest)
Once the text is vectorized, it is passed through a **Random Forest Classifier**—an ensemble learning method that constructs a multitude of decision trees during training. It outputs both a binary classification (Safe vs. Spam) and a confidence probability based on the consensus of the decision trees.

---

## 🛠️ Technical Stack

* **Language:** `Python 3.x`
* **Machine Learning:** `scikit-learn` (Random Forest, TF-IDF Vectorizer)
* **Frontend Delivery:** `streamlit` (Styled with custom Zero-Trust/CyberSec CSS)

---

## 📂 Repository Structure

    ├── app.py                  # Main Python application interface
    ├── rf_model.pkl            # Serialized Random Forest Classifier
    ├── tfidf_vectorizer.pkl    # Serialized NLP Vectorizer
    ├── requirements.txt        # Package dependencies
    └── README.md               # System documentation



⚙️ Installation & Deployment
1. Clone the Repository

      git clone [https://github.com/akshitgajera1013/Email-Spam_Detection.git](https://github.com/akshitgajera1013/Email-Spam_Detection.git)

      cd Email-Spam_Detection

3. Install Dependencies

      pip install -r requirements.txt

3. Initialize the Security Terminal

    python -m streamlit run app.py
