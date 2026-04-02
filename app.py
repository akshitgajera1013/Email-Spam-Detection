# =========================================================================================
# 🛡️ MAIL SPAM DETECTION TERMINAL (CYBERSEC EDITION)
# Description: Lightweight, high-performance UI for TF-IDF & Random Forest text classification.
# Theme: Zero-Trust Security (Deep Charcoal, Threat Crimson, Safe Emerald)
# =========================================================================================

import streamlit as st
import pickle
import time
import pandas as pd
import numpy as np

# =========================================================================================
# 1. PAGE CONFIGURATION
# =========================================================================================
st.set_page_config(
    page_title="Spam Detection Terminal",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================================================
# 2. MACHINE LEARNING ASSET INGESTION
# =========================================================================================
@st.cache_resource
def load_models():
    rf_model = None
    tfidf_vec = None
    
    try:
        with open("rf_model.pkl", "rb") as f:
            rf_model = pickle.load(f)
    except Exception as e:
        st.error(f"🔴 MODEL LOAD ERROR: Ensure `rf_model.pkl` exists. Details: {e}")
        
    try:
        with open("tfidf_vectorizer.pkl", "rb") as f:
            tfidf_vec = pickle.load(f)
    except Exception as e:
        st.error(f"🔴 VECTORIZER LOAD ERROR: Ensure `tfidf_vectorizer.pkl` exists. Details: {e}")
        
    return rf_model, tfidf_vec

model, vectorizer = load_models()

# =========================================================================================
# 3. CYBERSEC CSS INJECTION
# =========================================================================================
st.markdown(
"""<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600;800&display=swap');

.stApp {
    background-color: #09090b;
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

/* Hero Section */
.hero-container {
    text-align: center;
    padding: 40px 0 30px 0;
}
.hero-badge {
    display: inline-block;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #10b981;
    padding: 8px 20px;
    border-radius: 50px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 15px;
}
.hero-title {
    font-size: 45px;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
}
.hero-subtitle {
    color: #94a3b8;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    margin-top: 10px;
}

/* Text Area Customization */
div[data-testid="stTextArea"] > div > div > textarea {
    background-color: #18181b !important;
    border: 1px solid #3f3f46 !important;
    color: #f8fafc !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    padding: 20px !important;
}
div[data-testid="stTextArea"] > div > div > textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.2) !important;
}

/* Button Customization */
div.stButton > button {
    width: 100%;
    background-color: #ffffff !important;
    color: #09090b !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    padding: 20px !important;
    border-radius: 8px !important;
    border: none !important;
    transition: all 0.3s ease !important;
}
div.stButton > button:hover {
    background-color: #e2e8f0 !important;
    transform: translateY(-2px) !important;
}

/* Result Cards */
.result-card {
    padding: 40px;
    border-radius: 12px;
    text-align: center;
    margin-top: 30px;
    animation: popIn 0.5s ease both;
}
.result-safe {
    background: rgba(16, 185, 129, 0.05);
    border: 1px solid rgba(16, 185, 129, 0.4);
    box-shadow: 0 0 30px rgba(16, 185, 129, 0.1);
}
.result-threat {
    background: rgba(225, 29, 72, 0.05);
    border: 1px solid rgba(225, 29, 72, 0.4);
    box-shadow: 0 0 30px rgba(225, 29, 72, 0.1);
}
.result-icon {
    font-size: 50px;
    margin-bottom: 10px;
}
.result-title {
    font-size: 32px;
    font-weight: 800;
    margin: 0 0 10px 0;
}
.title-safe { color: #10b981; }
.title-threat { color: #e11d48; }
.result-prob {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: #94a3b8;
}

@keyframes popIn {
    from { opacity: 0; transform: scale(0.98); }
    to { opacity: 1; transform: scale(1); }
}
</style>""", unsafe_allow_html=True)

# =========================================================================================
# 4. MAIN INTERFACE
# =========================================================================================
st.markdown(
"""<div class="hero-container">
<div class="hero-badge">NLP THREAT DETECTION KERNEL</div>
<div class="hero-title">INBOX SECURE</div>
<div class="hero-subtitle">Random Forest Classifier • TF-IDF Vectorization</div>
</div>""", unsafe_allow_html=True)

# Main input area
user_email = st.text_area(
    "Email Content", 
    height=250, 
    placeholder="Paste the suspicious email, SMS, or message content here to run a heuristic threat analysis...",
    label_visibility="collapsed"
)

# Execution logic
if st.button("INITIATE THREAT SCAN"):
    if not user_email.strip():
        st.warning("⚠️ Please paste email text into the console before scanning.")
    elif model is None or vectorizer is None:
        st.error("🚨 System Offline: Machine Learning assets (.pkl files) are missing.")
    else:
        with st.spinner("Vectorizing text and parsing decision trees..."):
            time.sleep(0.8) # UI Polish
            
            try:
                # 1. Vectorize the input text
                vectorized_text = vectorizer.transform([user_email])
                
                # 2. Make Prediction
                prediction = model.predict(vectorized_text)[0]
                
                # 3. Get Probability (if supported by the model)
                if hasattr(model, "predict_proba"):
                    probs = model.predict_proba(vectorized_text)[0]
                    confidence = max(probs) * 100
                else:
                    confidence = 100.0 # Fallback if predict_proba is disabled
                
                # Assuming standard binary mapping: 1 = Spam, 0 = Ham (Safe)
                # Adjust this logic if your specific model uses different labels (e.g., 'spam' and 'ham')
                is_spam = str(prediction).lower() in ['1', 'spam', 'true']
                
                if is_spam:
                    st.markdown(
f"""<div class="result-card result-threat">
<div class="result-icon">⚠️</div>
<div class="result-title title-threat">MALICIOUS SPAM DETECTED</div>
<div class="result-prob">Algorithmic Confidence: {confidence:.2f}%</div>
</div>""", unsafe_allow_html=True)
                else:
                    st.markdown(
f"""<div class="result-card result-safe">
<div class="result-icon">✅</div>
<div class="result-title title-safe">MESSAGE IS SAFE (INBOX)</div>
<div class="result-prob">Algorithmic Confidence: {confidence:.2f}%</div>
</div>""", unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")

# Footer
st.markdown(
"""<div style="text-align:center; margin-top: 80px; color:#475569; font-family:'JetBrains Mono'; font-size:12px;">
    &copy; 2026 Threat Detection Terminal | Powered by Scikit-Learn
</div>""", unsafe_allow_html=True)